from gettext import install
from turtle import title
import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

st.header('Air Emissions Atlas')

#import data


air = pd.read_csv('AIR_EMISSIONS2017 (ENVIRONMENT.AIR_EMISSIONS2017) (ENVIRONMENT)_AIR_EMISSIONS2017.csv')
st.dataframe(air)



st.sidebar.header("Pick two variables for the charts")
x_val = st.sidebar.selectbox("Pick your x-axis",air.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis",air.select_dtypes(include=np.number).columns.tolist())




bar = alt.Chart(air, title = f" {x_val} and {y_val} ").mark_bar(fill = 'green',color = 'green').encode(
    alt.X(x_val, title = f"{x_val}"),
    alt.Y(y_val, title = f"{y_val}"),
    tooltip=[x_val,y_val]
    )


st.altair_chart(bar, use_container_width=True)

####

#clist = air['Country Name'].unique()
#country = st.selectbox("Select a country:",clist)
#col1, col2 = st.columns(2)
#air_country = air[air['Country Name']== country]
#GDP_Chart = alt.Chart(air_country).mark_line().encode(
#    x = 'Country',
#    y = 'Scale'
#)
#col1.altair_chart(GDP_Chart, use_container_width=True)
#POP_Chart = alt.Chart(air_country).mark_line().encode(
#    x = 'Country',
#    y = 'Scale'
#)
#col2.altair_chart(POP_Chart, use_container_width=True)



# Average Causes of Air Pollution

bar = alt.Chart(air,title='Average Causes of Air Pollution').mark_bar().encode(
    x= 'Variable Name',
    y= 'Value'
)

st.altair_chart(bar, use_container_width=True)


#pollutants over time
bar = alt.Chart(air, title = 'Pollutants Over Time').mark_line().encode(
    x= 'Date',
    y= 'Pollutant'
)
st.altair_chart(bar, use_container_width=True)

#map