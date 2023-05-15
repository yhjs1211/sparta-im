from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.goswrtc.mongodb.net/?retryWrites=true&w=majority')
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

    return jsonify({'msg': 'Save Compelete !'})
    
@app.route("/im", methods=["GET"])
def bucket_get():
    bucket_li = list(db.buckets.find({},{'_id':False}))

    return jsonify({'bucket_li': bucket_li})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)