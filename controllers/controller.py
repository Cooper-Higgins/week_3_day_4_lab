from app import app
from flask import render_template, request
from models.event_planner import events, add_new_event
from models.event import Event

@app.route('/events')
def index():
    return render_template("index.html", event_list = events)

@app.route('/events', methods=['POST'])
def add_event():
    event_name = request.form['event_name']
    date = request.form['event_date']
    guest_num = request.form['guest_num']
    room_location = request.form['event_location']
    description = request.form['description']
    new_event = Event(event_name, date, guest_num, room_location, description)
    add_new_event(new_event)

    return render_template('index.html', event_list=events)