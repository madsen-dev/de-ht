import csv
import random


def generate_countries(filename="countries.csv"):
    countries = [
        "Sweden", "Norway", "Denmark", "Finland", "Iceland",
        "Germany", "France", "Spain", "Italy", "Poland"
    ]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name"])
        for idx, country in enumerate(countries, start=1):
            writer.writerow([idx, country])
    print(f"{filename} created.")


def generate_invoices(filename="invoices.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "country_id", "amount_sek"])
        
        for invoice_id in range(1, 101):
            country_id = random.randint(1, 10)
            amount_sek = random.randint(100, 10000)
            writer.writerow([invoice_id, country_id, amount_sek])
    print(f"{filename} created.")


if __name__ == "__main__":
    generate_countries()
    generate_invoices()
