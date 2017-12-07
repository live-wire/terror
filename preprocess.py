import pandas as pd
from sklearn.externals import joblib
import json
from random import shuffle

try:
    data = joblib.load('data.pkl')
except:
    data = pd.read_csv('data.csv', encoding='ISO-8859-1')
    data.rename(
        columns={'iyear': 'Year', 'imonth': 'Month', 'iday': 'Day', 'country_txt': 'Country', 'region_txt': 'Region',
                 'attacktype1_txt': 'AttackType', 'target1': 'Target', 'nkill': 'Killed', 'nwound': 'Wounded',
                 'summary': 'Summary', 'gname': 'Group', 'targtype1_txt': 'Target_type', 'weaptype1_txt': 'Weapon_type',
                 'motive': 'Motive'}, inplace=True)
    data = data[['Year', 'Month', 'Day', 'Country', 'Region', 'city', 'latitude', 'longitude', 'AttackType', 'Killed',
                 'Wounded', 'Target', 'Summary', 'Group', 'Target_type', 'Weapon_type', 'Motive']]
    data['Killed'].fillna(0, inplace=True)
    data['Wounded'].fillna(0, inplace=True)
    # Renaming Columns, Dimensionality Reduction (Too many features initially, Renaming some features and keeping only some features for use)
    data['casualities'] = data['Killed'] + data['Wounded']
    joblib.dump(data,'data.pkl')

# Checking for null values
# print(data.isnull().sum())

# For Interactive shell
# data = joblib.load('/Users/dhruv/PycharmProjects/kaggle/dataviz/data.pkl')


# CHART1
firstBarChart = data[['Year','Country']].groupby(['Year']).agg(['count'])
# [["1970",651],["1971",470],["1972",496],["1973",473],["1974",580],["1975",740],["1976",923],["1977",1319],["1978",1526],["1979",2661],["1980",2662],["1981",2585],["1982",2545],["1983",2870],["1984",3495],["1985",2915],["1986",2860],["1987",3184],["1988",3720],["1989",4323],["1990",3887],["1991",4683],["1992",5073],["1994",3458],["1995",3081],["1996",3056],["1997",3200],["1998",933],["1999",1395],["2000",1813],["2001",1907],["2002",1332],["2003",1262],["2004",1162],["2005",2009],["2006",2749],["2007",3241],["2008",4803],["2009",4719],["2010",4822],["2011",5071],["2012",8500],["2013",11996],["2014",16860],["2015",14852],["2016",13488]]
# create a 2d array from this for plotting the incidents graph


# CHART2
casualties = [{'key':'Killed','values':[]},{'key':'Wounded','values':[]}]
countrykilledsums = {}
countrywoundedsums = {}
countrycasualitiessums = {}

for index,row in data[['Country','Killed','Wounded','casualities']].iterrows():
    if row['Country'] in countrykilledsums:
        countrykilledsums[row['Country']] = countrykilledsums[row['Country']] + row['Killed']
    else:
        countrykilledsums[row['Country']] = row['Killed']
    if row['Country'] in countrywoundedsums:
        countrywoundedsums[row['Country']] = countrywoundedsums[row['Country']] + row['Wounded']
    else:
        countrywoundedsums[row['Country']] = row['Wounded']
    if row['Country'] in countrycasualitiessums:
        countrycasualitiessums[row['Country']] = countrycasualitiessums[row['Country']] + row['casualities']
    else:
        countrycasualitiessums[row['Country']] = row['casualities']

top15 = [];
for i in range(15):
    max = 0
    keymax = ""
    temp = {}
    for key in countrycasualitiessums:
        if countrycasualitiessums[key]>max:
            max = countrycasualitiessums[key]
            keymax = key
    temp[keymax] = max
    del countrycasualitiessums[keymax]
    top15.append(temp)

for item in top15:
    key = ''
    for k in item:
        key = k
    tempkilled = {}
    tempkilled['label'] = key
    tempkilled['value'] = -countrykilledsums[key]
    casualties[0]['values'].append(tempkilled)
    tempwounded = {}
    tempwounded['label'] = key
    tempwounded['value'] = countrywoundedsums[key]
    casualties[1]['values'].append(tempwounded)
print(json.dumps(casualties))






# CHART3
weapon_sums = {}
for weapon in data['Weapon_type']:
    if weapon in weapon_sums:
        weapon_sums[weapon] = weapon_sums[weapon]+1
    else:
        weapon_sums[weapon] = 1
# print(weapon_sums)
# Use weapon_sums for the weapons bubble chart


