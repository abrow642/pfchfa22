# pfchfa22
Fanfiction Folksonomy Case Study
Our Flag Means Death on Archive of Our Own

Programming for Cultural Heritage Final Project

Contents (in order of use):
  1. ABrown_664_Final_AO3_WebScraper: scrapes AO3 for title, author, date, and freeform tags of specific link
      a. ABrown_664_Final_OFMD_RawData: JSON file containing aforementioned data
  2. ABrown_664_Final_Processing_OFMData: extracts # total fics scraped, # total tags, top 10 used tags, groups data by week from oldest fic, filters for tags used more than twice, exports all collected data into new, clean JSON
  3. ABrown_664_Final_Parser_Processed_TagData: prints week start date, week end date, number of tags per week (of the tags used more than twice), top 5 used tags and the number of their occurrences. Exports all aforementioned data to JSON.
      a. ABrown_664_Final_OFMD_Processed_Weekly_TagData
      
This project scrapes Archive of Our Own for freeform tag data. It was initially used to collect data on Our Flag Means Death, but can be adjusted to scrape for other searches. To look at other sources, change the source URL in the webscraper. 

The code relies on dateparser, datetime, Counter. 
      
