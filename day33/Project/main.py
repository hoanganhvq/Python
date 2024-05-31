import requests
from datetime import datetime
import smtplib

MY_LATE = 10.015618
MY_LONG = 105.754619
MY_EMAIL = "phananhvq223@gmail.com"
MY_PASSWORD = "Hoanganh@1"
#Get the position of ISS
def iss_posittion_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if MY_LATE-5 <=iss_latitude <=MY_LATE+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True

#Get your position
def is_night():

    parameter = {
        "lat": MY_LATE,
        "lng": MY_LONG,
        "formatted": 0
    }

    reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    data = reponse.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >=sunset and time_now <=sunrise:
        return True

if is_night() and iss_posittion_overhead():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: Look Up \n\n The ISS is above you in the sky"
    )


