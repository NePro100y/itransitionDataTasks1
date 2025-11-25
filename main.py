import re
import json
import psycopg2

raw = open("task1_d.json", "r", encoding="utf-8").read()
raw = re.sub(r':(\w+)\s*=>', r'"\1":', raw)
data = json.loads(raw)

conn = psycopg2.connect(
    dbname="itransitionDataTask1",
    user="postgres",
    password="123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
for book in data:
    cur.execute("""INSERT INTO books (id, title, author, genre, publisher, year, price_value, price_currency)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
        (book["id"], book["title"], book["author"], book["genre"], book["publisher"],
        book["year"], book["price"][1:], book["price"][0]))

conn.commit()