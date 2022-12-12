import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt


st.set_page_config(layout = "wide")
air = pd.read_csv('AIR_EMISSIONS2017 (ENVIRONMENT.AIR_EMISSIONS2017) (ENVIRONMENT)_AIR_EMISSIONS2017.csv')
st.header('Air Emissions Atlas')



page = st.sidebar.selectbox('Select a page',
  ['Introduction','Air Pollution & Causes'])


if page == 'Introduction':
    st.write('Air pollution is one of the many big problems in the world. There are number of types and causes of Air Pollution created by the human race and by nature as shown in the images below. Its the release of pollutants into the air, which are hazardous to human health and the planet. The majority of air pollution comes from energy use and production. Such as burning fossil fuels, which releases gases and chemicals into the air. To take a look at the average value of air pollutants and the causes, go to the next page.')
    st.write('These are some of the types of air pollutants presented on the next page.')
    st.image("There-are-four-main-types-of-air-pollution-sources-including-natural-area-stationary.png")
    st.write('These are some of the causes of air pollutants presented on the next page.')
    st.image("Sources_Graphic_Huge.jpg")
    st.write('This is a dataset of air pollutants and causes in countries from 1990 to 2018.')
    st.dataframe(air)

    
else:
    contlist = air['Country Name'].unique()
    country = st.selectbox("Select a Country:",contlist)


    st.write('This line chart displays the average values of seven common types of Air Pollution from 1990 to 2018 in several countries. These types of pollution include Carbon Monoxide, Ammonia(NH3), Nitrogen Oxides, Non-Methane Volatile Organic Compounds, Particulates Pm10 and Pm2.5, and Sulpher Oxides. You can isolate which pollutants you want to focus on on the line chart.')

    df = air.groupby(['Date','Pollutant Name','Country Name'])['Value'].mean().reset_index(name='Value')
    df['Date'] = pd.DatetimeIndex(df['Date']).year
    #st.dataframe(f)
        
    P_chart = px.line(df[df["Country Name"]==country],
     x='Date',
     y='Value',
     color ='Pollutant Name',
     title='Types of Air Pollution')
    st.plotly_chart(P_chart, use_container_width=True)


    st.write('This line chart displays the average values of Causes of Air Pollution in the same circumstance as the first line chart. The causes include types of Combustion, Mobile Sources, Agriculture, etc.')

    df1 = air.groupby(['Date','Variable Name','Country Name'])['Value'].mean().reset_index(name='Value')
    df1['Date'] = pd.DatetimeIndex(df1['Date']).year
    #st.dataframe(df1)


    v = df1[~df1['Variable Name'].isin(['Total Emissions, Index 1990 = 100', 'Total Emissions Per Unit of Gdp, Kg Per 1000 Usd',
    'Total Emissions, Index 2000 = 100', 'Total Emissions Per Capita','Total Mobile Sources','Total Stationary Sources',
    'Total Man-Made Emissions'])]

    
    V_chart = px.line(v[v["Country Name"]==country],
     x='Date',
     y='Value',
     color ='Variable Name',
     title='Causes of Air Pollution')
    st.plotly_chart(V_chart, use_container_width=True)



