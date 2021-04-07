import re
import os
import time
import urllib.request
from subprocess import Popen
from subprocess import PIPE
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
import logging


sql_user = os.getenv("SQL_USER", "root")
sql_pass = os.getenv("SQL_PASS", "root")


@respond_to("build (.*)")
def build(message, params):
    if message.get_channel_name() != "bot-house-qa":
        message.send(
            "You need to call `build` command from `bot-house-qa` channel. Otherwise I won't build it for you. :-p "
        )
        return

    params_arr = params.split(" ")
    b2_url = params_arr[0]

    try:
        qa_db_name = params_arr[1]
        if not qa_db_name.startswith(("qa", "cht", "uat", "test")):
            message.send(
                ":man_facepalming: I accept qa database name starting with `qa` or `cht` or `uat` or `test`"
            )
            return
    except Exception as e:
        qa_db_name = ""

    try:
        reset_cmd = params_arr[2]
    except Exception as e:
        reset_cmd = ""

    if message.get_channel_name() not in ["bot-house-qa"]:
        message.send(
            "You need to call `dump "
            + qa_db_name
            + "` command from `bot-house-qa` channel. Otherwise I won't dump it for you. :-p "
        )
        return

    message.send("Please wait while bot download database dump from backblaze...")

    try:
        # downloading database from backblaze
        file_name = b2_url.rpartition("/")[-1]
        unzipped_file_name = file_name.rpartition(".")[0]
        urllib.request.urlretrieve(b2_url, file_name)
        message.send("File downloaded successfully")

        # unzipping file
        cmd = "gunzip " + file_name
        execute_command(cmd)
        message.send("File Unzipped Successfully")

        # drop database
        cmd = (
            "mysql -u"
            + sql_user
            + " -p"
            + sql_pass
            + " -e 'drop database if exists "
            + qa_db_name
            + "'"
        )
        execute_command(cmd)

        # create database
        cmd = (
            "mysql -u"
            + sql_user
            + " -p"
            + sql_pass
            + " -e 'create database "
            + qa_db_name
            + "'"
        )
        execute_command(cmd)
        message.send(
            "Created database "
            + qa_db_name
            + ". Please wait until the build process complete. It may take some time. Have a break :coffee: :taco:"
        )

        # build database
        cmd = (
            "mysql -u"
            + sql_user
            + " -p"
            + sql_pass
            + " "
            + qa_db_name
            + " < "
            + unzipped_file_name
        )
        execute_command(cmd)
        message.send("Database build completed")

        # remove sql dump file
        cmd = "rm *.sql"
        execute_command(cmd)

        if reset_cmd == "reset":
            cmd = "php /root/db_bot/bot_reset_db.php " + qa_db_name
            try:
                pd = Popen(cmd, shell=True, stdout=PIPE)
                message.send("Database reset finished.")
            except Exception as e:
                print(e)
                message.send(
                    ":pray: Sorry! Resetting database was unsuccessful :cry: Please contact my creator :man_technologist:"
                )

    except Exception as e:
        print(e)
        message.send("🔥🔥🔥 Something horribly went wrong. 🚒")
        logging.exception("Error")

    # message.send("@db_bot build complete")


def execute_command(cmd):
    pd = Popen(cmd, shell=True, stdout=PIPE)
    for ln in pd.stdout:
        print("#" + ln)
