# This is the final assignment of Data Visualization course @coursera.org part2

#import libs
import pandas
import numpy
import matplotlib.pyplot as plt

# II. Choropleth map
# II.1. read_csv

CrimesFrame = pandas.read_csv('data\Police_Department_Incidents_-_Previous_Year__2016_.csv')
print(CrimesFrame.columns)
print(CrimesFrame[["PdDistrict", "Location"]].head())

GroupCrimes = CrimesFrame.groupby("PdDistrict").agg({"Location": "nunique"})

print(GroupCrimes.columns)
# CrimesFrame = CrimesFrame[["Neighborhood", "Count"]]
# print(CrimesFrame)

