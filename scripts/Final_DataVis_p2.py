# This is the final assignment of Data Visualization course @coursera.org part2

#import libs
import folium
import pandas
import numpy
import matplotlib.pyplot as plt

# II. Choropleth map
# II.1. read_csv

CrimesFrame = pandas.read_csv(
    'E:\projects\DS_stud\data\Police_Department_Incidents_-_Previous_Year__2016_.csv')
print(CrimesFrame.columns)

df_groupby = CrimesFrame.groupby("PdDistrict")
GroupCrimes = pandas.DataFrame(columns = ['Neighborhood', 'Count'])

for dist, group in df_groupby:
   # print(dist, len(group))
    GroupCrimes = GroupCrimes.append({'Neighborhood': dist, 'Count': len(group)}, ignore_index=True)

GroupCrimes.sort_values(['Count'], ascending = False, inplace = True, axis = 0)
GroupCrimes.reset_index(drop = True, inplace=True)
print(GroupCrimes)

# last part (4) of Data Vizualisation "Choropleth map"


# For the map, make sure that:
# TODO it is centred around San Francisco,
# TODO you use a zoom level of 12,
# TODO you use fill_color = 'YlOrRd',
# TODO you define fill_opacity = 0.7,
# TODO you define line_opacity = 0.2, and,
# TODO you define a legend and use the default threshold scale.

SF_geo = 'E:\projects\DS_stud\data\san-francisco.geojson'
SF_map = folium.Map(location=[37.7740, -122.4313],
                    zoom_start=12)

folium.Choropleth(
    geo_data=SF_geo,
    data = GroupCrimes,
    columns = ['Neighborhood', 'Count'],
    key_on = 'feature.properties.DISTRICT',
    fill_color='YlOrRd',
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = 'Crime Rate in San Francisco').add_to(SF_map)


SF_map.save('index.html')
