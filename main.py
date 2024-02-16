from bs4 import BeautifulSoup
import requests

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8"
}

telegram_api = "https://api.telegram.org/bot6547512859:AAH-OHxQmXS_o_Ivslu8s6KkDaxMJlI_jsk/sendMessage"

url = "https://eshop-prices.com/games/1063-dead-cells?currency=TRY"
html_content = requests.get(url, headers=header)

soup = BeautifulSoup(html_content.content, 'html.parser')

prices_table = soup.find('table', class_='prices-table')

div_text = None

div_tag = soup.find('div', class_='discounted')

if div_tag:
    div_text = ''.join(str(item) for item in div_tag.contents if not getattr(item, 'name', None) == 'del')
    div_text = BeautifulSoup(div_text, 'html.parser').get_text()
    print(f"Dead cells price is: {div_text}")
    parameters = {
        "chat_id": 6641479687,
        "text": f"Dead cells price is: {div_text}"
    }
    resp = requests.get(telegram_api, data=parameters)

elif prices_table:
    price_elements = prices_table.find_all('td', class_='price-value')
    if price_elements:
        desired_price = price_elements[0].get_text()
        print(f"Dead cells price is: {desired_price}")
        parameters = {
            "chat_id": 6641479687,
            "text": f"Dead cells price is: {desired_price}"
        }
        resp = requests.get(telegram_api, data=parameters)
    else:
        print("Price not found.")
else:
    print("Table not found.")
