from pytube import YouTube
import os
import config
import pandas as pd
import configparser

config_obj = configparser.ConfigParser()

config_obj.read("videoInfo.ini")

params = config_obj["VideosInfo"]

file_name = params["csv_file"]
topic = params["topic"]

csv_path = config.STORE_CSV
data = pd.read_csv(os.path.join(csv_path+"/"+file_name))
print(data.head())

full_path = config.PATH_TO_STORE + topic

def download(url,path):
    try:
        yt = YouTube(url)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
    except Exception as e: 
        print("ERROR: ", e)
        pass

downloaded = list()
for video in range(config.COUNT):
    download(data['Video_Links'].values[video].strip(),full_path)
    downloaded.append(data['Video_Links'].values[video])

for i in range(len(downloaded)):
    data.loc[data['Video_Links'] == downloaded[i], 'Downloaded'] = "Yes"

print(data.head())


