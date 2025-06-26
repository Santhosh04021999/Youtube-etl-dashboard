import requests
import json
import variables as var

def channel_details():
    response=requests.get(var.channel_details)
    if response.status_code ==200:
        data=response.json()
        with open('data/raw/channel_details.json','w')as file:
            json.dump(data,file,indent=4)
        print('channel_data file saved into data/raw/channel_details.json')
    else:
        print('issue on url to retrieve information')

with open('data/raw/channel_details.json','r') as file:
    data=json.load(file)
    playlist_id=data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

def get_all_video_ids(playlist_id):
    video_ids = []
    base_url = 'https://www.googleapis.com/youtube/v3/playlistItems'
    next_page_token = ''

    while True:
        params = {
            'part': 'snippet',
            'playlistId': playlist_id,
            'maxResults': 50,
            'pageToken': next_page_token,
            'key': var.youtube_api_key
        }
        response = requests.get(base_url, params=params).json()

        for item in response.get('items', []):
            video_ids.append(item['snippet']['resourceId']['videoId'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            # print(video_ids)
            break   
    return video_ids


def get_video_details(video_ids):
    file_count=1
    for i in range(0, len(video_ids), 50):
        id_chunk = ','.join(video_ids[i:i + 50])
        url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,contentDetails&id={id_chunk}&key={var.youtube_api_key}'
        response = requests.get(url).json()
        with open(f'data/raw/video_details_{file_count}.json','w') as source:
            json.dump(response,source,indent=4)
        file_count+=1
    print('video data file saved into data/raw/')
    

if __name__=='__main__':
    video_ids=get_all_video_ids(playlist_id)
    get_video_details(video_ids)
    
    

