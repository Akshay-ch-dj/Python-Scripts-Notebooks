import requests
import smtplib
import os
from dotenv import load_dotenv, find_dotenv

from bs4 import BeautifulSoup

URL = "https://www.bewakoof.com/p/hogwarts-crest-half-sleeve-t-shirt-for-men"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# loading the env. variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_dir = os.path.join(BASE_DIR, '.env')
load_dotenv(env_dir)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Extended Hello
    server.ehlo()
    # secure the connection
    server.starttls()
    server.ehlo()

    server.login(os.environ.get('EMAIL1'), os.environ.get('PASSWORD'))

    subject = "The price fell down"
    body = f"Check the link:- {URL}"

    # Actual message
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        os.environ.get('EMAIL1'),
        os.environ.get('EMAIL2'),
        msg
    )

    print("Email has been sent!")
    server.quit()


def check_price():
    page = requests.get(URL, headers=headers)

    # Parse using beautifulsoup
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get the price using id=testNetProdPrice
    price = int(soup.find(id="testNetProdPrice").get_text())

    if price > 300:
        send_email()


check_price()
