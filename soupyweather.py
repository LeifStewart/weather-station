import requests
from bs4 import BeautifulSoup
from datetime import datetime
import datetime
import time
now=datetime.datetime.now()
url = "https://forecast.weather.gov/MapClick.php?lat=39.6127&lon=-105.0162"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
while True:
    #scan the current temperature area of website
    current_temp = soup.find(class_="myforecast-current-lrg")

    # look at the 7 day prediction and copy the data
    forecast_items = soup.find_all(class_="tombstone-container")

    today_high = None
    today_low = None

    # extra double check
    found_high = False
    found_low = False

    # Iterate through the forecast items to find today's high and low
    for forecast in forecast_items:
        temp = forecast.find(class_="temp")

        if temp:
            temp_text = temp.text.strip()

            # Capture first high temperature
            if "High" in temp_text and not found_high:
                today_high = temp_text
                found_high = True  # get rid of all the extra useless daily highs for other days.

            # Capture first low temperature
            elif "Low" in temp_text and not found_low:
                today_low = temp_text
                found_low = True  # Stop after finding the first low

            # Stop searching once both high and low are found
            if found_high and found_low:
                break

    # print all temps
    if current_temp:
        print(f"Current Temperature: {current_temp.text}")

    if today_high:
        print(f"Today's High: {today_high}")

    if today_low:
        print(f"Tonight's Low: {today_low}")
    skibidi = [current_temp.text,today_high,today_low]
    file=open("weather.txt","a")
    file.write(str(skibidi)+str(now)+"\n")
    file.close
    time.sleep(3600)
