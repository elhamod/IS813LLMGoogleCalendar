import streamlit as st
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr, Sept


calendar = GoogleCalendar('mndhamod@gmail.com', credentials_path='client_secret_959719549897-5rocqlvu26t7gur3ods0gjdn4kagcl9g.apps.googleusercontent.com.json', open_browser=False,  authentication_flow_port=8502)
# event = Event() #
#     'Breakfast',
#     start=(1 / Sep / 2019)[9:00],
#     recurrence=[
#         Recurrence.rule(freq=DAILY),
#     ]
# )

# calendar.add_event(event)

for event in calendar:
    st.write(event)
