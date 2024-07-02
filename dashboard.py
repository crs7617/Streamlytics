import streamlit as st
import pandas as pd
import pymysql

DATABASE_URL = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Sairam0704*',
    'database': 'streamlytics',
}

def get_data():
    conn = pymysql.connect(**DATABASE_URL)
    df = pd.read_sql('SELECT * FROM data', conn)
    conn.close()
    return df

st.title("Real-Time Analytics Dashboard")

data = get_data()

st.line_chart(data.set_index('timestamp')['value'])
