import re
import os
import time
import urllib.request
from time import gmtime, strftime
from subprocess import Popen
from subprocess import PIPE
from urllib.parse import urlparse
import logging

from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
from b2blaze import B2

# Get the backblaze credentials
b2_account_id = os.getenv("B2_ACCOUNT_ID", "ea73b5dc53b3")
b2_key_id = os.getenv("B2_KEY_ID", "000ea73b5dc53b30000000002")
b2_app_key = os.getenv("B2_APPLICATION_KEY", "K000uZzNm4myWu0bZDH4SC3YXyJcZRM")
b2_bucket = os.getenv("B2_BUCKET", "linways-test")

sql_user = os.getenv("SQL_USER", "root")
sql_pass = os.getenv("SQL_PASS", "LinW*^(!S(^")


@respond_to("dump (.*)")
def dump(message, params):
    params_arr = params.split(" ")
    db_name = params_arr[0]

    try:
        qa_db_name = params_arr[1]
        if not qa_db_name.startswith(("qa", "cht", "uat", "test")):
            message.reply(
                ":man_facepalming: I accept qa database name starting with `qa` or `cht` or `uat` or `test`"
            )
            return
    except Exception as e:
        qa_db_name = ""

    try:
        reset_cmd = params_arr[2]
    except Exception as e:
        reset_cmd = ""

    if message.get_channel_name() not in ["bot-house", "bot-house-qa"]:
        message.reply(
            "You need to call `dump "
            + db_name
            + "` command from `bot-house` or `bot-house-qa` channel. Otherwise I won't dump it for you. :-p "
        )
        return

    if db_name in ["nucleus", "nucleus_db"]:
        message.reply(
            "Sorry, I don't have the permission to dump this database. Contact @rohith for this database"
        )
        return
    db_name = db_name.strip()
    message.reply("Okay. Please wait. I will upload the db in a moment.")
    tar_file = make_db_dump(db_name)
    message.reply("DB dumped and compressed. Please wait for the upload to complete.")
    try:
        b2_file = upload_to_b2(tar_file, db_name)
        url = get_friendly_url(b2_file)
        cleanup(tar_file)
        message.reply("DB uploaded to Backblaze successfully. Please download :" + url)
        if qa_db_name != "":
            message.send("@db_bot_qa build " + url + " " + qa_db_name + " " + reset_cmd)

    except Exception as e:
        print(e)
        message.reply("🔥🔥🔥 Something horribly went wrong. 🚒")
        logging.exception("Error")


@respond_to("thank you|thanks|thankyou", re.IGNORECASE)
def thanks(message):
    message.reply("You are welcome.")


def make_db_dump(db_name):
    # autonomous db server details dictionary
    database_dictionary = {
        "stjosephs_db": "192.168.129.209",
        "vimala_db": "192.168.129.209",
        "sbcollege_db": "192.168.129.209",
        "christijk_db": "192.168.129.209",
        "dgmmes_db": "192.168.149.96",
        "macollege_db": "192.168.149.96",
        "stthomas_db": "192.168.149.96",
        "stthomasforms_db": "192.168.149.96",
        "sjc_commerce_db": "192.168.145.147",
        "sjc_db": "192.168.145.147",
        "sjec_evening_db": "192.168.145.147",
        "stthomas_exat_db": "192.168.149.96",
        "sjc_exat_db": "192.168.145.147",
        "sjc_commerce_exat_db": "192.168.145.147",
        "vimala_exat_db": "192.168.129.209",
        "mbcet_db": "192.168.149.96",
        "mbcet_exat_db": "192.168.149.96",
    }

    backup_file_name = strftime(db_name + "-%Y-%m-%d-%H-%M.sql", gmtime()) + ".gz"
    # cmd = "mysqldump --routines -u "+ sql_user +" -p"+sql_pass+" "+ db_name+"> " + backup_file_name
    # mysqldump --routines -u root -p meaec_test_db | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/'  |
    # gzip -c> meaec_db_reset.sql.gz

    if db_name in database_dictionary.keys():
        cmd = (
            "mysqldump --routines -h"
            + database_dictionary[db_name]
            + " -u "
            + sql_user
            + " -p"
            + sql_pass
            + " "
            + db_name
            + "| sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | gzip -c > "
            + backup_file_name
        )
    else:
        cmd = (
            "mysqldump --routines -u "
            + sql_user
            + " -p"
            + sql_pass
            + " "
            + db_name
            + "| sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' | gzip -c > "
            + backup_file_name
        )

    pd = Popen(cmd, shell=True, stdout=PIPE)
    for ln in pd.stdout:
        print("#" + ln)

    print("-> dump finished")

    return backup_file_name


def upload_to_b2(tar_file, db_name):
    b2 = B2(b2_key_id, b2_app_key)
    bucket = b2.buckets.get(b2_bucket)
    f1 = open(tar_file, "rb")
    new_file = bucket.files.upload(
        contents=f1, file_name=db_name + "/" + tar_file, progress_listener=print
    )
    return new_file


def get_friendly_url(b2_file):
    url = urlparse(b2_file.url)
    file_url = "{uri.scheme}://{uri.netloc}".format(uri=url)
    file_url = file_url + "/file/" + b2_bucket + "/" + b2_file.file_name
    return file_url


def cleanup(tar_file):
    os.remove(tar_file)
