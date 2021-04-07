#!/bin/bash

PID=$(pidof /home/linways/db_bot/mm_bot_env/bin/python /home/linways/db_bot/mattermost-bot/run.py)
if [[ "" !=  "$PID" ]]; then
echo "killing $PID"
  kill -9 $PID
fi
echo "Starting bot..."
export B2_ACCOUNT_ID="29d54173f4bc"
export B2_KEY_ID="00129d54173f4bc0000000002"
export B2_APPLICATION_KEY="K001fYbca9Ok+So9tHtEMkBXe8NkMPM"
export B2_BUCKET="custom-backups-professional"
export SQL_USER="ams_dump_user"
export SQL_PASS="amsuser17092019"
export BOT_LOGIN="db_bot_3@example.com"
export BOT_PASSWORD="db_bot_12_chicken_biriyani"
nohup /home/linways/db_bot/mm_bot_env/bin/python /home/linways/db_bot/mattermost-bot/run.py > /home/linways/db_bot/bot.log 2>&1 &
echo "bot started"
