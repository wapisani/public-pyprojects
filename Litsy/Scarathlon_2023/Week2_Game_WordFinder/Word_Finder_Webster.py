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
"""
import os, json, string, re

directory = r'/home/wapisani/Documents/Programming/public-pyprojects/Litsy/Scarathlon_2023/Week2_Game_WordFinder'
os.chdir(directory)

json_file = r'Websters_Unabridged_Dictionary_UpdatedJan2023.json'

with open(json_file, 'r') as f:
    webster = json.load(f)

# We don't need definitions for this challenge
words = [word for word in webster.keys()]

# The Scarathlon 2023 phrase
phrase = "happyhalloweenscarathloners"

phrase_count = {s:0 for s in string.ascii_lowercase}

for s in phrase:
    phrase_count[s] += 1
    
# Determine the letters that are not present in 
# the phrase because we can skip the words without them
letters_not_present = ''
for key in phrase_count.keys():
    if phrase_count[key] == 0:
        letters_not_present += key

# Skip words with hyphens, '-' must be escaped in a regex string
letters_not_present = '[\-' + letters_not_present + ']'

found_words = []
for w in words:
    
    # Skip word if a letter not present in the phrase
    # is in the word
    if bool(re.search(letters_not_present,w)):
        continue
    
    # Remove all one or two letter words
    if len(w) <= 2:
        continue
    
    # Remove all words that have white space
    if ' ' in w:
        continue
    
    word_count = {s:w.count(s) for s in w}
    
    # Check if the word count is less than or equal
    # to the phrase count, if it is, then the word
    # can be spelled from the letters in the phrase
    for l in word_count:
        num_l_in_word = word_count[l]
        num_l_in_phrase = phrase_count[l]
        # Check all the letters in the word and if the number of letters 
        # for a particular letter is greater than the number of letters for that 
        # particular letter in the phrase, break out of the loop and move on to 
        # the next word
        if num_l_in_word > num_l_in_phrase:
            break
    
    # Since the loop exited normally, all of the letters in the word
    # must be present in the phrase, so we add it to the found_words list
    else:
        found_words.append(w)

print(f"Given the list of words in the Webster's Unabridged Dictionary, \
{len(found_words)} words were found that can be created with the \
phrase {phrase}.")

with open('found_words.txt','w') as f:
    f.write(f"Given the list of words in the Webster's Unabridged Dictionary, \
{len(found_words)} words were found that can be created with the \
phrase {phrase}.\n\n")
    f.write("Here is the list of found words.\n")
    found_words_str = '\n'.join(found_words)
    f.write(found_words_str)

print("\nThe list of found words was written to the file found_words.txt.")

