# Final
Final 5122 Project

Air Emissions Atlas

Introduction:

My code displays the average value of Air Pollutants and causes of Air Pollution from 1990 to 2018 for a number of countries. I would like the address the amount of air pollutation and the causes throughout the world. I wish to show how the numbers are affected with each variable in each country over the years. Air pollution is one of the many big problems in the world. There are number of causes of Air Pollution created by the human race and nature as shown in the picture below. Its the release of pollutants into the air, which are hazardous to human health and the planet. Most comes from energy use and production. Such as burning fossil fuels, which releases gases and chemicals into the air.


Data/operation abstraction design:

The app is divided into two pages; an introduction and line chart page using a selectbox if else function.

On the first page I inserted an image that displays air pollution causes and a dataframe of the dataset used in the app, along with some descriptions.

On the second page, I divided Air Pollutants and Air Pollution Causes into two line charts, using the px plotly function. I also installed a selectbox that isolates a country so the user can pick the country to focus on their air pollution and causes. The first line chart displays the average values of seven common types of Air Pollution from 1990 to 2018. These types of pollution include Carbon Monoxide, Ammonia(NH3), Nitrogen Oxides, Non-Methane Volatile Organic Compounds, Particulates Pm10 and Pm2.5, and Sulpher Oxides. The user can isolate which pollutants to focus on on the line chart and drag the cursor across a line to view the exact year and average value as it increases or decreases over time. The second line chart displays the average values of Causes of Air Pollution in the same circumstance as the first line chart. The causes include types of Combustion, Mobile Sources, Agriculture, etc.

To make these line charts work I had to use a groupby function to aggregate the average of the values of the variables.

The data can be found on Snowflake.

Future Work:

In the future, I might try to add more selectbox functions so that the user can isolate exact years, air pollutants, and causes. I could try to put in a bar chart function. I also might try to install a map that responds to the year, air pollutant, and the cause.

Streamlit App:

Citation:

U.S. Department of the Interior. (n.d.). Where does air pollution come from? National Parks Service. Retrieved December 10, 2022, from https://www.nps.gov/subjects/air/sources.htm 

Mackenzie, J., &amp; Turrentine, J. (2021, June 22). Air pollution: Everything you need to know. NRDC. Retrieved December 11, 2022, from https://www.nrdc.org/stories/air-pollution-everything-you-need-know 
