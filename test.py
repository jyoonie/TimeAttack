from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStock

indicators = db.codes.distinct('group')

print(indicators)