from flask import Flask, render_template, request, jsonify
app = Flask(__name__)



from pymongo import MongoClient
from bson.objectid import ObjectId #ObjectId 형을 str 형으로 바꾸기 위해서는 from bson를 import ObjectId 꼭 써야한다.
client = MongoClient('mongodb+srv://sparta:test@cluster0.vxfylst.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
col = db['novengers']

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
    pw = request.form['img_pw']

    
    doc = {
        'name':name,
        'position':position,
        'self_introduce':s_i,
        'mbti':mbti,
        'comment':comment,
        'blog':blog,
        'image':image,
        'pw':pw
    }

    db.novengers.insert_one(doc)

    return jsonify({'msg': 'Save Compelete !'})
    
@app.route("/im", methods=["GET"])
def bucket_get():
    bucket_li = list(db.novengers.find({}))
    for a in bucket_li:
        a['_id']=str(a['_id'])

    return jsonify({'result': bucket_li})

@app.route("/qq", methods=["DELETE"])
def bucket_del():
    # id = request.form.get("_id_give")
    id = request.form['_id_give']
    # print("qqqqqqqqqqqqqqqqqqqqqq",id)
    id = ObjectId(id)
    db.novengers.delete_one({'_id':id})

    return jsonify({'msg': 'Member deleted successfully'})


@app.route("/ww", methods=["PUT"])
def bucket_up():
    id = request.form['_id']
    id = ObjectId(id)
    name = request.form['name']
    position = request.form['position']
    s_i = request.form['self_introduce']
    mbti = request.form['mbti']
    comment = request.form['comment']
    blog = request.form['blog']
    image = request.form['image']
    pw = request.form['pw']

    form = request.form
    for key, value in form.items():
        if key == '_id' :
            pass
        else :
            db.novengers.update_one({'_id':id},{'$set':{key:value}})


    # db.novengers.update_one({'_id':id},{'$set':{'name':name}})

    return jsonify({'msg': '업데이트 완료'})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)
