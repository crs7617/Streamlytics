import requests
import asyncio
from databases import Database
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")

if not DATABASE_URL or not API_KEY:
    raise ValueError("DATABASE_URL and API_KEY environment variables must be set")

database = Database(DATABASE_URL)

async def fetch_and_store_data():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get('https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent', headers=headers)
    response.raise_for_status()
    data = response.json()

    await database.connect()
    try:
        query = "INSERT INTO data (timestamp, value) VALUES (:timestamp, :value)"
        values = [{"timestamp": data_point['timestamp'], "value": data_point['value']} for data_point in data]
        await database.execute_many(query, values)
    finally:
        await database.disconnect()

if __name__ == "__main__":
    asyncio.run(fetch_and_store_data())