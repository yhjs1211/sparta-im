from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb+srv://sparta:test@cluster0.vxfylst.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta
col = db['novengers']

id = "6461f59eb73cfb478042bce6"
id = ObjectId(id)
db.novengers.delete_one({'_id':id})

