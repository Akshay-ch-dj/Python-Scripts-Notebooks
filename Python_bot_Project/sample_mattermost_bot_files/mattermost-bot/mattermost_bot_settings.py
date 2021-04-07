import os
DEBUG = False

PLUGINS = [
    'plugins'
]

# Docs + regexp or docs string only
PLUGINS_ONLY_DOC_STRING = False

# Basic configuration
BOT_URL = 'https://mattermost.linways.com/api/v3'
BOT_LOGIN = os.getenv('BOT_LOGIN','db_bot_qa')
BOT_PASSWORD = os.getenv('BOT_PASSWORD','uzhuNNuvada')
BOT_TEAM = 'Linways'




# Ignore broadcast message
IGNORE_NOTIFIES = ['@channel', '@all']

# Threads num
WORKERS_NUM = 5

'''
# Custom default reply module

Example:
filename:
    my_default_reply.py
code:
    def default_reply(dispatcher, raw_msg):
        dispatcher._client.channel_msg(
            raw_msg['channel_id'], dispatcher.get_message(raw_msg)
        )
settings:
    DEFAULT_REPLY_MODULE = 'my_default_reply'
'''
DEFAULT_REPLY_MODULE = None

# or simple string for default answer
DEFAULT_REPLY = None

'''
If you use Mattermost Web API to send messages (with send_webapi()
or reply_webapi()), you can customize the bot logo by providing Icon or Emoji.
If you use Mattermost API to send messages (with send() or reply()),
the used icon comes from bot settings and Icon or Emoji has no effect.
'''
BOT_ICON = 'http://lorempixel.com/64/64/abstract/7/'
BOT_EMOJI = ':godmode:'
