
import time
import requests
from bs4 import BeautifulSoup
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_BOT_TOKEN = "xoxb-9024374351126-9024493904003-9xArLdYy9HZkS5V2WV84py77"
CHANNEL_ID = "C090QB0L230"  # напр. C06D7K31FJG

UPDATE_INTERVAL = 15  # секунд

STOCK_SYMBOLS = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA"
}

slack_client = WebClient(token=SLACK_BOT_TOKEN)

def get_stock_prices():
    prices = {}
    headers = {'User-Agent': 'Mozilla/5.0'}
    for name, symbol in STOCK_SYMBOLS.items():
        try:
            url = f"https://finviz.com/quote.ashx?t={symbol}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("table", class_="snapshot-table2")

            if not table:
                prices[name] = "❌ Таблиця не знайдена"
                continue

            rows = table.find_all("tr")
            found = False
            for row in rows:
                cells = row.find_all("td")
                for i in range(0, len(cells), 2):
                    key = cells[i].text.strip()
                    val = cells[i + 1].text.strip()
                    if key == "Price":
                        prices[name] = val
                        found = True
                        break
                if found:
                    break
            if not found:
                prices[name] = "❌ Ціна не знайдена"

        except Exception as e:
            prices[name] = f"❌ Помилка: {e}"
    return prices

def format_prices(prices):
    message = "*📊 Поточні ціни з Finviz:*\n"
    for name, price in prices.items():
        message += f"> *{name}*: ${price}\n"
    return message

def post_to_slack(text):
    try:
        slack_client.chat_postMessage(channel=CHANNEL_ID, text=text)
    except SlackApiError as e:
        print(f"❌ Slack error: {e.response['error']}")

if __name__ == "__main__":
    while True:
        prices = get_stock_prices()
        message = format_prices(prices)
        print(message)
        post_to_slack(message)
        time.sleep(UPDATE_INTERVAL)
