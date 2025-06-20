import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('all_df.csv')
st.set_page_config(page_title='My Sale Dashboard',page_icon=':bar_chart:',layout='wide')
st.sidebar.header('Please filter here')
pchoice = st.sidebar.multiselect(
    'Select Product',
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5]
)
cchoice = st.sidebar.multiselect(
    'Select City',
    options = df['City'].unique(),
    default = df['City'].unique()[:5]
)
mchoice = st.sidebar.multiselect(
    'Select Month',
    options = df['Month'].unique(),
    default = df['Month'].unique()[:5]
)
st.title(':bar_chart: Sales Dashboard for 2019')
ourtotal = df['Total'].sum()
no_of_product = df['Product'].nunique()
left,right = st.columns(2)
with left:
    st.subheader('Total Sale')
    st.subheader(f'US $ {ourtotal}')
with right:
    st.subheader('No. of Product')
    st.subheader(f'{no_of_product}')
df_select = df.query('Product == @pchoice and City == @cchoice and Month == @mchoice')
pp = df_select.groupby('Product')['Total'].sum().sort_values()
fig_by_Product = px.bar(
    pp, 
    x=pp.values, 
    y= pp.index,
    title='Total Sale by Product'
)
mm = df_select.groupby('Month')['Total'].sum().sort_values()
fig_by_Month = px.bar(
    mm, 
    x=mm.values, 
    y= mm.index,
    title='Total Sale by Month'
)
fig_pie = px.pie(
    df_select, 
    values='Total', 
    names='City', 
    title='Total Sale by Month')
a,b,c = st.columns(3)
a.plotly_chart(fig_by_Product,use_container_width = True)
b.plotly_chart(fig_pie,use_container_width = True)
c.plotly_chart(fig_by_Month,use_container_width = True)
fig_line = px.line(
    mm, 
    x=mm.values, 
    y=mm.index, 
    title='Total Sale by Month'
)
fig_scatter = px.scatter(
    df_select, 
    x='Total', 
    y='QuantityOrdered', 
    title='Total Sale Quantity'
)
d,e = st.columns(2)
d.plotly_chart(fig_line,use_container_width = True)
e.plotly_chart(fig_scatter,use_container_width = True)