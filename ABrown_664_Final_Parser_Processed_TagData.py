import json
import csv
from collections import Counter

all_items = []
TopfiveTags = {}

with open('OFMD_Processed_TagData.json', 'r') as datafile:
    processed_json = json.load(datafile)

    for week in processed_json:
        StartoftheWeek = week['Week Start Date']
        print('Week Start Date')
        print('\t', week['Week Start Date'])
        EndoftheWeek = week['Week Start Date']
        print('Week End Date')
        print('\t', week['Week End Date'])
        NumberofTags = week['Number of Tags']
        print('Number of Tags')
        print('\t', week['Number of Tags'])

        TopfiveTags = dict(sorted(week['Tags Most-Least'].items(), key=lambda item: item[1]))   
        TopfiveTags = list(week['Tags Most-Least'].items())[:5]

        print('Top 5 Tags')
        print('\t', list(week['Tags Most-Least'].items())[:5])
        print('---------', '\n', '\n')

        list_item = {
            'Week Start Date': StartoftheWeek,
            'Week End Date': EndoftheWeek,
            'Number of Tags This Week': NumberofTags,
            'Top 5 Tags of the Week': TopfiveTags,
                        } 
        
        all_items.append(list_item)



        with open('OFMD_Weekly_Processed_TagData.json', 'w') as OFMD_file_parsed:
            json.dump(all_items,OFMD_file_parsed,indent=2,default=str)