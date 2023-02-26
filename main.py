from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/books", methods=["GET"])
def book_index():
    return jsonify({
        "books": "books",
        "titles": [
            "hello",
            "world",
            "biggie"
        ]
    })

@app.route("/books", methods=["POST"])
def book_create():
    #Create a new book
    pass

@app.route("/books/<int:id>", methods=["GET"])
def book_show(id):
    #Return a single book
    pass

@app.route("/books/<int:id>", methods=["PUT", "PATCH"])
def book_update(id):
    #Update a book
    pass

@app.route("/books/<int:id>", methods=["DELETE"])
def book_delete(id):
    #Delete a book
    pass

@app.route("/")
def home_page():
    return "This will be my landing page for my website/portfolio site"

@app.route('/contact')
def contact_page():
    return "contact page"