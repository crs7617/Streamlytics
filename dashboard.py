import streamlit as st
import pandas as pd
import pymysql
from dotenv import load_dotenv
import os
from urllib.parse import urlparse

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

def get_db_config(url):
    parsed = urlparse(url)
    return {
        'host': parsed.hostname,
        'user': parsed.username,
        'password': parsed.password,
        'database': parsed.path[1:],
        'port': parsed.port or 3306
    }

def get_data():
    db_config = get_db_config(DATABASE_URL)
    conn = pymysql.connect(**db_config)
    try:
        df = pd.read_sql('SELECT * FROM data', conn)
        return df
    finally:
        conn.close()

st.title("Real-Time Analytics Dashboard")

data = get_data()

if not data.empty:
    st.line_chart(data.set_index('timestamp')['value'])
else:
    st.warning("No data available")