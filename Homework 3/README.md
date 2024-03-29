# Homework 3: Plotly Charts

This repository contains the materials and resources needed to complete homework assignment focused on creating interactive visualizations using Plotly.

In this assignment, we'll be dealing with the population data of Bangkok, Thailand, focusing on each district within the city. Through the use of Plotly charts, we'll visualize various aspects of the population data, such as total population counts, population density, etc. Plotly's interactive features will allow us to explore the data dynamically, enabling us to identify trends, outliers, and patterns that may not be apparent from static representations.

## Data Source

There are 3 dataset used in this homework:
1. [Official statistics registration systems](https://stat.bora.dopa.go.th/stat/statnew/statMONTH/statmonth/#/displayData): Population in Bangkok as of January 2024 
- <ins>Columns used</ins>: AMPHOE_E, LAT, LONG
- <ins>Data Gathering Method</ins>: Download [CSV](https://github.com/prattapong/DADS5001/blob/main/Homework%203/data/bangkok_population.csv) from website
2. [Open Government Data of Thailand](https://data.go.th/dataset/item_c6d42e1b-3219-47e1-b6b7-dfe914f27910): Latitude and Longitude of each Sub-District
- <ins>Columns used</ins>: District, lat, long
- <ins>Data Gathering Method</ins>: Download [CSV](https://github.com/prattapong/DADS5001/blob/main/Homework%203/data/tambon.csv) from website
3. [E-Report Energey](https://e-report.energy.go.th/area/Bangkok.htm): Area of each District
- <ins>Columns used</ins>: District, Area (sq. km)
- <ins>Data Gathering Method</ins>: Web Scraping with [BeautifulSoup](https://github.com/prattapong/DADS5001/blob/main/Homework%203/code/homework_3.ipynb)

## Visualization
**1. Understanding Population in each District**
![district_population](https://github.com/prattapong/DADS5001/assets/124485030/9ee7b812-36ad-4714-b824-ce12a6c0cf69)
- <ins>Title</ins>: Number of Population in Bangkok by District
- <ins>Chart Type</ins>: Scatter Mapbox
- <ins>Reason for Chart Selection</ins>: Scatter Mapbox provides immediate context to your data by showing the geographic distribution of population data across different districts in Bangkok. Users can easily identify clusters, trends, or outliers based on the spatial arrangement of data points.
- <ins>Description</ins>: In the scatter map visualization above, it is obvious that population density in central districts is notably lower compared to their surrounding districts. However, some districts, such as Bangbon and Taweewattana, exhibit a relatively small number of population.
![top_5](https://github.com/prattapong/DADS5001/assets/124485030/f7766c8d-b266-430b-a0a0-0e13d01e5ff5)
- <ins>Title</ins>: Top 5 Districts by Population
- <ins>Chart Type</ins>: Horizontal Bar Chart
- <ins>Reason for Chart Selection</ins>: Horizontal bar charts make it easy to compare the population sizes of different districts. The horizontal orientation of the bars naturally arranges the districts in a ranked order from top to bottom which make the ranking clear.
- <ins>Description</ins>: Top 5 districts have more than 180,000 people in each district. Khlongsamwa is the district which has the most people leaving
![lowest_5](https://github.com/prattapong/DADS5001/assets/124485030/3ba3a5fa-0863-4762-aed6-0fa750ad7f4d)
- <ins>Title</ins>: Lowest 5 Districts by Population
- <ins>Chart Type</ins>: Horizontal Bar Chart
- <ins>Reason for Chart Selection</ins>: Like with the top 5 districts, using a horizontal bar chart allows for easy comparison of the population sizes of the lowest 5 districts. Viewers can quickly see the relative magnitudes of population for each district. When comparing the lowest 5 districts with the top 5, using horizontal bar charts allows for easy visual contrast. The orientation of the bars and the scaling of axis make it immediately clear which districts have the smallest populations compared to the largest populations.
- <ins>Description</ins>: Lowest 5 districts have people living less than 45,000 people. Sampanthawong has the least people living with a number of 19,451 which is more than 10 times less than the most people living district (Khlongsamwa).

**2. Male proportion in each district**
![male_ratio](https://github.com/prattapong/DADS5001/assets/124485030/1b3f4482-e7a1-4f3f-860d-2ae0a0026008)
- <ins>Title</ins>: Male Ratio in each District
- <ins>Chart Type</ins>: Scatter Mapbox
- <ins>Reason for Chart Selection</ins>: Scatter Mapbox provides immediate context to data by showing the geographic distribution of male ratio across different districts in Bangkok. Viewers can easily identify patterns or clusters of high or low male ratios in specific areas of the city.
- <ins>Description</ins>: There is only one district which is Dusit that has more men than women

**3. Understanding the density of population per area of each district**
![population_density](https://github.com/prattapong/DADS5001/assets/124485030/c7ecd248-210d-4271-9fcb-5f165c3d1cad)
- <ins>Title</ins>: Population per sq. km in Bangkok by District
- <ins>Chart Type</ins>: Scatter Mapbox
- <ins>Reason for Chart Selection</ins>: In Scatter Mapbox, using color to represent population density allows for quick and intuitive interpretation of the data. High-density areas are represented with red, while low-density areas are represented with blue. This color setting allows viewers to identify areas of high and low population density at a glance. Not only population density, but size of scatter also allows viewers to sea the sizing of each district to understand how crowded of each area.
- <ins>Description</ins>: Pom Prap Sattruphai and Samphanthawong rank among the five districts with the lowest population counts. With their small geographical areas, only around 1 to 2 square kilometers each, these districts are characterized by high population density, making them among the most densely populated areas in the region.
