import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("CBR_API_URL")

def fetch_currency_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

def save_to_csv(data: dict, filename: str = "../raw_data/raw_currency_rates.csv"):
    df = pd.DataFrame.from_dict(data['Valute'], orient='index')
    df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.to_csv(filename, mode="a", header=not os.path.exists(filename), index=False)
    print(f"Данные сохранены в {filename}")

if __name__ == "__main__":
    currency_data = fetch_currency_rates()
    if currency_data:
        save_to_csv(currency_data)