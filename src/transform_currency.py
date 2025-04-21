import pandas as pd
import os


def transform_data(input_path: str, output_path: str) -> None:
    try:
        df = pd.read_csv(input_path)

        df["Value"] = df["Value"].astype(float)
        df["Previous"] = df["Previous"].astype(float)

        df["Change_pct"] = round((df["Value"] - df["Previous"]) / df["Previous"] * 100, 2)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"Обработанные данные сохранены в {output_path}")

    except Exception as e:
        print(f"Ошибка при трансформации: {e}")


if __name__ == "__main__":
    transform_data(
        input_path="../raw_data/raw_currency_rates.csv",
        output_path="../processed_data/processed_rates.csv"
    )