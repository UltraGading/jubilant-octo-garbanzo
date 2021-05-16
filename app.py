from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'number': u'(598)-641-3031',
        'name': u'Jungleman-1', 
        'done': False
    },
    {
        'id': 2,
        'number': u'(670)-222-7988',
        'name': u'Jungleman-2', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello gamers!!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "un gamer moment"
        },400)

    task = {
        'id': contacts[-1]['id'] + 1,
        'number': request.json['number'],
        'name': request.json.get('name', ""),
        'done': False
    }
    contacts.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)