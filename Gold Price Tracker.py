from bs4 import BeautifulSoup
import requests
import smtplib

MY_EMAIL = 'warannal@gmail.com'
PASSWORD = 'Eswari@26'
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

# if current_price <= DESIRED_PRICE:
#     message = f"Price of Gold,is now ₹{current_price}.\n Buy Now!"
#     connection = smtplib.SMTP('smtp.gmail.com')
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs='vigneshtnv@outlook.com',
#         msg=f'Subject:Price Drop Alert!\n\n{message}'.encode('utf-8')
#     )
#     connection.close()