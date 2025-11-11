from flask import Flask, jsonify, request

app = Flask(__name__)

# GET
# (1) 전체 게시물을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    date = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}
    return date

# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    data = {'result':'success', 'data':{'feed1':'data1'}}
    return data

# POST
# (1) 게시글을 작성 하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feeds():
    name = request.form.get('name')
    age = request.form.get('age')

    print(name, age)

    return jsonify({'result':'success'})

datas = [{"items": [{"name": "items","price": 10}]}]

@app.route('/api/v1/datas', methods=['GET'])
def get_datas():
    return {"datas":datas}

@app.route('/api/v1/datas', methods=['POST'])
def create_datas():
    body = request.get_json()
    new_data = {'items': body.get('items', [])}
    datas.append(new_data)

    return new_data, 201
