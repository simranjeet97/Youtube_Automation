import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import pandas as pd

CLIENT_SECRET_FILE = r'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

categorylist = service.videoCategories().list(part='snippet',regionCode='US',).execute()
df_categorylist = pd.DataFrame(categorylist['items'])
pd.concat([df_categorylist['id'],df_categorylist['snippet'].apply(pd.Series)['title']],axis=1).to_csv('categoryList.csv',index=False)