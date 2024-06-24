import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


df = pd.read_csv('world_population.csv',index_col=False)

st.markdown("<h1>Data Overview</h1>",unsafe_allow_html=True)
st.write(df.head())



st.markdown("<h1>Descriptive Statistics</h1>",unsafe_allow_html=True)
st.write(df.describe())

st.markdown("<h1>Top 10 Countries with Highest Population 2022</h1>",unsafe_allow_html=True)
st.write(df.sort_values(by='2022 Population', ascending=False)[['Country','Continent','2022 Population']].head(10))

st.markdown("<h1>Continent-wise Population Data</h1>",unsafe_allow_html=True)
st.write(df.groupby('Continent').describe())

df_conti = df.groupby('Continent')[['2022 Population']].mean().sort_values('2022 Population',ascending=False)
st.markdown("<h1>Population Distribution : 2022</h1>",unsafe_allow_html=True)
labels = ["Asia","South America","Africa","Europe","North America","Oceania"]
fig,ax = plt.subplots()
ax.pie(df_conti['2022 Population'],labels=labels)
st.pyplot(fig)


data = df.sort_values(by = '2022 Population',ascending=False)[['Country','2022 Population']].head(10)
x = data['Country']
y = data['2022 Population']
#st.write(data)
#st.bar_chart(x=data.Country,y=data['2022 Population'])
st.markdown("<h1>Continent-wise Population : 2022</h1>",unsafe_allow_html=True)
country = df.groupby(by='Continent')['2022 Population'].sum()

#st.markdown("<h1>Continent-wise Population Data</h1>",unsafe_allow_html=True)
st.bar_chart(country)
country = df.groupby(by='Country')['2022 Population'].sum()

st.markdown("<h1>Country-wise Population Data: 2022</h1>",unsafe_allow_html=True)

st.bar_chart(country)

st.markdown("<h1>Continent-wise Area Distribution</h1>",unsafe_allow_html=True)
area = df.groupby(by='Continent')['Area (km²)'].sum()
st.bar_chart(area)

# fig,ax = plt.subplots()
# st.write(df_conti.keys())
# ax.pie(area['Area (km²)'],labels=area.Country)
# st.pyplot(fig)
