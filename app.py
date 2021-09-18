from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStock

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/code', methods=['GET'])
def test_get():
    # indicators = db.codes.distinct('group')

    indicators = list(db.codes.find({'group': 'market'}, {'_id': False}))

    return jsonify({all_items: indicators})

@app.route('/stock', methods=['POST'])
def save_info():
    info = request.json
    return jsonify(stocks)


@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
