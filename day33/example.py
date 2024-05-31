# import requests
#
# response = requests.get("http://api.open-notify.org/iss-now.json")
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_location = (longitude,latitude)
# print(iss_location)

import requests
import datetime
MY_LATE = 10.015618
MY_LONG = 105.754619

parameter = {
    "lat": MY_LATE,
    "lng": MY_LONG,
    "formatted": 0
}

reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
reponse.raise_for_status()
data = reponse.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(datetime.datetime.now().hour)