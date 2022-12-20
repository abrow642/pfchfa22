import json
import dateparser
from datetime import datetime, timedelta
from collections import Counter

all_tags_ever = {}
weeklytags = {}
all_items = []


def sort_date_funk(date_item):
    return dateparser.parse(date_item['date'])


with open('OFMD_data.json', 'r') as datafile:
    processed_json = json.load(datafile)

# this section provides preliminary data: number of all fics
    print('Total Quantity of Fics')
    print('\t', len(processed_json))



# this section provides preliminary data: number of all tags, top 10 most used tags 
    all_tags = []

    for entry in processed_json:
        all_tags += entry['custom_tags']
    
    print('Total Quantity of Tags')
    print('\t', len(all_tags))

    all_tags_count = Counter(all_tags)

    # only grab tags that occur more than twice
    all_tags_ever = {k: v for k, v in all_tags_count.items() if v > 2}

    # sort tags by quanitity of occurences
    all_tags_ever = dict(sorted(all_tags_ever.items(), key=lambda item: item[1], reverse = True))   

    # prints total number of tags that occur more than once
    print('\n', 'Total Quantity of Tags That Appear More Than Twice')
    print('\t',len(all_tags_ever))

    # prints top 10 most used tags
    top_ten_tags = list(all_tags_ever.items())[:10]
    print('Top 10 Tags:')
    print(top_ten_tags)


# this section works on organizing the data by week in order to determine the most popular tags over time

    # sort data by date (oldest to newest)
    processed_json = sorted(processed_json, key = sort_date_funk)

    # find start date, end date
    startdate = dateparser.parse(processed_json[0]['date'])
    enddate = dateparser.parse(processed_json[-1]['date'])

    print(startdate)
    print(enddate)

    # group by week
    days_of_interest = enddate - startdate

    print(days_of_interest)

    for weeks in range(0, days_of_interest.days, 7):
        fromtime = startdate + timedelta(days=weeks)
        endtime = fromtime + timedelta(days=7)

        print(f"From {fromtime} to {endtime}")

        works = list(filter(lambda x: fromtime < dateparser.parse(x['date']) < endtime, processed_json))
        tags = []

        # parse tags
        for fic in works:
            tags += fic['custom_tags']
        
        tagcount = Counter(tags)

        # only grab tags that occur more than once
        weeklytags[fromtime] = {k: v for k, v in tagcount.items() if v > 2}

        # sort tags by quanitity of occurences
        weeklytags[fromtime] = dict(sorted(weeklytags[fromtime].items(), key=lambda item: item[1], reverse = True))    

        print(weeklytags[fromtime])

        json_StartDate = fromtime
        json_EndDate = endtime
        json_WeekNum = len(weeklytags)
        json_TagNum = len(weeklytags[fromtime])
        json_TagsMost = weeklytags[fromtime]

        list_item = {
            'Week Start Date': json_StartDate,
            'Week End Date': json_EndDate,
            'Week Number': json_WeekNum,
            'Number of Tags': json_TagNum,
            'Tags Most-Least': json_TagsMost,
                        } 
        
        all_items.append(list_item)

        with open('OFMD_Processed_TagData.json', 'w') as OFMD_file_parsed:
            json.dump(all_items,OFMD_file_parsed,indent=2,default=str)

    
