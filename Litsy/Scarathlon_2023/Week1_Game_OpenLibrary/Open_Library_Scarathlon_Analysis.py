# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 10:32:54 2023

@author: Dr. Will Pisani

The purpose of this script is to load the search results from Open Library
and filter until only fiction books are found.
"""

import os, json

directory = r'F:\Documents\Programming\Python\python-projects\Litsy_Scarathlon'
os.chdir(directory)

json_files = [x for x in os.listdir(directory) if '.json' in x]

subject_queries = [x.split('_')[2] for x in json_files]
total_count = 0
books = {}
# loaded_jsons = {} # For debugging and data exploration
with open('Scarathlon_PumpkinHeads_Dowry_of_Blood_Game1.txt','w',encoding='utf8') as h:
    h.write("Open Library's Search API was used to find these books. Instructions on using the API were found at this URL: https://openlibrary.org/dev/docs/api/search\n")
    h.write("The Open Library's database was queried (using the 'q' solr query) using these subjects as keywords (spaces between words): " + ', '.join(subject_queries) + "\n")
    for index,j in enumerate(json_files):
        subject = subject_queries[index]
        h.write(f"\n\nFor {subject}:\n")
        subject_count = 0
        books[subject] = {'list': []}
        with open(j,'r') as f:
            cur_json = json.load(f)
            # loaded_jsons[subject] = cur_json # For debugging and data exploration
            for doc in cur_json['docs']:
                if 'author_name' not in doc or 'title' not in doc: # Filter out any entry without a title or authors
                    continue
                    
                if subject in doc['author_name'][0] or subject.lower() in doc['author_name'][0]: # Filter out entries that have the subject in the author's name
                    continue
                if 'coloring' in doc['title']: # Filter out coloring books
                    continue
                
                if 'subject' not in doc: # Filter out anything without a genre
                    continue
                else:
                    book_subjects = doc['subject']
                    for s in book_subjects:
                        if 'Fiction' in s or 'fiction' in s:
                            break
                    else:
                        continue # Filter out anything that's not fiction
                
                author = ', '.join(doc['author_name'])
                title = doc['title']
                
                books[subject]['list'].append(title.title() + ' - ' + author.title())
                
                
                
        books[subject]['set'] = set(books[subject]['list']) # Remove simple duplicates by converting the list to a set
        books[subject]['set2list'] = sorted(list(books[subject]['set'])) # Convert the set to a list and sort it
        for i,b in enumerate(books[subject]['set2list']):
            h.write(f"{i+1} {b}\n")
            total_count += 1
            subject_count += 1
        h.write(f"Total number of books for {subject}: {subject_count}\n")
        
    h.write(f"Total number of books across all subjects: {total_count}")
