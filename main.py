#RBooth
#'AZPHX20190219DATA
# Unit 3| Assignment - Py Me Up, Charlie
#******************************************

# Assignment to modernize election data by using python to create a program which reads the raw data from a 
# csv file which totals the election results and percent of the vote each candidate received, and identify 
# the winner. These results then must be available in terminal readout and in a textfile.

#******************************************

# Start by importing dependencies
import os
# Import CSV module and CSV Dictionary Reader and Writer
import csv
from csv import DictReader
from csv import DictWriter
from collections import defaultdict

# Create empty list for csv file
cleetus_dict_reader=[]
# Create empty dictionary to record only candidate names
candis_dict = {}
# Create empty dictionaty to summarize the total number votes per candidate name
polling_summary_dict = {}
# Open election_data.csv with "read" permission
file_object = open('election_data.csv', 'r') 
# Create a CSV.DictReader (cleetus_dict_reader) object
cleetus_dict_reader = csv.DictReader(file_object, delimiter=',')
# Call cleetus_dict_reader fieldnames property to get all CSV file field names in a Python list
field_names = cleetus_dict_reader.fieldnames
# Verified >>for row in cleetus_dict_reader:
   # >>print(cleetus_dict_reader)

Count = 1
for line in open(cleetus_dict_reader).xreadlines(  ): count += 1
total_votes=count  
for line in cleetus_dict_reader:
    name_key=line[2]
    if name_key not in candis_dict:
        # insert name_key into dictionary and initialize to 0
        candis_dict[name_key]=0
    # count the name key inside dictionary
    candis_dict[name_key]+=1
    # Compute the percentages of each name key of dict_polls and insert into dict_summary
for name in candis_dict:
    polling_summary_dict[name]=((candis_dict[name]/total_votes)*100)