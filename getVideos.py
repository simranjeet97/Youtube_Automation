import urllib.request
import re
import pandas as pd
from datetime import datetime
from pytube import YouTube
import config
import os
import configparser

def search():
    print(config.MESSAGE)
    global search_keyword
    search_keyword=input("Enter the Topic you want to Search : ").strip()

    if len(search_keyword.split(" ")) == 1 and len(search_keyword.split(" ")) != 0 and search_keyword != None:
        html = urllib.request.urlopen(config.SEARCH_LINK + search_keyword + config.COMM_SUBLINK)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    elif len(search_keyword.split(" ")) > 1:
        search_keyword = search_keyword.replace(" ","+")
        html = urllib.request.urlopen(config.SEARCH_LINK + search_keyword + config.COMM_SUBLINK)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return video_ids

def createList():
    video_ids = search()
    videos_list = list()
    for id in range(len(video_ids)):
        link = config.WATCH_LINK + str(video_ids[id])
        videos_list.append(link)
    return videos_list

def createDataFrame():
    videos_list = createList()
    date = datetime.today().strftime('%Y%m%d')
    videos_list = list(set(videos_list))
    df = pd.DataFrame(videos_list,columns=['Video_Links'])
    time=list()
    for video in range(len(videos_list)):
        youtubeObject = ""
        youtubeObject = YouTube(videos_list[video])
        time.append(round((youtubeObject.length/60),2))

    df['Length(Min)'] = time
    df = df.sort_values(by=['Length(Min)'], ascending=False)
    df = df.reset_index(drop=True)
    #print(df.head())
    df.to_csv(os.path.join(config.STORE_CSV,config.NAME_CSV+config.DATE+ "_" + search_keyword + ".csv"))

    #Setting Configuration File for Setting Parameters
    configObj = configparser.ConfigParser()
    configObj.add_section('VideosInfo')
    configObj.set('VideosInfo', 'topic', search_keyword)
    configObj.set('VideosInfo', 'csv_file', config.NAME_CSV+config.DATE+ "_" + search_keyword + ".csv")

    with open(config.PROJECT_PATH+"videoInfo.ini", 'w') as configfile:
        configObj.write(configfile)

if __name__ == "__main__":
    createDataFrame()
