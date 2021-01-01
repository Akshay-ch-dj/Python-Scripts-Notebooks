# Web Scrapping with python

## [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

* Install using `pip install beautifulsoup4`.
* Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
* Beautifulsoup [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Basics

* As stated bs4(Beautifulsoup version 4) works with html(and xml too), so it needed a html script to parse with, to get a page from the web use the `requests` python module to send a http get request to the server and fetch the page.
* Also needed the user agent for sending the http request header.(just google "my user agent" from the def. browser to get it)
* The `soup.prettify()` gives the html in a human readable prettier format, ie

  ```py
  import requests
  from bs4 import BeautifulSoup

  URL = "<any url that doesn't require authentication>"

  headers = {
      "user-agent": "Mozilla/5.0 ---- AppleWebKit/537.36\
      (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
  }

  page = requests.get(URL, headers=headers)

  # Parse using beautifulsoup
  soup = BeautifulSoup(page.content, 'html.parser')

  # print the prettified version (line-by-line with indentation)
  print(soup.prettify())

  ```

* We don't need all the data, but specific data ie to work with, eg. if need to check price of a particular product in the store, need that only,

* NOTE:- To send a mail using gmail, enable 2 step verification and generate an app password to support low security apps like this then use the [`smtplib`](https://docs.python.org/3/library/smtplib.html) (Simple Mail Transfer Protocol) to send a mail,
* PORT 587 is the default mail submission port. When an email client or outgoing server is submitting an email to be routed by a proper mail server, it should always use SMTP port 587 as the default port.
* A `HELO` is used by client, sends this command to the SMTP server to identify itself and initiate the SMTP conversation. The domain name or IP address of the SMTP client is usually sent as an argument together with the command (e.g. “HELO client.example.com”). `EHLO` is same as HELO but tells the server that the client may want to use the Extended SMTP (ESMTP) protocol instead. EHLO can be used although you will not use any ESMTP command. And servers that do not offer any additional ESMTP commands will normally at least recognize the EHLO command and reply in a proper way.

* A sample script to check if the price of a product fell down and notify via email is here, [`scrapper.py`](../web_scrapper_bewakoof.py)
