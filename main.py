import pymongo
import os
from random import seed, random
from datetime import datetime
from time import sleep

# Get env variables
CONNECTION_STRING = os.environ.get('CONNECTION_STRING')
DB_NAME = os.environ.get('DB_NAME')
COLLECTION_NAME = os.environ.get('COLLECTION_NAME')
BATCH_SIZE = os.environ.get('BATCH_SIZE')
DEVICE_ID = os.environ.get('DEVICE_ID')

# Create client
myclient = pymongo.MongoClient(CONNECTION_STRING)
mydb = myclient[DB_NAME]
mycol = mydb[COLLECTION_NAME]

batchdata= []
while true:
    for i in range(BATCH_SIZE):
    seed(datetime.now().timestamp())
    batchdata.append({ "deviceid": DEVICE_ID, "timestamp": datetime.now() , a:random()*100, b: random()*200, c: random()*50, message: 'Telemetric entity'})
    x = mycol.insert_many(mydict)
    sleep(1)