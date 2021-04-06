# app.py
from flask import Flask, request, jsonify, render_template
from datetime import date, datetime
app = Flask(__name__)


@app.route('/')
def index():
    today = date.today()

    print("reading")
    with open('travels.csv') as f:
        lis = [line.split() for line in f]
        for i, next_travel in enumerate(lis[1:]):
            arrival_date = datetime.strptime(next_travel[0],
                                             '%d-%m-%y').date()
            diff = arrival_date - today
            if diff.days > 0:
                break

    if diff.days > 0:
        text = f"{diff.days} days to go!"
        city = str(next_travel[2])
        arrival_time = str(next_travel[1])

    else:
        text = "No travels planned :( "
        city = 'last visit was on:'
        arrival_time = ''




    return render_template("index.html",
                           text=text,
                           city=city,
                           date=arrival_date,
                           arrival_time=arrival_time)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
