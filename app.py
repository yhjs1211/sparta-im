from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
<<<<<<< HEAD
client = MongoClient('mongodb+srv://sparta:test@cluster0.vxfylst.mongodb.net/?retryWrites=true&w=majority')
=======

mongo_key = '<put your key here>'
client = MongoClient(mongo_key)
>>>>>>> 22da8d8a59343d5c53951e5fb425b3f3e2099de6
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
    
@app.route("/im", methods=["GET"])
def bucket_get():
    bucket_li = list(db.novengers.find({},{'_id':False}))

    return jsonify({'result': bucket_li})

if __name__ == '__main__':
<<<<<<< HEAD
    app.run('127.0.0.1', port=5001, debug=True)
=======
    app.run('127.0.0.1', port=5003, debug=True)
>>>>>>> 22da8d8a59343d5c53951e5fb425b3f3e2099de6
