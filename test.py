from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStock

indicators = list(db.codes.find({'group': 'market'}, {'_id': False}))

print(indicators[0]['name'])

users = list(db.user.find({}, {'_id': False}))

print(users)

code1 = users[0]['codes1']
code2 = users[1]['codes2']
code3 = users[2]['codes3']

rec = list(db.stocks.find({'market': code1, 'sector': code2, 'tag': code3}, {'_id': False}))