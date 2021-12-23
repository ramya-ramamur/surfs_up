# surfs_up
Advanced Data Storage and Retrieval with Jupyter Notebook, SQLite and SQLAlchemy

# Overview
The purpose of this analysis is to analyze a dataset pertaining to weather conditions (temperature and precipitation data) for the months of June and December in Oahu, in order to determine ifopening up a Surf n' Shake shop in Oahu, Hawaii, a surf and ice cream shop business is sustainable year-round.

# Resources
* Data Source: 
  Weather Database: data is stored in the SQLite database, and SQLAlchemy was used to connect and generate queries to pull the necessary information needed for the analysis.
* Software: Python 3.8.8, Pandas Dataframe, Matplotlib, Jupyter Notebook 6.3.0, SQLite, SQLAlchemy, Flask

# Results
### Initial Analysis 
Initial analysis for one year revealed the that a vast majority of the observations were over 67 degrees. If you count up the bins to the right of 67 degrees, you will get about 325 days where it was over 67 degrees when the temperature was observed. Precipitation data statistics gives us a summary of different statistics for the amount of precipitation in a year. We can see from the chart that some months have higher amounts of precipitation than others but the recorded levels are very low. 

![temp:prcp](https://user-images.githubusercontent.com/75961057/147171164-d7da8d83-0fdf-43d0-92e5-ba1901faf98a.png)

### June and December Temperature Analysis
1. 
Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
