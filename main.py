from email import message
from pip._vendor import requests
# need to instsall package
# can send an email instead
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "b52dd2142d0d1a1bc21a27603162cf10" 
ACCOUNT_SID = ""
AUTH_TOKEN = ""
LAT = 35
LONG = 35

weather_params = {
    "lat" : 32.779167,
    "lon" : -96.808891, 
    "appid" : API_KEY,
    "exclude" : "current,minutely,daily"
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body = "it's going to rain today. bring an umbrella", 
            # would theoretically include the phone number from the twilio acccount here
            from = "", 
            to = ""
        )
# weather_data["hourly"][0]["weather"][0]["id"]