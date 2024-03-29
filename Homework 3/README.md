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
1. **Understanding Population in each District**
![district_population](https://github.com/prattapong/DADS5001/assets/124485030/9ee7b812-36ad-4714-b824-ce12a6c0cf69)
- Title: Number of Population in Bangkok by District
- Chart Type: Scatter Mapbox
- Reason for Chart Selection: Scatter Mapbox provides immediate context to your data by showing the geographic distribution of population data across different districts in Bangkok. Users can easily identify clusters, trends, or outliers based on the spatial arrangement of data points.
- Description: In the scatter map visualization above, it is obvious that population density in central districts is notably lower compared to their surrounding districts. However, some districts, such as Bangbon and Taweewattana, exhibit a relatively small number of population.
![top_5](https://github.com/prattapong/DADS5001/assets/124485030/f7766c8d-b266-430b-a0a0-0e13d01e5ff5)
- Title: Top 5 Districts by Population
- Chart Type: Horizontal Bar Chart

