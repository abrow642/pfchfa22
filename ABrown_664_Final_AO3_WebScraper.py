import requests
from bs4 import BeautifulSoup
import json
import re
import time

title_pattern = re.compile(r'(/works/..)')

title = None
author = None
date = None
freeform_tags = None


all_items = []

# loop through all pages

for item_number in range(1, 800):
    url = f"https://archiveofourown.org/works/search?commit=Search&page={item_number}&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=&work_search%5Bfandom_names%5D=Our+Flag+Means+Death+%28TV%29&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=en&work_search%5Bquery%5D=&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=revised_at&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D="
    # keyword search: f"https://archiveofourown.org/works/search?page={item_number}&work_search%5Bquery%5D=our+flag+means+death"
    print(item_number)

    r = requests.get(url)
    
    time.sleep(3)
    
    if r.status_code == 200:
        print('She works')


        soup = BeautifulSoup(r.text, features="html.parser")

        works = soup.find_all('li', {'class': 'work'})
        for entry in works:
            
            language = entry.find('dd', {'class': 'language'}).text
            if language == 'English':


                title = entry.find('a', {'href': title_pattern})
                if title == None:
                    title = "No title"
                else:
                    title = entry.find('a', {'href': title_pattern}).text
              
                author = entry.find('a', {'rel': 'author'})
                if author == None:
                    author = "No author"
                else:
                    author = entry.find('a', {'rel': 'author'}).text
               
                date = entry.find('p', {'class': 'datetime'})
                if date == None:
                    date = "No Date"
                else:
                    date = entry.find('p', {'class': 'datetime'}).text
                
                
                freeform_tags = entry.find('li', {'class': 'freeforms'})
                if freeform_tags == None:
                    freeform_tags = "No custom tags"
                else:
                    freeform_tags = entry.find_all('li', {'class': 'freeforms'})
                    # print(freeform_tags)
                    
                    
                    all_custom_tags = []
                    
                    for onetag in freeform_tags:
                        # print(onetag.text)
                        onetag = onetag.text                                        
                        all_custom_tags.append(onetag)
                   

                list_item = {
                    'title': title,
                    'author': author,
                    'date': date,
                    'custom_tags': all_custom_tags
                        } 

                all_items.append(list_item)

                with open('OFMD_data.json', 'w') as OFMD_file:
                    json.dump(all_items,OFMD_file,indent=2)

              
    