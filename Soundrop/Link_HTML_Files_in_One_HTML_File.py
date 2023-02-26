#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Will Pisani

This script creates a table of contents web page for all of the Soundrop
royalty report web pages created in "Soundrop_Report_Generator.py".
"""

import os

directory = r'/home/wapisani/Documents/Music/Soundrop_csvs'
os.chdir(directory)

html_files = [x for x in os.listdir(directory) if '.html' in x and 'Soundrop_Royalty_reports.html' not in x]
html_files.sort()

begin_year, begin_month = html_files[0].split('_')[0].split('-')
end_year, end_month = html_files[-1].split('_')[0].split('-')

month_num_to_str = {'01': 'January', '02': 'February', '03': 'March', '04': 'April',
                    '05': 'May', '06': 'June', '07': 'July', '08': 'August',
                    '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
begin_month_str = month_num_to_str[begin_month]
end_month_str = month_num_to_str[end_month]


with open('Soundrop_Royalty_reports.html','w') as f:
    f.write("<!DOCTYPE html>\n")
    f.write("""<html lang="en">\n""")
    f.write('<head>\n')
    f.write('<title>Soundrop Royalties Reports </title>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1">\n')
    f.write("""<link
    rel="preload"
    href="./w3.css"
    as="style"/> 
    """)
    f.write("""<style>/* https://doodad.dev/pattern-generator?share=hex-0-177_156_217_1-156_217_177_1-217_177_156_1-59-208-3-3-20-0-0-0-0-0-0 */
  .pattern-background {
    background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='100%25' width='100%25'%3E%3Cdefs%3E%3Cpattern id='doodad' width='68.13' height='59' viewBox='0 0 34.64101615137755 30' patternUnits='userSpaceOnUse' patternTransform='rotate(208)'%3E%3Crect width='100%25' height='100%25' fill='rgba(217, 177, 156,1)'/%3E%3Cpath d='M-20-20h200v200h-200M33.34 25.75L25.98 21.5L18.62 25.75L18.62 34.25L25.98 38.5L33.34 34.25zM16.02 25.75L8.66 21.5L1.3 25.75L1.3 34.25L8.66 38.5L16.02 34.25zM7.36 10.75L0 6.5L-7.36 10.75L-7.36 19.25L0 23.5L7.36 19.25zM16.02-4.25L8.66-8.5L1.3-4.25L1.3 4.25L8.66 8.5L16.02 4.25zM33.34-4.25L25.98-8.5L18.62-4.25L18.62 4.25L25.98 8.5L33.34 4.25zM42 10.75L34.64 6.5L27.28 10.75L27.28 19.25L34.64 23.5L42 19.25zM24.68 10.75L17.32 6.5L9.96 10.75L9.96 19.25L17.32 23.5L24.68 19.25z' fill='rgba(177, 156, 217,1)'/%3E%3Cpath d='M-20-20h200v200h-200M43.34 25.75L35.98 21.5L28.62 25.75L28.62 34.25L35.98 38.5L43.34 34.25zM26.02 25.75L18.66 21.5L11.3 25.75L11.3 34.25L18.66 38.5L26.02 34.25zM17.36 10.75L10 6.5L2.64 10.75L2.64 19.25L10 23.5L17.36 19.25zM26.02-4.25L18.66-8.5L11.3-4.25L11.3 4.25L18.66 8.5L26.02 4.25zM43.34-4.25L35.98-8.5L28.62-4.25L28.62 4.25L35.98 8.5L43.34 4.25zM52 10.75L44.64 6.5L37.28 10.75L37.28 19.25L44.64 23.5L52 19.25zM60.66 25.75L53.3 21.5L45.94 25.75L45.94 34.25L53.3 38.5L60.66 34.25zM34.68 40.75L27.32 36.5L19.96 40.75L19.96 49.25L27.32 53.5L34.68 49.25zM8.7 25.75L1.34 21.5L-6.02 25.75L-6.02 34.25L1.34 38.5L8.7 34.25zM8.7-4.25L1.34-8.5L-6.02-4.25L-6.02 4.25L1.34 8.5L8.7 4.25zM34.68-19.25L27.32-23.5L19.96-19.25L19.96-10.75L27.32-6.5L34.68-10.75zM60.66-4.25L53.3-8.5L45.94-4.25L45.94 4.25L53.3 8.5L60.66 4.25zM52 40.75L44.64 36.5L37.28 40.75L37.28 49.25L44.64 53.5L52 49.25zM17.36 40.75L10 36.5L2.64 40.75L2.64 49.25L10 53.5L17.36 49.25zM0.04 10.75L-7.32 6.5L-14.68 10.75L-14.68 19.25L-7.32 23.5L0.04 19.25zM17.36-19.25L10-23.5L2.64-19.25L2.64-10.75L10-6.5L17.36-10.75zM52-19.25L44.64-23.5L37.28-19.25L37.28-10.75L44.64-6.5L52-10.75zM69.32 10.75L61.96 6.5L54.6 10.75L54.6 19.25L61.96 23.5L69.32 19.25zM34.68 10.75L27.32 6.5L19.96 10.75L19.96 19.25L27.32 23.5L34.68 19.25z' fill='rgba(156, 217, 177,1)'/%3E%3C/pattern%3E%3C/defs%3E%3Crect fill='url(%23doodad)' height='200%25' width='200%25'/%3E%3C/svg%3E ")
  }
  .border-color {
    border: 5px solid #b19cd9;
  }
  .icon-color {
    color: #b19cd9;
  }
  .div-margin {
    margin-top: 25px;
    margin-bottom: 25px;
    margin-right: 25px;
    margin-left: 25px;    
  }
  a:visited {
    color: blue;
    }
</style>\n """)
    f.write('</head>\n')
    f.write('<body class="pattern-background">\n')
    f.write("""<div class="div-margin w3-content w3-container w3-padding-16 w3-margin-top w3-margin-bottom w3-card border-color" style="background-color:#aaf0d1">
      <div class="w3-center"> \n""")
    f.write(f'<h1 style="text-align:center">Soundrop Royalties Reports from {begin_month_str} {begin_year} - {end_month_str} {end_year}</h1>\n')
    f.write('<center>\n')
    for html_file in html_files:
        current_year, current_month = html_file.split('_')[0].split('-')
        current_month_str = month_num_to_str[current_month]
        f.write(f'<a style="font-size:28px;" href="./{html_file}">{current_month_str} {current_year}</a><br />\n')
    f.write('</center>\n')
    f.write('</div>\n</div>')
    f.write('</body>\n')
    f.write('</html>')

