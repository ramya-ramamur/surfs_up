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

![AA397D7F-0545-4D4D-B844-81D0D95739F5_4_5005_c](https://user-images.githubusercontent.com/75961057/147172522-2dfb12e8-8f16-4b15-a2f0-8ed3dad1bbd7.jpeg)

### June and December Temperature Analysis
The client wants a temperature analysis including statistical inference for the months of June and December to compare in order to determine if the surf and ice cream shop business is sustainable year-round.

![Untitled](https://user-images.githubusercontent.com/75961057/147173320-8405db63-2743-49ed-abac-1656d4b9f996.png)

* The average recorded temperature in June is about 75°F, 4 degrees higher than the average temp in December(.71°F)
* June's standard deviation of 3.26 and December's standard deviation of 3.75 so temperature records are concentrated around both of their average temperatures. * Temperatures can reach upto 80+ degrees in both June and December which is great ice cream weather. 
* Minimum temperatures in December can go to 56 °F, ~10 degrees lower than in summer but the frequency of that is low from the December Temperature chart. 
* June and December had a 75th percentile of 77°F and 74°F, respectively, which indicates that these two seasons had relatively warm temperatures.

# Summary:
