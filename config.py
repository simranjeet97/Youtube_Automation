from datetime import datetime

PATH_TO_STORE = "../Users/simranjeetsingh1497/Desktop/MLOPS_Project_1/Youtube_Automation/Download_Videos/"
STORE_CSV = r'/Users/simranjeetsingh1497/Desktop/MLOPS_Project_1/Youtube_Automation/Files'
PROJECT_PATH = r'/Users/simranjeetsingh1497/Desktop/MLOPS_Project_1/Youtube_Automation/'

IG_USERNAME = "freebirdscrew" 
IG_PASSWORD = "$imr@n2022F"

SEARCH_LINK = "https://www.youtube.com/results?search_query="
COMM_SUBLINK = "&sp=EgIwAQ%253D%253D"
WATCH_LINK = "https://www.youtube.com/watch?v="
NAME_CSV = "VideoLinks_"

DATE = datetime.today().strftime('%Y%m%d')

COUNT = 3


MESSAGE = """ 
              ----------------YouTube Automation-----------------------
               Welcome to Simranjeet Singh - YouTube Automation Program \n
               > Get Videos of your Searched Topic ! \n
               > Get Downloaded by Greater then 10 minutes ! \n
          """