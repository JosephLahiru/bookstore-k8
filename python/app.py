from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['bookstore']
collection = db['books']

@app.route('/', methods=['GET'])
def index():
   return "Hello, I am Online!!!"

@app.route('/books', methods=['GET'])
def get_all_books():
   books = collection.find()
   return jsonify(list(books))

@app.route('/add-book', methods=['POST'])
def add_book():
   book = request.get_json()
   collection.insert_one(book)
   return jsonify(book), 201

if __name__ == '__main__':
   app.run(debug=True)
