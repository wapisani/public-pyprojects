#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: William A. Pisani
@email: wapisani@mtu.edu

This script generates an HTML page of a Soundrop royalty earnings spreadsheet.
"""

import os, re, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


directory = r''
os.chdir(directory)

soundrop_csvs = [x for x in os.listdir(directory) if '.csv' in x]
soundrop_csvs.sort()

over_time = {}

for csv in soundrop_csvs:
    date = csv.split('_')[1]
    year, month = date.split('-')
    month_num_to_str = {'01': 'January', '02': 'February', '03': 'March', '04': 'April',
                        '05': 'May', '06': 'June', '07': 'July', '08': 'August',
                        '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
    month_str = month_num_to_str[month]
    output_name = date + '_'
    df = pd.read_csv(csv)
    print(f"Now working on {month_str} {year}")
    columns = list(df.columns)
    
    net_revenue = df['Net Revenue in USD'].sum()
    total_streams = df['Quantity'].sum()
    countries = df.Country.unique()
    total_countries = len(countries)
    total_spotify_streams = df[df['Service'] == 'Spotify']['Quantity'].sum()
    total_spotify_rev = df[df['Service'] == 'Spotify']['Net Revenue in USD'].sum()
    
    net_rev_by_service = df.groupby(['Service'])['Net Revenue in USD'].sum()
    
    net_rev_by_track = df.groupby(['Track Title'])['Net Revenue in USD'].sum()
    
    streams_by_service = df.groupby(['Service'])['Quantity'].sum()
    
    streams_by_country = df.groupby(['Country'])['Quantity'].sum()
    
    net_rev_by_country = df.groupby(['Country'])['Net Revenue in USD'].sum()
    streams_by_track = df.groupby(['Track Title'])['Quantity'].sum()
    
    streams_by_track_service = df.groupby(['Track Title','Service'])['Quantity'].sum()
    streams_by_country_service = df.groupby(['Country','Service'])['Quantity'].sum()
    streams_by_track_country = df.groupby(['Track Title','Country'])['Quantity'].sum()
    streams_by_country_track = df.groupby(['Country','Track Title'])['Quantity'].sum()
    # To print the full data frame, do print(df.to_string())
    # Don't do this for a large data frame!!☺
    
    # Get countries where the net rev is greater than 10 cents
    top_country_net_rev = net_rev_by_country[net_rev_by_country>0.3]
    
    # Plot net rev per country greater than 1 cent with a bar chart
    fig, ax = plt.subplots()
    ax_net_rev_by_country = net_rev_by_country[net_rev_by_country>0.1].sort_values().plot(kind='barh',color='#b19cd9',ylabel="Countries with net revenue greater than $0.01",xlabel="$ (USD)")
    # fig_net_rev_by_country = ax_net_rev_by_country.get_figure()
    plt.tight_layout()
    fig.savefig(output_name+'Net_Rev_by_Country.png',dpi=300)
    plt.close(fig)
    
    # Plot net rev per service
    fig, ax = plt.subplots()
    ax_net_rev_by_service = net_rev_by_service.sort_values().plot(kind='barh',color='#b19cd9',xlabel='$ (USD)')
    # fig_net_rev_by_service = ax_net_rev_by_service.get_figure()
    plt.tight_layout()
    fig.savefig(output_name+'Net_Rev_by_Service.png',dpi=300)
    plt.close(fig)
    
    # Plot streams per service
    fig, ax = plt.subplots()
    ax_streams_by_service = streams_by_service.sort_values().plot(kind='barh',color='#b19cd9',xlabel='Number of streams/purchases')
    # fig_streams_by_service = ax_streams_by_service.get_figure()
    plt.tight_layout()
    fig.savefig(output_name+'Streams_by_Service.png',dpi=300)
    plt.close(fig)
    
    # Plot streams per track, need to figure out how to make the plot big enough
    # such that the track titles are not cut off.
    # ax_streams_by_track = streams_by_track.sort_values().plot(kind='barh',color='purple',xlabel='Number of streams/purchases')
    # fig = ax_streams_by_track.get_figure()
    # plt.tight_layout()
    # fig.savefig(output_name+'Streams_by_Track.pdf')
    
    # Plot streams per release
    fig, ax = plt.subplots()
    ax_streams_by_release = df.groupby(['Release Title'])['Quantity'].sum().sort_values().plot(kind='barh',color='#b19cd9',xlabel='Streams/purchases')
    # fig_streams_by_release = ax_streams_by_release.get_figure()
    plt.tight_layout()
    fig.savefig(output_name+'Streams_by_Release.png',dpi=300)
    plt.close(fig)
    
    fig_net_rev_country = output_name+'Net_Rev_by_Country.png'
    fig_net_rev_service = output_name+'Net_Rev_by_Service.png'
    fig_streams_service = output_name+'Streams_by_Service.png'
    fig_streams_release = output_name+'Streams_by_Release.png'
    
    str_streams_track_service = streams_by_track_service.to_string().split('\n')
    str_streams_by_country_service = streams_by_country_service.to_string()
    
    
    for country in countries:
        str_streams_by_country_service = re.sub(country+' ',country+'\n',str_streams_by_country_service)
    
    
    
    with open(date+'_Soundrop_Royalties_Report.html','w') as f:
        f.write("<!DOCTYPE html>\n")
        f.write("""<html lang="en">\n""")
        f.write('<head>\n')
        f.write(f'<title>Soundrop Royalties Report for {month_str} {year}</title>\n')
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
      img {
        max-width: 100%;
        height: auto;
      }
    </style>\n """)
        f.write('</head>\n')
        f.write('<body class="pattern-background">\n')
        f.write("""<div class="div-margin w3-content w3-container w3-padding-16 w3-margin-top w3-margin-bottom w3-card border-color" style="background-color:#aaf0d1">
          <div class="w3-center"> \n""")
        f.write(f'<h1 style="text-align:center">Soundrop Royalties Report for {month_str} {year}</h1>\n')
        f.write('<p style="font-size:28px">')
        f.write(f'Net Revenue: ${net_revenue:0.2f}<br />\n')
        f.write(f'Total Streams: {total_streams}<br />\n')
        f.write(f'Total Countries: {total_countries}<br />\n')
        f.write(f'Total Spotify Net Rev: ${total_spotify_rev:0.2f}<br />\n')
        f.write(f'Total Spotify Streams: {total_spotify_streams}\n')
        f.write('</p>')
        f.write('<center>\n')
        f.write(f"""<img src="./{fig_net_rev_country}" class="w3-round w3-image w3-center" width="700" height="500">\n""")
        f.write('<h3 style="text-align:center">Figure 1: Net Revenue by Country</h3>\n')
        f.write(f"""<img src="./{fig_net_rev_service}" class="w3-round w3-image w3-center" width="700" height="500">\n""")
        f.write('<h3 style="text-align:center">Figure 2: Net Revenue by Service</h3>\n')
        f.write(f"""<img src="./{fig_streams_service}" class="w3-round w3-image w3-center" width="700" height="500">\n""")
        f.write('<h3 style="text-align:center">Figure 3: Streams by Service</h3>\n')
        f.write(f"""<img src="./{fig_streams_release}" class="w3-round w3-image w3-center" width="700" height="500">\n""")
        f.write('<h3 style="text-align:center">Figure 4: Streams by Release</h3>\n')
        f.write('</center>\n')
        # f.write(f"""<img src="./" class="w3-round w3-image" width="700" height="500">\n""")
        # f.write('<h3 style="text-align:center"></h3>\n')
        f.write('<h3>Streams grouped by track then service:</h3>\n')
        f.write('<p> \n')
        for line in str_streams_track_service[1:]:
            if ')' in line:
                line = line.split(')')
                f.write(f"<br /><br /><b>{line[0]})</b><br />")
                f.write(f"{line[1]}<br />")
            else:
                f.write(f"{line}<br />")
        
        f.write('</p>\n')
        
        f.write('<h3>Streams grouped by country then service</h3>\n')
        f.write('<p> \n')
        for line in str_streams_by_country_service.split('\n')[1:]:
            if line == '':
                continue
            if line[0] != ' ':
                f.write(f"<br /><b>{line}</b><br />")
            else:
                f.write(f"{line}<br />")
                
        f.write('</p> \n')
        f.write('</div>\n</div>')
        f.write('</body>\n')
        
        
        
        
        
        f.write('</html>')
    
    
    # Data over time
    over_time[date] = {}
    over_time[date]['net_rev'] = net_revenue
    over_time[date]['total_streams'] = total_streams
    over_time[date]['countries'] = total_countries
    over_time[date]['total_spotify_rev'] = total_spotify_rev
    over_time[date]['total_spotify_streams'] = total_spotify_streams
    over_time[date]['rev_per_track'] = net_rev_by_track.to_dict()
    over_time[date]['rev_per_country'] = net_rev_by_country.to_dict()
    over_time[date]['streams_per_service'] = streams_by_service.to_dict()
    
    
# Save over time data to JSON for later analysis
# NpEncoder from https://stackoverflow.com/a/57915246 to prevent a TypeError 
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)
    
with open('Soundrop_Data_Over_time.json','w') as f:
    json.dump(over_time,f,cls=NpEncoder)