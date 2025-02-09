import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Punjab Kings',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals',
 'Gujarat Titans',
 'Lucknow Super Giants']

venues = [
    'M Chinnaswamy Stadium,Bengaluru', 'Punjab Cricket Association Stadium, Mohali',
    'Arun Jaitley Stadium, Delhi', 'Wankhede Stadium, Mumbai', 'Eden Gardens, Kolkata',
    'Sawai Mansingh Stadium', 'Rajiv Gandhi International Stadium',
    'MA Chidambaram Stadium, Chepauk, Chennai', 'Dr DY Patil Sports Academy',
    'Newlands', "St George's Park", 'Kingsmead', 'SuperSport Park', 'Buffalo Park',
    'New Wanderers Stadium', 'De Beers Diamond Oval', 'OUTsurance Oval', 'Brabourne Stadium',
    'Sardar Patel Stadium, Motera', 'Barabati Stadium', 'Brabourne Stadium, Mumbai',
    'Vidarbha Cricket Association Stadium, Jamtha', 'Himachal Pradesh Cricket Association Stadium',
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Subrata Roy Sahara Stadium',
    'Shaheed Veer Narayan Singh International Stadium', 'JSCA International Stadium Complex',
    'Sheikh Zayed Stadium', 'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
    'Maharashtra Cricket Association Stadium', 'Holkar Cricket Stadium',
    'Narendra Modi Stadium, Ahmedabad', 'Zayed Cricket Stadium, Abu Dhabi',
    'Dr DY Patil Sports Academy, Mumbai', 'Maharashtra Cricket Association Stadium, Pune',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
    'Barsapara Cricket Stadium, Guwahati', 'Sawai Mansingh Stadium, Jaipur',
    'Himachal Pradesh Cricket Association Stadium, Dharamsala',
    'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur',
    'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam'
]

pipe = pickle.load(open('ipl.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_venue = st.selectbox('Select Venue',sorted(venues))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'venue':[selected_venue],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")