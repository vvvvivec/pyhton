# NOTE , THIS FUCKING SCRIPT IS BROKEN , I GUESS THE API IS ABANDONED?
# weather.py
# Gets weather data based on city

# Import weather Package
from weather import Weather

# Get a weather object
weather = Weather()

# Lookup weather via location name
# Fuck WOEID queries
location = weather.lookup_by_location('jacksonville')
condition = location.condition()

# Get weather forecasts for upcoming days
forecasts = location.forecast()
for forecast in forecasts:
    print(forecasts.text())
    print(forecasts.date())
    print(forecasts.high())
    print(forecasts.low())
