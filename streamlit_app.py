import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr, Sept


calendar = GoogleCalendar('mndhamod@gmail.com', credentials_path='client_secret_959719549897-dpj0rcr0bbic4v2vqnbheiliu341l1pn.apps.googleusercontent.com.json', open_browser=False)
# event = Event(
#     'Breakfast',
#     start=(1 / Sep / 2019)[9:00],
#     recurrence=[
#         Recurrence.rule(freq=DAILY),
#     ]
# )

# calendar.add_event(event)

for event in calendar:
    st.write(event)
