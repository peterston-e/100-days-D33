import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "visionaryvoiceuk@gmail.com"
PASSWORD = "nfjt aikr deqv npla"

MY_LAT = 50.860260
MY_LONG = -0.130310


# Your position is within +5 or -5 degrees of the ISS position.
def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # ------ for testing ------- #
    # iss_latitude = MY_LAT - 4
    # iss_longitude = MY_LONG - 4

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if sunrise < time_now.hour < sunset:
        return False
    else:
        return True


while True:
    time.sleep(120)
    if iss_is_overhead() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="peterfaretra77@gmail.com",
                msg="Subject:ISS is in view\n\nLook up!"
            )

# BONUS: run the code every 60 seconds.
