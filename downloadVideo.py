from pytube import YouTube
import os
import config
import pandas as pd
import configparser

config_obj = configparser.ConfigParser()
config_obj.read("videoInfo.ini")
params = config_obj["VideosInfo"]
topic = params["topic"]
full_path = config.PATH_TO_STORE + topic

def read_data():
    file_name = params["csv_file"]
    csv_path = config.STORE_CSV
    data = pd.read_csv(os.path.join(csv_path+"/"+file_name))
    return data

def download(url,path):
    try:
        yt = YouTube(url)
        yt = yt.streams.filter(progressive=True).get_highest_resolution()
        if not os.path.exists(path):
            os.makedirs(path)
        print("Download Started....")
        yt.download(path)
        print("Downloaded")
    except Exception as e: 
        print("ERROR: ", e)
        pass

def make_download(full_path):
    data = read_data()
    downloaded = list()
    for video in range(config.COUNT):
        download(data['Video_Links'].values[video].strip(),full_path)
        downloaded.append(data['Video_Links'].values[video])

    for i in range(len(downloaded)):
        data.loc[data['Video_Links'] == downloaded[i], 'Downloaded'] = "Yes"
    print(data.head())    
    return downloaded

if __name__ == "__main__":
    make_download()

