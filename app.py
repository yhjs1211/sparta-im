from bson import ObjectId
from flask import Flask, redirect, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={
    r"/im/*":{"origin":"*"}
})

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.x2zlpmf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

# 멤버

@app.route("/members")
def render_member():
    return render_template('member.html')
    
@app.route("/members/list", methods=["GET"])
def novengerse_get():
    member_li = list(db.novengers.find({}))
    
    for a in member_li:
        a['_id']=str(a['_id'])

    return jsonify({'member_li': member_li})

@app.route("/members", methods=["POST"])
def novengerse_post():
    doc = {}
    
    if('_id' in request.form):
        
        # ID 유효성 2차 검사 ( DB 상에 존재하는 ID값인지 아닌지 )
        chk = db.novengers.find_one({'_id':ObjectId(request.form['_id'])})
        
        if(chk is not None):
            # delete 일 경우
            if(len(request.form)==1):
                db.novengers.delete_one({'_id':ObjectId(request.form['_id'])})
                return jsonify({'msg':"삭제되었습니다."})
            else:
                for k in request.form.keys():
                    if(k!='_id'):
                        db.novengers.update_one({'_id':ObjectId(request.form['_id'])},
                                                {'$set':{k:request.form[k]}}
                            )
        else:
            return jsonify({'msg':"존재하지 않는 ID입니다."})
        msg = "업데이트 완료"
        return jsonify({'msg':msg})
    else:
        for k in request.form.keys():
            doc[k]=request.form[k]
        db.novengers.insert_one(doc)
        _id = str(db.novengers.find_one({'name':request.form['name']})['_id'])
        return jsonify({'msg': '고유 ID는'+_id+' 입니다.'})

# 방명록

@app.route("/board")
def render_board():
    return render_template("board.html")

@app.route("/board", methods=["POST"])
def create_visitBook():
    doc={}
    for i in request.form.keys():
        doc[i]=request.form[i]

    db.visitBooks.insert_one(doc)

    return jsonify({'msg':"방명록이 생성되었습니다."})
    
@app.route("/board", methods=["DELETE"])
def delete_visitBook():
    password = request.form['password']
    print(password)    
    chk = db.visitBooks.find_one({'password':password})
    print(chk)
    if(chk is not None):
        db.visitBooks.delete_one({'password':password})
        return jsonify({'msg':"삭제되었습니다."})
    else:
        return jsonify({'msg':"비밀번호를 확인해주세요"})

@app.route("/board/list", methods=["GET"])
def visitBook_get():
    visitBook_li = list(db.visitBooks.find({}))
    
    for a in visitBook_li:
        a['_id']=str(a['_id'])[18:24]
    return jsonify({'visitBook_li': visitBook_li})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5001, debug=True)

    
