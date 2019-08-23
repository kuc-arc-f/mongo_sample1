# encoding: utf-8
# pymongo 2.5 sample
#
import pymongo
from datetime import datetime

#client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient(host='192.168.10.104', port=27017)

#db = client.get_database('db2')
# use database;
db = client.db2

# find
items = db.post.find()
for post in items:
#    print(post["title"] )
    print(post )
quit()
#insert
post = {
    'title': 't12',
    'content': 'c12',
    'up_date': datetime.now()
}
result1 = db.post.save(post)
quit()
