import glob as gb
import json
import pandas as pd
import re
import csv

def channel_data():
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
    print("Channel data loaded into processed folder")

def cleansed_video_data():
    #iterating the folder to fetch all the pattern files in the folder
    file_list=gb.glob(r'data\raw\video_details_*')
    # print(file_list)

    video_data=[]
    #fetch the required data 
    for file in file_list:
        with open(file,'r',encoding='utf-8') as source:
            data=json.load(source)
        for video in data.get('items',[]):
            snippet = video.get('snippet', {})
            stats = video.get('statistics', {})
            content = video.get('contentDetails', {})
            thumbnails =snippet.get('thumbnails',{})	
            mode=thumbnails.get('standard',{})
            video_data.append({'video_id': video['id'],
                        'title': snippet.get('title'),
                        'description':snippet.get('description'),
                        'published_at':snippet.get('publishedAt'),
                        'thumbnails': mode.get('url',''),
                        'tags': ', '.join(snippet.get('tags', [])),
                        'language': snippet.get('defaultLanguage', 'NA'),
                        'category_id': snippet.get('categoryId', 'NA'),
                        'view_count': stats.get('viewCount', 0),
                        'like_count': stats.get('likeCount', 0),
                        'comment_count': stats.get('commentCount', 0),
                        'duration': content.get('duration', 'NA'),
                        'definition': content.get('definition', 'NA'),
                    })
    raw_data=pd.DataFrame(video_data)

    def duration_to_seconds(duration):
        match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', duration)
        if not match:
            return 0
        h = int(match.group(1)) if match.group(1) else 0
        m = int(match.group(2)) if match.group(2) else 0
        s = int(match.group(3)) if match.group(3) else 0
        return h * 3600 + m * 60 + s

    raw_data['duration'] = raw_data['duration'].apply(duration_to_seconds)
    for col in raw_data.select_dtypes(include='object').columns:
        raw_data[col] = raw_data[col].str.replace(r'[\r\n]+', ' ', regex=True)

    raw_data.to_csv(r"data\processed\cleansed_video_data.csv",index=False, quoting=csv.QUOTE_ALL,quotechar='"', escapechar='\\')
    print("Cleansed video_data loaded into processed folder")

if __name__=='__main__':
    channel_data()
    cleansed_video_data()
