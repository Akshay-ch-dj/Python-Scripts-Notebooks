import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# For django BASE_DIR is the path where manage.py lies
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Get env using os.path.join()

# env_dir = os.path.join(BASE_DIR, 'django-config.env')
# env_dir = dotenv.find_dotenv('django-config.env')
# print(env_dir)

# dotenv.load_dotenv(env_dir)
# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = os.getenv('SECRET_KEY')

print(SECRET_KEY)
