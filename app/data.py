from datetime import datetime
from app.models import Event

event1 = Event()
event1.name = "HackJam"
event1.location = "The Woz, Soda Hall"
event1.sponsor = "Hackers@Berkeley"
event1.latitude = 37.8757435
event1.longitude = -122.2587323
event1.description = "Awesome Hackathon" 
event1.food = "Cheeseboard"
event1.start_time = datetime.datetime(2013, 9, 28, 11, 00)
event1.end_time = datetime.datetime(2013, 9, 29, 1, 00)


event2 = Event()
event2.name = "Berkeley MFE Info Session"
event2.location = "The Woz, Soda Hall"
event2.sponsor = "Master of Financial Engineering Program"
event2.latitude = 37.8715012
event2.longitude = -122.2538014
event2.description = "Information session and Q&A: resume review, discussion of finance career paths.  Lunch Served"
event2.food = "Lunch"
event2.start_time = datetime.datetime(2013, 10, 3, 13, 00)
event2.end_time = datetime.datetime(2013, 10, 4, 14, 00)


event3 = Event()
event3.name = "Tech Talk: Dropbox"
event3.location = "The Woz, Soda Hall"
event3.sponsor = "Dropbox"
event3.latitude = 37.8757435
event3.longitude = -122.2587323
event3.description = "At Dropbox we like to say that Dropbox 'just works.' It means you, the user, don't have to think about how to use it or worry about weird bugs or edge cases. But it takes a lot of engineering to get there, especially when you have 200 million users! Come hear Dropbox engineer Alex Allain take you behind the scenes of some of the bugs we've run into at Dropbox scale and how we build robust systems. Join us for free food, shirts and Dropbox storage!"
event3.food = "Free Food"
event3.start_time = datetime.datetime(2013, 10, 2, 18, 00)
event3.end_time = datetime.datetime(2013, 10, 2, 19, 00)


event4 = Event()
event4.name = "Info Session: EA"
event4.location = "The Woz, Soda Hall"
event4.sponsor = "EA"
event4.latitude = 37.8757435
event4.longitude = -122.2587323
event4.description = "Join us to learn more about new grad and internship roles, and to find out why its such a great time to be part of our world. Enjoy great food and swap your resume for a raffle ticket to win cool swag."
event4.food = "Great Food"
event4.start_time = datetime.datetime(2013, 10, 2, 18, 00)
event4.end_time = datetime.datetime(2013, 10, 2, 19, 30)


event5 = Event()
event5.name = "Info Session: National Instruments"
event5.location = "The Woz, Soda Hall"
event5.sponsor = "National Instruments"
event5.latitude = 37.8757435
event5.longitude = -122.2587323
event5.description = "Please join us for food and refreshments, and learn more about the exciting career opportunities at National Instruments!"
event5.food = "Food and Refreshments"
event5.start_time = datetime.datetime(2013, 10, 3, 18, 00)
event5.end_time = datetime.datetime(2013, 10, 3, 19, 00)

event6 = Event()
event6.name = "Undergrad Social Hour"
event6.location = "Cory Hall, 2nd Floor Courtyard"
event6.sponsor = "EECS Department"
event6.latitude = 37.8750793 
event6.longitude = -122.257581
event6.description = "UG Social Hour 10/08 with Special Guest Speaker Professor Jan Rabaey."
event6.food = "Food and Refreshments"
event6.start_time = datetime.datetime(2013, 10, 8, 15, 30)
event6.end_time = datetime.datetime(2013, 10, 8, 16, 30)

event7 = Event()
event7.name = "Kaffee Klatsch"
event7.location = "German Department Library, Dwinelle Hall"
event7.sponsor = "German Department"
event7.latitude = 37.8707856 
event7.longitude = -122.2605146
event7.description = "Come speak German and enjoy coffee and treats at the German Coffee Hour"
event7.food = "Coffee and Refreshments"
event7.start_time = datetime.datetime(2013, 10, 2, 11, 30)
event7.end_time = datetime.datetime(2013, 10, 2, 12, 30)

event_list = [event1, event2, event3, event4, event5, event6, event7]
