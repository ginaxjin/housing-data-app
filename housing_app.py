import streamlit as st
import pandas as pd
import numpy as np

def my_select_callback():
    select_event = st.session_state.on_select_callback
    if select_event:
        st.info(
            f"Selected {select_event.row} (row) / {select_event.column} (column) with value: {select_event.value}"
        )

st.title('Housing Charts :house:')

sales_cnt = pd.read_csv('housing_data/sales_count_month.csv')
median_price_cut = pd.read_csv('housing_data/med_price_cut_perc_week.csv')
perc_price_cnt = pd.read_csv('housing_data/perc_price_cut_week.csv')

if st.checkbox('Show sales count raw data'):
    st.subheader('Sales Count Raw Data')
    st.write(sales_cnt)

if st.checkbox('Show median price cut raw data'):
    st.subheader('Median Price Cut Raw Data')
    st.write(median_price_cut)

if st.checkbox('Show percentage price cut raw data'):
    st.subheader('Percentage Price Cut Raw Data')
    st.write(perc_price_cnt)

all_metros = sales_cnt['RegionName']
metros = st.multiselect("Choose metro area:", all_metros)

chart_source = sales_cnt[sales_cnt.RegionName.isin(metros)]
# st.dataframe(chart_source, on_select=my_select_callback, key="on_select_callback")
st.write(chart_source)

df = pd.DataFrame(chart_source)
df_transposed = df.loc[:, ~df.columns.isin(['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'])].transpose()

df_transposed.columns = df['RegionName'].values.tolist()
st.line_chart(df_transposed)
