# app.py
from flask import Flask, request, jsonify
from datetime import date
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # retrieve name from URL parameters
    name = requests.args
    print(f" got name {name}")
    response = {
        "name": f"Welcome {name}"
    }

    return jsonify(response)

@app.route('/post/', methods=['POST'])
def posting_something():
    param = requests.form.get('name')
    print(param)

    if param:
        return jsonify({
            "Message": f"Welcome {name}",
            "METHOD": 'POST'
        })

@app.route('/')
def index():
    today = date.today()
    next_visit = date(2021, 5, 22)
    diff = next_visit - today
    print(diff)
    print(diff.days)
    return f"<h1> Only {diff.days} to go! </h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)




