from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database
import sqlalchemy

DATABASE_URL = "mysql://root:Sairam0704*@localhost/streamlytics"

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

@app.post("/data")
async def add_data(data_point: DataPoint):
    query = data.insert().values(timestamp=data_point.timestamp, value=data_point.value)
    await database.execute(query)
    return {"message": "Data added successfully"}

@app.get("/data")
async def get_data():
    query = data.select()
    return await database.fetch_all(query)
