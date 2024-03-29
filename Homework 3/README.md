# Homework 3: Plotly Charts

This repository contains the materials and resources needed to complete homework assignment focused on creating interactive visualizations using Plotly.

In this assignment, we'll be dealing with the population data of Bangkok, Thailand, focusing on each district within the city. Through the use of Plotly charts, we'll visualize various aspects of the population data, such as total population counts, population density, etc. Plotly's interactive features will allow us to explore the data dynamically, enabling us to identify trends, outliers, and patterns that may not be apparent from static representations.

## Data Source

There are 3 dataset used in this homework:
1. [Official statistics registration systems](https://stat.bora.dopa.go.th/stat/statnew/statMONTH/statmonth/#/displayData): Population in Bangkok as of January 2024
- Columns used: AMPHOE_E, LAT, LONG
2. [Open Government Data of Thailand](https://data.go.th/dataset/item_c6d42e1b-3219-47e1-b6b7-dfe914f27910): Latitude and Longitude of each Sub-District
- Columns used: District, lat, long
3. [E-Report Energey](https://e-report.energy.go.th/area/Bangkok.htm): Area of each District
- Columns used: District, Area (sq. km)

## Visualization
**1. Understanding Population in each District**
![district_population](https://github.com/prattapong/DADS5001/assets/124485030/9ee7b812-36ad-4714-b824-ce12a6c0cf69)
- Title: Number of Population in Bangkok by District
- Chart Type: Scatter Mapbox
- Reason for Chart Selection: Scatter Mapbox provides immediate context to your data by showing the geographic distribution of population data across different districts in Bangkok. Users can easily identify clusters, trends, or outliers based on the spatial arrangement of data points.
- Description: In the scatter map visualization above, it is obvious that population density in central districts is notably lower compared to their surrounding districts. However, some districts, such as Bangbon and Taweewattana, exhibit a relatively small number of population.
![top_5](https://github.com/prattapong/DADS5001/assets/124485030/f7766c8d-b266-430b-a0a0-0e13d01e5ff5)
- Title: Top 5 Districts by Population
- Chart Type: Horizontal Bar Chart
- Reason for Chart Selection: Horizontal bar charts make it easy to compare the population sizes of different districts. The horizontal orientation of the bars naturally arranges the districts in a ranked order from top to bottom which make the ranking clear.
- Description: Top 5 districts have more than 180,000 people in each district. Khlongsamwa is the district which has the most people leaving
![lowest_5](https://github.com/prattapong/DADS5001/assets/124485030/3ba3a5fa-0863-4762-aed6-0fa750ad7f4d)
- Title: Lowest 5 Districts by Population
- Chart Type: Horizontal Bar Chart
- Reason for Chart Selection: Like with the top 5 districts, using a horizontal bar chart allows for easy comparison of the population sizes of the lowest 5 districts. Viewers can quickly see the relative magnitudes of population for each district. When comparing the lowest 5 districts with the top 5, using horizontal bar charts allows for easy visual contrast. The orientation of the bars and the scaling of axis make it immediately clear which districts have the smallest populations compared to the largest populations.
- Description: Lowest 5 districts have people living less than 45,000 people. Sampanthawong has the least people living with a number of 19,451 which is more than 10 times less than the most people living district (Khlongsamwa).

**2. Male proportion in each district**
![male_ratio](https://github.com/prattapong/DADS5001/assets/124485030/1b3f4482-e7a1-4f3f-860d-2ae0a0026008)
- Title: Male Ratio in each District
- Chart Type: Scatter Mapbox
- Reason for Chart Selection: Scatter Mapbox provides immediate context to data by showing the geographic distribution of male ratio across different districts in Bangkok. Viewers can easily identify patterns or clusters of high or low male ratios in specific areas of the city.
- Description: There is only one district which is Dusit that has more men than women

**3. Understanding the density of population per area of each district**
![population_density](https://github.com/prattapong/DADS5001/assets/124485030/c7ecd248-210d-4271-9fcb-5f165c3d1cad)
- Title: Male Ratio in each District
- Chart Type: Scatter Mapbox
- Reason for Chart Selection: In Scatter Mapbox, using color to represent population density allows for quick and intuitive interpretation of the data. High-density areas are represented with red, while low-density areas are represented with blue. This color setting allows viewers to identify areas of high and low population density at a glance. Not only population density, but size of scatter also allows viewers to sea the sizing of each district to understand how crowded of each area.
- Description: Pom Prap Sattruphai and Samphanthawong rank among the five districts with the lowest population counts. With their small geographical areas, only around 1 to 2 square kilometers each, these districts are characterized by high population density, making them among the most densely populated areas in the region.
