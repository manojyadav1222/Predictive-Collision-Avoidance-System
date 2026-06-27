import streamlit as st
from predict import predict_severity
from datetime import datetime

st.set_page_config(
    page_title="Predictive Collision Avoidance System",
    page_icon="🚗",
    layout="wide"
)
# ------------------------
# SIDEBAR
# ------------------------

st.sidebar.title("📊 Project Statistics")

st.sidebar.metric(
    "Model Accuracy",
    "86.11%"
)

st.sidebar.metric(
    "Dataset Size",
    "500K Records"
)

st.sidebar.metric(
    "Features",
    "39"
)

st.sidebar.metric(
    "Algorithm",
    "Random Forest"
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    Developed by:
    Manoj Kumar

    AIML Student
    
    """
)


st.title("🚗 Predictive Collision Avoidance System")

st.markdown(
    "Predict accident severity using weather, location and road conditions."
)

# ------------------------
# USER INPUTS
# ------------------------

col1, col2 = st.columns(2)

with col1:

    source = st.selectbox(
        "Source",
        ["Source1", "Source2", "Source3"]
    )

    state = st.selectbox(
        "State",
        ['AL','AR','AZ','CA','CO','CT','DC','DE',
         'FL','GA','IA','ID','IL','IN','KS','KY',
         'LA','MA','MD','ME','MI','MN','MO','MS',
         'MT','NC','ND','NE','NH','NJ','NM','NV',
         'NY','OH','OK','OR','PA','RI','SC','SD',
         'TN','TX','UT','VA','VT','WA','WI','WV','WY']
    )

    timezone = st.selectbox(
        "Timezone",
        [
            "US/Central",
            "US/Eastern",
            "US/Mountain",
            "US/Pacific"
        ]
    )

    latitude = st.number_input(
        "Latitude",
        value=34.0
    )

    longitude = st.number_input(
        "Longitude",
        value=-118.0
    )

    distance = st.number_input(
        "Distance (mi)",
        min_value=0.0,
        value=1.0
    )

with col2:

    temperature = st.number_input(
        "Temperature (F)",
        value=70.0
    )

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0
    )

    pressure = st.number_input(
        "Pressure (in)",
        value=30.0
    )

    visibility = st.number_input(
        "Visibility (mi)",
        value=10.0
    )

    wind_speed = st.number_input(
        "Wind Speed (mph)",
        value=5.0
    )

    precipitation = st.number_input(
        "Precipitation (in)",
        value=0.0
    )

# ------------------------
# WEATHER
# ------------------------

weather_condition = st.selectbox(
    "Weather Condition",
    [
        "Clear",
        "Cloudy",
        "Fair",
        "Fair / Windy",
        "Fog",
        "Haze",
        "Light Rain",
        "Mostly Cloudy",
        "Overcast",
        "Partly Cloudy",
        "Rain",
        "Scattered Clouds"
    ]
)

wind_direction = st.selectbox(
    "Wind Direction",
    [
        "CALM","Calm","E","ENE","ESE",
        "East","N","NE","NNE","NNW",
        "NW","North","S","SE","SSE",
        "SSW","SW","South","VAR",
        "Variable","W","WNW","WSW","West"
    ]
)

# ------------------------
# DATE TIME
# ------------------------

selected_date = st.date_input(
    "Accident Date"
)

selected_time = st.time_input(
    "Accident Time"
)

# ------------------------
# PREDICT BUTTON
# ------------------------

if st.button("Predict Severity"):

    accident_datetime = datetime.combine(
        selected_date,
        selected_time
    )

    hour = accident_datetime.hour
    month = accident_datetime.month
    day_of_week = accident_datetime.weekday()
    year = accident_datetime.year

    is_weekend = int(day_of_week >= 5)

    rush_hour = int(
        (7 <= hour <= 9) or
        (16 <= hour <= 18)
    )

    is_daytime = int(
        6 <= hour <= 18
    )

    input_data = {

        "Source": source,
        "Start_Lat": latitude,
        "Start_Lng": longitude,
        "Distance(mi)": distance,
        "State": state,
        "Timezone": timezone,

        "Temperature(F)": temperature,
        "Wind_Chill(F)": temperature,
        "Humidity(%)": humidity,
        "Pressure(in)": pressure,
        "Visibility(mi)": visibility,

        "Wind_Direction": wind_direction,
        "Wind_Speed(mph)": wind_speed,
        "Precipitation(in)": precipitation,
        "Weather_Condition": weather_condition,

        "Amenity": False,
        "Bump": False,
        "Crossing": False,
        "Give_Way": False,
        "Junction": False,
        "No_Exit": False,
        "Railway": False,
        "Roundabout": False,
        "Station": False,
        "Stop": False,
        "Traffic_Calming": False,
        "Traffic_Signal": False,

        "Sunrise_Sunset": 1,
        "Civil_Twilight": 1,
        "Nautical_Twilight": 1,
        "Astronomical_Twilight": 1,

        "Hour": hour,
        "Month": month,
        "DayOfWeek": day_of_week,
        "Year": year,

        "Is_Weekend": is_weekend,

        "Accident_Duration_Minutes": 60,

        "Is_Daytime": is_daytime,

        "Rush_Hour": rush_hour
    }
    prediction = predict_severity(input_data)

    risk_levels = {
       1: "🟢 Low Risk",
       2: "🟡 Moderate Risk",
       3: "🟠 High Risk",
       4: "🔴 Critical Risk"
    }
    recommendations = {
       1: "Road conditions appear safe.",
       2: "Exercise caution while driving.",
       3: "Reduce speed and maintain safe distance.",
       4: "High accident risk. Consider alternative routes."
    }
    st.success(f"Predicted Severity: {prediction}")
    st.info(f"Risk Level: {risk_levels[prediction]}")
    st.warning(recommendations[prediction])
