from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStock

indicators = list(db.codes.find({'group': 'market'}, {'_id': False}))

print(indicators[0]['name'])