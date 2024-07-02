import streamlit as st
import pandas as pd
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")

def get_data():
    conn = pymysql.connect(**DATABASE_URL)
    df = pd.read_sql('SELECT * FROM data', conn)
    conn.close()
    return df

st.title("Real-Time Analytics Dashboard")

data = get_data()

st.line_chart(data.set_index('timestamp')['value'])
