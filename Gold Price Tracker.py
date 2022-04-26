from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = 'AC723997122710e147b7920e6e7a3ea951'
auth_token = 'a32647faa50e81b37c3e3470bd54cf21'
client = Client(account_sid, auth_token)
DESIRED_PRICE = 5000

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

print(current_price)

if current_price <= DESIRED_PRICE:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body=f"Price of Gold,is now ₹{current_price}.\n Buy Now!",
        from_='+19206682105',
        to='+91 80726 99523'
    )
    print(message.status)