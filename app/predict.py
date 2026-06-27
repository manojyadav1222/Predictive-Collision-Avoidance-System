import pandas as pd
import joblib

model = joblib.load("models/random_forest_model.pkl")
encoders = joblib.load("models/encoders.pkl")


def predict_severity(input_data):

    input_df = pd.DataFrame([input_data])

    categorical_cols = [
        "Source",
        "State",
        "Timezone",
        "Wind_Direction",
        "Weather_Condition"
    ]

    for col in categorical_cols:
        input_df[col] = encoders[col].transform(
            input_df[col]
        )

    input_df = input_df[[
        'Source', 'Start_Lat', 'Start_Lng', 'Distance(mi)', 'State',
        'Timezone', 'Temperature(F)', 'Wind_Chill(F)', 'Humidity(%)',
        'Pressure(in)', 'Visibility(mi)', 'Wind_Direction',
        'Wind_Speed(mph)', 'Precipitation(in)', 'Weather_Condition',
        'Amenity', 'Bump', 'Crossing', 'Give_Way', 'Junction',
        'No_Exit', 'Railway', 'Roundabout', 'Station', 'Stop',
        'Traffic_Calming', 'Traffic_Signal', 'Sunrise_Sunset',
        'Civil_Twilight', 'Nautical_Twilight',
        'Astronomical_Twilight', 'Hour', 'Month',
        'DayOfWeek', 'Year', 'Is_Weekend',
        'Accident_Duration_Minutes', 'Is_Daytime',
        'Rush_Hour'
    ]]

    prediction = model.predict(input_df)

    return prediction[0]