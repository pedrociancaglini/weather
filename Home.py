import streamlit as st
import requests

# Function to get weather data
def get_weather(city_name):
    base_url = f"https://wttr.in/{city_name}?format=j1"
    
    # Sending the GET request
    response = requests.get(base_url)
    
    # Extracting data in JSON format
    data = response.json()
    
    # Parse the weather data
    if response.status_code == 200:
        current_condition = data['current_condition'][0]
        
        # Storing data in variables
        temperature = current_condition["temp_C"]
        humidity = current_condition["humidity"]
        weather_description = current_condition["weatherDesc"][0]["value"]
        wind_speed = current_condition["windspeedKmph"]
        
        # Return the data
        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": weather_description,
            "wind_speed": wind_speed,
        }
    else:
        return None

# Streamlit app
def main():
    st.title("Weather App")
    st.write("Get the current weather for Buenos Aires, Argentina")

    # City name input (predefined to Buenos Aires)
    city_name = "Buenos Aires"

    # Get weather data
    weather_data = get_weather(city_name)

    # Display the weather inside an expander
    with st.expander(f"Weather Details for {city_name}"):
        if weather_data:
            st.write(f"**Temperature:** {weather_data['temperature']} °C")
            st.write(f"**Humidity:** {weather_data['humidity']} %")
            st.write(f"**Weather Description:** {weather_data['description']}")
            st.write(f"**Wind Speed:** {weather_data['wind_speed']} km/h")
        else:
            st.write("City not found, or there was an error with the API request.")

if __name__ == "__main__":
    main()
