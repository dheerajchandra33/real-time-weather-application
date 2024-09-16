import requests

def get_weather_data(city, api_key):
    """Fetch weather data for a given city using OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather_info(weather_data):
    """Display weather information from the weather data."""
    if weather_data:
        if weather_data.get('cod') == 200:
            city = weather_data['name']
            weather = weather_data['weather'][0]['main']
            description = weather_data['weather'][0]['description']
            temp = round(weather_data['main']['temp'])
            humidity = weather_data['main']['humidity']
            pressure = weather_data['main']['pressure']
            
            print(f"The weather in {city} is: {weather} ({description})")
            print(f"The temperature in {city} is: {temp}ºF")
            print(f"Humidity: {humidity}%")
            print(f"Pressure: {pressure} hPa")
        else:
            print("No City Found or other API error.")
    else:
        print("Failed to retrieve weather data.")

def main():
    api_key = '30d4741c779ba94c470ca1f63045390a'
    user_input = input("Enter city: ").strip()

    if not user_input:
        print("No city entered. Please try again.")
    else:
        weather_data = get_weather_data(user_input, api_key)
        display_weather_info(weather_data)

if _name_ == "_main_":
    main()
