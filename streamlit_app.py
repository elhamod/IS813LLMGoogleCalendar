import streamlit as st
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr, Sept
import json
from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from google.oauth2 import service_account
from beautiful_date import Jan, Apr, Sept


credentials = service_account.Credentials.from_service_account_info(
        json.loads(st.secrets["MYJSON"]),
        scopes=["https://www.googleapis.com/auth/calendar"]
    )


calendar = GoogleCalendar(credentials=credentials)
# for cal in calendar.get_calendar_list():
#   print(cal)
# event = Event(
#     'Breakfast',
#     start=(25 / Sept / 2024)[9:00],
#     end=(25 / Sept / 2024)[10:00],
# )

# calendar.add_event(event)
c = list(calendar.get_events(calendar_id="mndhamod@gmail.com"))
# print(c)
for event in c:
    st.write(event)


# calendar = GoogleCalendar('mndhamod@gmail.com', credentials_path='client_secret_959719549897-5rocqlvu26t7gur3ods0gjdn4kagcl9g.apps.googleusercontent.com.json', open_browser=False,  authentication_flow_port=8502)
# # event = Event() #
# #     'Breakfast',
# #     start=(1 / Sep / 2019)[9:00],
# #     recurrence=[
# #         Recurrence.rule(freq=DAILY),
# #     ]
# # )

# # calendar.add_event(event)

# for event in calendar:
#     st.write(event)
