from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStock

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/code', methods=['GET'])
def selection():
    # indicators = db.codes.distinct('group')
    indicators = list(db.codes.find({'group': 'market'}, {'_id': False}))

    return jsonify({'all_items': indicators})

@app.route('/code2', methods=['GET'])
def selection2():
    # indicators = db.codes.distinct('group')
    indicators = list(db.codes.find({'group': 'sector'}, {'_id': False}))

    return jsonify({'all_items': indicators})

@app.route('/code3', methods=['GET'])
def selection3():
    # indicators = db.codes.distinct('group')
    indicators = list(db.codes.find({'group': 'tag'}, {'_id': False}))

    return jsonify({'all_items': indicators})

@app.route('/codes', methods=['POST'])
def save_info():
    name_receive = request.form['name_give']
    item = db.codes.find_one({'name': name_receive}, {'_id': False})['code']
    doc = {
        'code1': item
    }

    db.user.insert_one(doc)

    return jsonify({'code1': item})

@app.route('/codes2', methods=['POST'])
def save_info2():
    name_receive = request.form['name_give']
    item = db.codes.find_one({'name': name_receive}, {'_id': False})['code']
    doc = {
        'code2': item
    }

    db.user.insert_one(doc)

    return jsonify({'code2': item})

@app.route('/codes3', methods=['POST'])
def save_info3():
    name_receive = request.form['name_give']
    item = db.codes.find_one({'name': name_receive}, {'_id': False})['code']
    doc = {
        'code3': item
    }

    db.user.insert_one(doc)

    return jsonify({'code3': item})

@app.route('/stock', methods = ['GET'])
def save_info4():
    users = list(db.user.find({}, {'_id': False}))

    code1 = users[0]['code1']
    code2 = users[1]['code2']
    code3 = users[2]['code3']

    rec = list(db.stocks.find({'market': code1, 'sector': code2, 'tag': code3}, {'_id': False}))

    return jsonify({'user': rec})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
