import streamlit as st
import pandas as pd
from st_pages import Page, show_pages

st.set_page_config(layout='wide')
show_pages(
    [
        Page('app.py', 'Home', '🏚️'),
        Page('pages/tab.py', 'Tab Layout', '📖'),
        Page('pages/map.py', 'Map Layout', '🌎')
    ]
)

st.markdown('สวัสดี! **Streamlit**')
st.title('San Francisco Trees Columns')
st.write("""
เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')
# df_dbh_grouped = pd.DataFrame(
#     trees_df.groupby(['dbh']).count()['tree_id'])
# df_dbh_grouped.columns = ['tree_count']

owners = st.sidebar.multiselect(
    "Tree Owner Filter",
    trees_df['caretaker'].unique()
)

if owners:
    trees_df = trees_df[ trees_df['caretaker'].isin(owners) ]

df_dbh_grouped = pd.DataFrame(
    trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.write('Line Chart')
    st.line_chart(df_dbh_grouped)
with col2:
    st.write('Bar Chart')
    st.bar_chart(df_dbh_grouped)
with col3:
    st.write('Area Chart')
    st.area_chart(df_dbh_grouped)

st.caption('กราฟ แสดงจำนวนต้นไม้ จัดกลุ่มตามเส้นผ่าศูนย์กลาง')
st.title('แปลผล')
st.write("""
ส่วนใหญ่ของต้นไม้ใน San Francisco มีเส้นผ่านศูนย์กลาง 3' (2,721 ต้น)
""")