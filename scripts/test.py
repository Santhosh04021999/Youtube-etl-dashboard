import json
import pandas as pd
import csv


channel_data=[]
with open(r"data\raw\channel_details.json",'r')as file:
    data=json.load(file)
# print(data.get('items'))
for items in data.get('items'):
    snippet=items.get('snippet')
    thumnbails=snippet.get('thumbnails')
    mode=thumnbails.get('high','')
    statistics=items.get('statistics')
    channel_data.append({
        'title': snippet['title'],
        'description': snippet['description'],
        'channel_create_dt': snippet['publishedAt'],
        'thumbnail':mode['url'],
        'country':snippet['country'],
        'viewCount':statistics['viewCount'],
        'subscriberCount':statistics['subscriberCount'],
        'videoCount':statistics['videoCount']
        })
raw_data=pd.DataFrame(channel_data)
for col in raw_data.select_dtypes(include='object').columns:
    raw_data[col] = raw_data[col].str.replace(r'[\r\n]+', ' ', regex=True)
raw_data.to_csv(r"data\processed\channel_data.csv",index=False, quoting=csv.QUOTE_ALL,quotechar='"', escapechar='\\')
print("Cleansed video_data loaded into processed folder")