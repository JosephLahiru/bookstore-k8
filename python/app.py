from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['bookstore']
collection = db['books']

@app.route('/books', methods=['GET'])
def get_all_books():
   books = collection.find()
   return jsonify(list(books))

# Additional routes for POST, PUT, DELETE methods go here

if __name__ == '__main__':
   app.run(debug=True)
