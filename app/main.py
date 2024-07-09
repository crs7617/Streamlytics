from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from databases import Database
import sqlalchemy
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

data = sqlalchemy.Table(
    "data",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("timestamp", sqlalchemy.String),
    sqlalchemy.Column("value", sqlalchemy.Float),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

class DataPoint(BaseModel):
    timestamp: str
    value: float

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

async def get_db():
    async with database.connection() as connection:
        yield connection

@app.post("/data")
async def add_data(data_point: DataPoint, db: Database = Depends(get_db)):
    query = data.insert().values(timestamp=data_point.timestamp, value=data_point.value)
    try:
        await db.execute(query)
        return {"message": "Data added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data")
async def get_data(db: Database = Depends(get_db)):
    query = data.select()
    try:
        result = await db.fetch_all(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))