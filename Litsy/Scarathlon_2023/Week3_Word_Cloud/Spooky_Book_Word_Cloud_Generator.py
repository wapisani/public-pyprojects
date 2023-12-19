#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2023 Dr. William A. Pisani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The purpose of this script is to load the search results from Open Library
and filter until only fiction books are found.

This script will load in books found on Project 
Gutenberg and generate word clouds from the text.
"""

import os
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

directory = r'/home/wapisani/Documents/Programming/public-pyprojects/Litsy/Scarathlon_2023/Week3_Word_Cloud'
os.chdir(directory)

text_files = [x for x in os.listdir(directory) if '.txt' in x]

stopwords = set(STOPWORDS)
additional_words = ['Gutenberg','an\'','The','the',
                    'Project','S','one','back','will',
                    'man','time','may','o\'','said',
                    'house','without','year','upon',
                    'work','see','say','now','hand',
                    'way','seen','might','still','ye',
                    'know','make','along','come','thought',
                    'look','must','eye','though','made',
                    'day','came','place','tell','side',
                    'door','room','nothing','little','never',
                    'tell','seemed','thing','ll','old','much',
                    'go','d','The_','_The','bed','don\'t','dont','Illustration',
                    'O','o','Twas','ze','Ah','gave','give','took','went',
                    'thro\'','thus','got','siz','many','well','away','wid','thee',
                    'u','long','looked','take','two','even','de','don_t','put',
                    'sir','Yes','something','first']
for word in additional_words:
    stopwords.add(word)

for file in text_files:
    print(file)
    with open(file,'r') as f:
        text = f.read()
        
    wordcloud = WordCloud(width = 2000, height = 2000,
                    background_color ='white',
                    stopwords = stopwords,
                    min_font_size = 20).generate(text)
     
    # plot the WordCloud image                       
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.savefig(file.split('.')[0]+'_WordCloud.png',dpi=400)
    plt.show()
    
