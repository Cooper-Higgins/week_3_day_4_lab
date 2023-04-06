from models.event import *
import datetime

event1 = Event("Pub Thursday", datetime.date(2023, 5, 13), 15, "Howlin Wolf Main Bar", "Raucous Thursday at the Wolf")
event2 = Event("Egg Hunt", datetime.date(2023, 4, 6), 3, "Clockwise Lobby", "Beth on the Hunt")
event3 = Event("Pancake Afternoon", datetime.date(2023, 7, 9), 20, "Kitchen", "Steph's pancake afternoon")
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)