# encoding: utf-8
" delete"
import pymongo
from datetime import datetime

#client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient(host='192.168.10.104', port=27017)

db = client.db2
db.post.drop()
