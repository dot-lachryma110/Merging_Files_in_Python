# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:50:56 2019

@author: chris.bargman5
"""

import pandas as pd

import numpy as np

import csv

output_filename = "C:/Users/chris.bargman5/Desktop/Radio_Stations/Sacramento_Stations_merge.csv"

#import tweets for Alabama
CA_stations = pd.read_csv('C:/Users/chris.bargman5/Desktop/Radio_Stations/CA_stations.csv',encoding = 'unicode_escape')


#import geocoded list with x,y coords
Sacramento_area = pd.read_csv('C:/Users/chris.bargman5/Desktop/Radio_Stations/Sacramento_Metropolitan.csv',encoding = 'unicode_escape')

#this works!
#left and right outer join
merged = pd.merge(CA_stations, Sacramento_area,  how='outer',
                  left_on='City', right_on='City')
#merged = merged.drop('newspaper', 1)
merged.head()


#export merged csv

#this is the only way I was able to get the export to populate all the rows
merged.iloc[0:1000].to_csv(output_filename)


# Write the full results to csv using the pandas library.
# this doesn't work because it exports an infinitely long single row
#pd.DataFrame(merged).to_csv(output_filename, encoding='unicode_escape')

#STEP 2: Merge frequency data

AL_freq = pd.read_csv('C:/Users/chris.bargman5/Desktop/Geog701/projects/R_code/export_to_excel/AL_screen_occur.csv')

#this works!
#left and right outer join
merged2 = pd.merge(merged, AL_freq, how='outer',
                  left_on='screenName', right_on='screenName')

merged2.head()

output_filename2 = "C:/Users/chris.bargman5/Desktop/Geog701/projects/Excel/AL_tweet_FREQ.csv"


#this is the only way I was able to get the export to populate all the rows
merged2.iloc[0:19412].to_csv(output_filename2)

#now merge population data
AL_pops = pd.read_csv('C:/Users/chris.bargman5/Desktop/Geog701/projects/CIty_Population_Tables/State_Pops_for_Merge/AL_Pop_merge.csv')
output_filename3 = "C:/Users/chris.bargman5/Desktop/Geog701/projects/Excel/AL_tweet_FREQ_POP.csv"
merged3.iloc[0:19801].to_csv(output_filename3)

merged3 = pd.merge(merged2, AL_pops, how='outer',
                  left_on='City', right_on='City')
#merged = merged.drop('newspaper', 1)
merged.head()




