# TASK: List the top 5 countries with the highest total invoice amount
import duckdb

con = duckdb.connect()

result = con.execute("""
    SELECT c.name, SUM(i.amount_sek) AS total_amount
    FROM 'invoices.csv' i
    JOIN 'countries.csv' c ON c.id = i.country_id
    GROUP BY c.name
    ORDER BY total_amount DESC
    LIMIT 5
""").fetchdf()

print(result)
