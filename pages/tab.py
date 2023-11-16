import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.markdown('สวัสดี! **Streamlit**')
st.title('San Francisco Trees Tab')
st.write("""
เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')