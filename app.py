from bson.objectid import ObjectId
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

# mongo_key = '<put your key here>'
mongo_key = 'mongodb+srv://sparta:test@cluster0.qt51rgo.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongo_key)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/im", methods=["POST"])
def bucket_post():
    name = request.form['name_give']
    position = request.form['po_give']
    s_i = request.form['s_i_give']
    mbti = request.form['mbti_give']
    comment = request.form['comment_give']
    blog = request.form['blog_give']
    image = request.form['img_give']

    
    doc = {
        'name':name,
        'position':position,
        'self_introduce':s_i,
        'mbti':mbti,
        'comment':comment,
        'blog':blog,
        'image':image
    }

    db.novengers.insert_one(doc)

    return jsonify({'msg': 'Save Compelete !'})

@app.route('/im', methods=["PUT"])
def bucket_put():
    name = request.form['name_give']
    position = request.form['po_give']
    s_i = request.form['s_i_give']
    mbti = request.form['mbti_give']
    comment = request.form['comment_give']
    blog = request.form['blog_give']
    image = request.form['img_give']

    filter = {'name':name}

    doc = {
        'position':position,
        'self_introduce':s_i,
        'mbti':mbti,
        'comment':comment,
        'blog':blog,
        'image':image
    }
    
    for i in doc.keys():
        new_value = {"$set":{i:doc[i]}}
        db.novengers.update_one(filter, new_value)
    # new_value = {"$set":{'position':"181818"}}
    # db.novengers.update_one(filter, new_value)

    return jsonify({'msg':'수정이 완료됐습니다.'})

@app.route('/im', methods=["DELETE"])
def bucket_delete():
    name = request.form['name_give']

    doc = {
        'name':name
    }
    db.novengers.delete_one(doc)
    return jsonify({'msg':"삭제가 완료됐습니다."})

@app.route("/im", methods=["GET"])
def bucket_get():
    # temp = db.novengers.find({})
    # for i in temp:
    #     print(i)
    bucket_li = list(db.novengers.find({}))
    print(bucket_li)
    for i in range(0, len(bucket_li)):
        bucket_li[i]['_id'] = str(bucket_li[i]['_id'])
    
    print(bucket_li)
    
    return jsonify({'result': bucket_li})
    # return jsonify({'result': "message"})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5003, debug=True)