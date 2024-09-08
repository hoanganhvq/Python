import requests
import smtplib
my_email = "anhphan42891@gmail.com"
password = "xyrx nycf zgez gclw"
MY_LATE = 10.012857
MY_LONG = 105.755524
api_key = "0240fd27b861c9953b829b6edd210f82"
parameter = {
    "lat" : MY_LATE,
    "lon" : MY_LONG,
    "appid" : "0240fd27b861c9953b829b6edd210f82",
    "cnt" : 4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameter)
response.raise_for_status()
weather_data = response.json()
# id = weather_data["list"][0]["weather"][0]["id"]
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="anhphan42891@gmail.com", msg="Bring Umbrella")
    connection.close()


