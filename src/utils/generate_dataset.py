import os
import random
from datetime import datetime, timedelta
import csv

PRODUCTS = [
    ("Keyboard", 150.0, 90.0),
    ("Mouse", 80.5, 30.0),
    ("Monitor", 900.0, 650.0),
    ("Headset", 200.0, 120.0),
    ("Webcam", 250.0, 140.0),
    ("Laptop Stand", 120.0, 60.0),
    ("USB Hub", 70.0, 25.0),
    ("SSD 1TB", 450.0, 320.0),
]


def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))


def main(rows: int = 10000, out_path: str = "data/raw/vendas.csv") -> None:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    start = datetime(2025, 1, 1)
    end = datetime(2026, 1, 1)

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "order_id",
                "order_date",
                "customer_id",
                "product",
                "qty",
                "unit_price",
                "cost",
                "channel",
                "city",
            ]
        )

        for i in range(1, rows + 1):
            order_id = 100000 + i
            dt = random_date(start, end).strftime("%Y-%m-%d %H:%M:%S")
            customer_id = f"C{random.randint(1, 5000):05d}"

            product, base_price, base_cost = random.choice(PRODUCTS)
            qty = random.randint(1, 5)

            # variação de preço/custo para ficar realista
            unit_price = round(base_price * random.uniform(0.9, 1.1), 2)
            cost = round(base_cost * random.uniform(0.9, 1.1), 2)

            channel = random.choice(["online", "store", "marketplace"])
            city = random.choice(
                [
                    "Fortaleza",
                    "São Paulo",
                    "Rio de Janeiro",
                    "Curitiba",
                    "Recife",
                    "Salvador",
                    "Brasília",
                    "Cuiaba",
                    "Goiania",
                ]
            )

            writer.writerow(
                [
                    order_id,
                    dt,
                    customer_id,
                    product,
                    qty,
                    unit_price,
                    cost,
                    channel,
                    city,
                ]
            )

    print(f"Arquivo gerado em: {out_path} ({rows} linhas)")


if __name__ == "__main__":
    main()
