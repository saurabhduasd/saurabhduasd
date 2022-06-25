import requests

api_key = "b2629e25730246ff520eda354ac7ee11"  # The API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
print(complete_url)
response = requests.get(complete_url)
x = response.json()
temp_celcius=0

if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]
    z = x["weather"]
    temp_celcius = round(current_temperature-273.15,2)
    weather_description = z[0]["description"]

    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
                    "\n Temperature in Celcius = " + str(temp_celcius) +
                     "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")

if temp_celcius > 29 or temp_celcius < 19:
    print('Stay inside')
else:
    print('Have fun outdoors')
