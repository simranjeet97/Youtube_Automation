import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, required=True)
parser.add_argument('--p', type=str, default=os.getcwd())
parser.op('--file', type=str, required=True)
args = parser.parse_args()

def gettags():
    df = pd.read_csv(args.file)
    data=[]
    for i in df.values:
        data.append(i[0])
    result = ",".join(data)
    return result

print(gettags())
