import requests
import asyncio
from databases import Database

DATABASE_URL = "mysql://root:Sairam0704*@localhost/streamlytics"

database = Database(DATABASE_URL)

async def fetch_and_store_data():
    response = requests.get('uu0urfqge7gu0icqi3j2rk61ouj2db2gntac7nf7a9p70mnbhca3o')
    data = response.json()

    await database.connect()
    for data_point in data:
        query = f"INSERT INTO data (timestamp, value) VALUES ('{data_point['timestamp']}', {data_point['value']})"
        await database.execute(query)
    await database.disconnect()

if __name__ == "__main__":
    asyncio.run(fetch_and_store_data())
