from bs4 import BeautifulSoup
import requests
import datetime
import time
import lxml
from keep_alive import keep_alive
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = 'AC723997122710e147b7920e6e7a3ea951'
auth_token = '28df1270546026be34174fa9e126a22d'
client = Client(account_sid, auth_token)
DESIRED_PRICE = 5000

keep_alive()

URL="https://www.goodreturns.in/gold-rates/"
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
}
result = requests.get(URL, headers=headers)
web_page = result.text
soup = BeautifulSoup(web_page, 'lxml')
item_price = soup.find(id='el').get_text().split(' ')[1].replace(',','')

current_price = int(item_price)


while True:
  if current_price <= DESIRED_PRICE and datetime.datetime.now().time().hour==3:
      proxy_client = TwilioHttpClient()
      # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
      client = Client(account_sid, auth_token,         http_client=proxy_client)
      message = client.messages.create(
          body=f"Price of Gold,is now ₹{current_price}.\n Buy Now!",
          from_='+19206682105',
          to='+91 80726 99523'
      )
      print(message.status)
      time.sleep(3600)
      