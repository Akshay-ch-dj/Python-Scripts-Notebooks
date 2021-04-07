import os
from mattermost_bot.bot import Bot


if __name__ == "__main__":
    os.environ["MATTERMOST_BOT_SETTINGS_MODULE"] = "mattermost_bot_settings"
    Bot().run()