import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.markdown('สวัสดี! **Streamlit**')
st.title('San Francisco Trees Map')
st.write("""
เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)