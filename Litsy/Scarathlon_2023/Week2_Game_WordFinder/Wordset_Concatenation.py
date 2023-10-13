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

import os, json

directory = r'/home/wapisani/Documents/Programming/public-pyprojects/Litsy/Scarathlon_2023/Week2_Game_WordFinder/Wordset_json_files'
os.chdir(directory)

json_files = [x for x in os.listdir(directory) if '.json' in x]
json_files.sort()

data_to_merge = list()
for j in json_files:
    with open(j, 'r') as infile:
        data_to_merge.extend(json.load(infile))

with open('Wordset_Dictionary_A-Z.json', 'w') as output_file:
    json.dump(data_to_merge, output_file)