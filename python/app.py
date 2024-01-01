from flask import Flask, jsonify, request
from pymongo import MongoClient, InsertOne
import json

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['bookstore']
collection = db['books']

books_json = """
[{"isbn":"0596159900","title":"Head First HTML and CSS","year":2012,"price":26.78,"page":768,"category":"IT","coverPhoto":"images/head.first.html.and.css.png","publisher":{"id":1,"name":"O'Reilly"},"author":{"identityNo":"5","firstName":"Stoyan","lastName":"Stefanov"}},
  {"isbn":"978-1449369279","title":"WebSocket","year":2015,"price":23.99,"page":144,"category":"IT","coverPhoto":"images/websocket.jpg","publisher":{"id":1,"name":"O'Reilly"},"author":{"identityNo":"1","firstName":"Andrew","lastName":"Lombardi"}},
  {"isbn":"Mastering JavaScript Design Patterns","title":"1783987987","year":2014,"price":40.49,"page":290,"category":"IT","coverPhoto":"images/mastering.javascript.design.patterns.jpg","publisher":{"id":4,"name":"Packt"},"author":{"identityNo":"8","firstName":"Simon","lastName":"Timms"}},
  {"isbn":"CSS3: The Missing Manual","title":"1449325947","year":2013,"price":28.48,"page":650,"category":"IT","coverPhoto":"images/css3.missing.manual.png","publisher":{"id":1,"name":"O'Reilly"},"author":{"identityNo":"6","firstName":"Stoyan","lastName":"Stefanov"}},
  {"isbn":"0596806752","title":"JavaScript Patterns","year":2010,"price":20.78,"page":236,"category":"IT","coverPhoto":"images/javascript.patterns.jpg","publisher":{"id":1,"name":"O'Reilly"},"author":{"identityNo":"4","firstName":"Stoyan","lastName":"Stefanov"}},
  {"isbn":"978-0441172719","title":"Dune","year":1990,"price":16.68,"page":896,"category":"Science Fiction","coverPhoto":"images/dune.jpg","publisher":{"id":2,"name":"Ace"},"author":{"identityNo":"2","firstName":"Frank","lastName":"Herbert"}},
  {"isbn":"1430263881","title":"Pro jQuery 2.0","year":2013,"price":56.99,"page":1044,"category":"IT","coverPhoto":"images/pro.jquery.2.png","publisher":{"id":1,"name":"O'Reilly"},"author":{"identityNo":"7","firstName":"Stoyan","lastName":"Stefanov"}},
  {"isbn":"978-1617291999","title":"Java 8 in Action","year":2014,"price":37.28,"page":424,"category":"IT","coverPhoto":"images/java-8-in-action.jpg","publisher":{"id":3,"name":"Manning Publication"},"author":{"identityNo":"3","firstName":"Andrew","lastName":"Lombardi"}},
  {"isbn":"978-0345391803","title":"The Hitchhiker's Guide to the Galaxy","year":1995,"price":11.41,"page":224,"category":"Science Fiction","coverPhoto":"images/the.hitchhikers.guide.to.the.galaxy.jpg","publisher":{"id":5,"name":"Del Rey"},"author":{"identityNo":"9","firstName":"Douglas","lastName":"Adams"}}]
"""
books = json.loads(books_json)

requests = [InsertOne(book) for book in books]

collection.bulk_write(requests)

@app.route('/', methods=['GET'])
def index():
  return "Hello, I am Online!!!"

@app.route('/books', methods=['GET'])
def get_all_books():
  books = collection.find()
  return jsonify(list(books))

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
  book = collection.find_one({'_id': book_id})
  return jsonify(book)

@app.route('/add-book', methods=['POST'])
def add_book():
  book = request.get_json()
  collection.insert_one(book)
  return jsonify(book), 201

@app.route('/update-book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
  book = request.get_json()
  collection.update_one({'_id': book_id}, {'$set': book})
  return jsonify(book)

@app.route('/delete-book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
  collection.delete_one({'_id': book_id})
  return '', 204

if __name__ == '__main__':
  app.run(debug=True)
