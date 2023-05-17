from bson.objectid import ObjectId
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

mongo_Key = 'mongodb+srv://sparta:test@cluster0.goswrtc.mongodb.net/?retryWrites=true&w=majority'

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.goswrtc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    try:
        return render_template('index.html'),200 #render_template() > flask에서 제공하는 함수로 templates에 저장된 html을 불러올 때 사용한다.
    except Exception as e:
        print(e)
        return jsonify({'msg':e}),500 #flask에 내장되어 있는 기능으로 jsonify() 모듈을 사용하여 JSON 데이터 전달
    

#Create
@app.route("/im", methods=["POST"])
def bucket_post():
    try:
        name = request.form['name_give']
        position = request.form['po_give']
        s_i = request.form['s_i_give']
        mbti = request.form['mbti_give']
        comment = request.form['comment_give']
        blog = request.form['blog_give']
        img = request.form['img_give']

        
        doc = {
            'name':name,
            'position':position,
            'self_introduce':s_i,
            'mbti':mbti,
            'comment':comment,
            'blog':blog,
            'image':img
        }

        db.novengers.insert_one(doc)

        return jsonify({'msg': 'Save Compelete !'}),200
    except Exception as e:
        print(e)
        return jsonify({'msg:e'}),500
#Update
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
        img = request.form['img_give']

        # print("post_id:")
        # print(post_id)

        # print("===================")
        # for i in request.form.keys():
        #     print(i + ':' + request.form[i])

        filiter = {'_id:ObjectId(post_id)'}

        doc = {
            'name':name,
            'position':position,
            'self_introduce':s_i,
            'mbti':mbti,
            'comment':comment,
            'blog':blog,
            'image':img
        }

        for i in doc.keys():
            new_value = {"$set":{i:doc[i]}}
            db.novengers.update_one(filter, new_value)

        # new_value = {"$set":{'position':"181818"}}
        # db.novengers.update_one(filter, new_value)
        return jsonify({'msg':'수정이 완료되었습니다.'}),200
    except Exception as e:
        print(e)
        return jsonify({'msg':e}), 500


#Read
@app.route("/im", methods=["GET"])
def bucket_get():
    bucket_li = list(db.novengers.find({},{'_id':False}))
    return jsonify({'result': bucket_li})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)