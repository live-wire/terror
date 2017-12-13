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
# print(data)

# Checking for null values
# print(data.isnull().sum())

# For Interactive shell
# data = joblib.load('/Users/dhruv/PycharmProjects/kaggle/dataviz/data.pkl')


# CHART 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#
firstBarChart = data[['Year','Country']].groupby(['Year']).agg(['count'])
# [["1970",651],["1971",470],["1972",496],["1973",473],["1974",580],["1975",740],["1976",923],["1977",1319],["1978",1526],["1979",2661],["1980",2662],["1981",2585],["1982",2545],["1983",2870],["1984",3495],["1985",2915],["1986",2860],["1987",3184],["1988",3720],["1989",4323],["1990",3887],["1991",4683],["1992",5073],["1994",3458],["1995",3081],["1996",3056],["1997",3200],["1998",933],["1999",1395],["2000",1813],["2001",1907],["2002",1332],["2003",1262],["2004",1162],["2005",2009],["2006",2749],["2007",3241],["2008",4803],["2009",4719],["2010",4822],["2011",5071],["2012",8500],["2013",11996],["2014",16860],["2015",14852],["2016",13488]]
# create a 2d array from this for plotting the incidents graph
# CHART 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# CHART 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ----COMMENTING HEAVY OPERATION------
#
#
# casualties = [{'key':'Killed','values':[]},{'key':'Wounded','values':[]}]
# countrykilledsums = {}
# countrywoundedsums = {}
# countrycasualitiessums = {}
#
# for index,row in data[['Country','Killed','Wounded','casualities']].iterrows():
#     if row['Country'] in countrykilledsums:
#         countrykilledsums[row['Country']] = countrykilledsums[row['Country']] + row['Killed']
#     else:
#         countrykilledsums[row['Country']] = row['Killed']
#     if row['Country'] in countrywoundedsums:
#         countrywoundedsums[row['Country']] = countrywoundedsums[row['Country']] + row['Wounded']
#     else:
#         countrywoundedsums[row['Country']] = row['Wounded']
#     if row['Country'] in countrycasualitiessums:
#         countrycasualitiessums[row['Country']] = countrycasualitiessums[row['Country']] + row['casualities']
#     else:
#         countrycasualitiessums[row['Country']] = row['casualities']
#
# top15 = [];
# for i in range(15):
#     max = 0
#     keymax = ""
#     temp = {}
#     for key in countrycasualitiessums:
#         if countrycasualitiessums[key]>max:
#             max = countrycasualitiessums[key]
#             keymax = key
#     temp[keymax] = max
#     del countrycasualitiessums[keymax]
#     top15.append(temp)
#
# for item in top15:
#     key = ''
#     for k in item:
#         key = k
#     tempkilled = {}
#     tempkilled['label'] = key
#     tempkilled['value'] = -countrykilledsums[key]
#     casualties[0]['values'].append(tempkilled)
#     tempwounded = {}
#     tempwounded['label'] = key
#     tempwounded['value'] = countrywoundedsums[key]
#     casualties[1]['values'].append(tempwounded)
# print(json.dumps(casualties))
#  USE this dump of causalities for plotting the 3rd graph
#
#
# ----COMMENTING HEAVY OPERATION------
#
# CHART 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# CHART 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# weapon_sums = {}
# for weapon in data['Weapon_type']:
#     if weapon in weapon_sums:
#         weapon_sums[weapon] = weapon_sums[weapon]+1
#     else:
#         weapon_sums[weapon] = 1
# print(weapon_sums)
# Use weapon_sums for the weapons bubble chart

# CHART 3 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# CHART 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# chart4data = {"name": "flare","description": "flare","children": []}
# countries = {}
# countrysums = {}
# for index,row in data[['city','Country']].iterrows():
#     if row['Country'] in countries:
#         if row['city'] in countries[row['Country']]['cities']:
#             countries[row['Country']]['cities'][row['city']]['size'] =  countries[row['Country']]['cities'][row['city']]['size'] + 1
#         else:
#             temp = {"name":row['city'],"description":"city","size":1}
#             countries[row['Country']]['cities'][row['city']] = temp
#     else:
#         temp = {"name":row['Country'],"description":"country","cities":{}}
#         countries[row['Country']] = temp
#
#     if row['Country'] in countrysums:
#         countrysums[row['Country']] = countrysums[row['Country']]+1
#     else:
#         countrysums[row['Country']] = 1
# top15countries = []
# for i in range(15):
#     max = 0
#     keymax = ""
#     temp = {}
#     for key in countrysums:
#         if countrysums[key]>max:
#             max = countrysums[key]
#             keymax = key
#     temp[keymax] = max
#     del countrysums[keymax]
#     top15countries.append(keymax)
# for key in countries:
#     if key in top15countries:
#
#         top5cities = []
#         obj = dict(countries[key]['cities'])
#         for i in range(5):
#             if obj == {}:
#                 break
#             max = 0
#             keymax = ""
#             for city in obj:
#                 if obj[city]['size'] > max:
#                     max = obj[city]['size']
#                     keymax = city
#             top5cities.append(obj[keymax])
#             del obj[keymax]
#         others = {"name":"Other cities","description":"city","size":0}
#         if obj == {}:
#             pass
#         else:
#             for city in obj:
#                 others['size'] = others['size'] + obj[city]['size']
#             top5cities.append(others)
#         temp = {"name":countries[key]['name'],"description":countries[key]['description']}
#         temparr = []
#         for i in top5cities:
#             temparr.append(i)
#         temp['children'] = temparr
#         chart4data['children'].append(temp)
# f = open('chart4.json','w')
# f.write(json.dumps(chart4data))
# f.close()
# print(json.dumps(chart4data))
# CHART 4 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# CHART 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# dropping rows that don't have latitude longitude data

try:
    xoxo = joblib.load('dumpchart5.pkl')
    f = open('d3/chart5/bubble_data.js', 'w')
    f.write("var bubble_data_global = " + str(xoxo['solo_data']) + ";")
    f.close()
except:
    latlongdata = data[data["latitude"]==data["latitude"]]

    # getting the top 15 terrorist groups based on number of incidents
    x = latlongdata.groupby('Group')['Region'].nunique()
    top50groups = x.sort_values(axis=0,ascending=False).head(15)
    groupdata= {}
    bubble_data = []
    solo_data = {}

    for index,row in latlongdata[['latitude','longitude','AttackType','Group','Year','casualities']].iterrows():
        if row['Group'] in top50groups.keys():
            temp = {}
            temp['latitude'] = row['latitude']
            temp['longitude'] = row['longitude']
            temp['type'] = row['AttackType']

            calc = (float(row['casualities'])/float(500))*12
            temp['radius'] = 8 + calc

            if 'Armed' in row['AttackType']:
                temp['fillKey'] = 'ONE'
            elif 'Bombing' in row['AttackType']:
                temp['fillKey'] = 'TWO'
            elif 'Unarmed' in row['AttackType']:
                temp['fillKey'] = 'SIX'
            elif 'Unknown' in row['AttackType']:
                temp['fillKey'] = 'FIVE'
            elif 'Hostage' in row['AttackType']:
                temp['fillKey'] = 'FOUR'
            else:
                temp['fillKey'] = 'THREE'

            temp['y'] = row['Year']
            # temp['Group'] = row['Group']
            bubble_data.append(temp)
            if row['Group'] in solo_data:
                solo_data[row['Group']].append(temp)
            else:
                solo_data[row['Group']] = []
                solo_data[row['Group']].append(temp)
            if row['Group'] in groupdata:
                if row['AttackType'] in groupdata[row['Group']]:
                    groupdata[row['Group']][row['AttackType']] = groupdata[row['Group']][row['AttackType']]+1
                else:
                    groupdata[row['Group']][row['AttackType']] = 1
            else:
                groupdata[row['Group']] = {}
                groupdata[row['Group']][row['AttackType']] = 1
    print(top50groups.keys())
    print(solo_data)

    dumpchart5 = {'solo_data':solo_data,'groups':top50groups.keys()}
    joblib.dump(dumpchart5,'dumpchart5.pkl');


# CHART 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# CHART 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# CHART 6 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# CHART 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# CHART 7 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

