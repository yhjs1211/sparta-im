from bson.objectid import ObjectId
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

mongo_key = 'Your Mongo Key'

client = MongoClient('Your Mongo Key')
db = client.dbsparta

@app.route('/')
def home():
    try:
        return render_template('index.html'), 200
    except Exception as e:
        print(e)
        return jsonify({ 'msg':e }), 500

# 회원정보를 DB에 저장
@app.route("/im", methods=["POST"])
def bucket_post():
    try:
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

        return jsonify({ 'msg': 'Save Compelete !' }), 200
    except Exception as e:
        print(e)
        return jsonify({ 'msg':e }), 500

# 회원정보 수정
@app.route('/im', methods=["PUT"])
def bucket_put():
    try:
        post_id = request.form['post_id_give']
        name = request.form['name_give']
        position = request.form['po_give']
        s_i = request.form['s_i_give']
        mbti = request.form['mbti_give']
        comment = request.form['comment_give']
        blog = request.form['blog_give']
        image = request.form['img_give']
        

        # print("post_id:")
        # print(post_id)

        # print("===================")
        # for i in request.form.keys():
        #     print(i + ':' + request.form[i])

        filter = { '_id':ObjectId(post_id) }

        doc = {
            'name':name,
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

        return jsonify({ 'msg':'수정이 완료됐습니다.' }), 200
    except Exception as e:
        print(e)
        return jsonify({ 'msg':e }), 500

# 회원정보 삭제
@app.route('/im', methods=["DELETE"])
def bucket_delete():
    try:
        post_id_receive = request.form['post_id_give']
        db.novengers.delete_one({'_id':ObjectId(post_id_receive)})
        return jsonify({ 'msg':"삭제가 완료됐습니다." }), 200
    except Exception as e:
        print(e)
        return jsonify({ 'msg':e }), 500
    

# 회원정보를 클라이언트에 넘겨줌
@app.route("/im", methods=["GET"])
def bucket_get():
    try:
        # temp = db.novengers.find({})
        # for i in temp:
        #     print(i)
        bucket_li = list(db.novengers.find({}))
        # print(bucket_li)
        for i in range(0, len(bucket_li)):
            bucket_li[i]['_id'] = str(bucket_li[i]['_id'])
    
        # print(bucket_li)
    
        return jsonify({ 'result': bucket_li }), 200
        # return jsonify({'result': "message"})
    except Exception as e:
        print(e)
        return jsonify({ 'msg':e }), 500

# 수정할 때 요청한 특정 회원정보를 클라이언트에게 넘겨준다.
@app.route('/info/<id>', methods=["GET"])
def call_info(id):
    try:
        # print(id)
        # print(db.novengers.find_one({'_id':ObjectId(id)}, {'_id':False}))
        # info = list(db.novengers.find_one({'_id':ObjectId(id)}, {'_id':False}))
        print(id)
        info = list(db.novengers.find({ '_id': ObjectId(id)}, { '_id':False }))
        # info = list(db.novengers.find_one())
        # print("111======111")
        # print(info)
        # print("222======222")
        return jsonify({ 'result':info }), 200
    except Exception as e:
        print('error message : ')
        print(e)
        return jsonify({'msg':e}), 500

if __name__ == '__main__':
    app.run('127.0.0.1', port=5003, debug=True)