import random
import requests
import time
from PIL import Image
import io
import urllib.parse


def random_line(placeNames):
    lines = open(placeNames).read().splitlines()
    return random.choice(lines)


placeName = random_line('placeNames.txt')
parsePlaceName = urllib.parse.quote(placeName)
googleMapLink = "https://www.google.co.uk/maps/search/" + parsePlaceName

splitter = placeName.split(',')
cityName = splitter[0]
countryName = splitter[1]
countryNameHashTag = "#" + countryName.replace(" ", "")
cityNameHashtag = "#" + cityName.replace(" ", "")
cityNameHashtagReplacement = cityNameHashtag
something = cityNameHashtagReplacement.replace("'", "").replace('-', '').replace(" ", "")

language = "en"  # can be "en" or "ru"
place = cityName  # can be any city, place, street, or site, geocoder automatically selects location.
timestamp = round(time.time())  # optional timestamp, can be any unix timestamp from now, to now + three days
r = requests.get(f"https://vwapi.herokuapp.com?lang={language}&city={place}&timestamp={timestamp}")
image = Image.open(io.BytesIO(r.content))
image.show()

tweet = cityName + " - " + countryName + "\n\n" + googleMapLink + "\n\n" + countryNameHashTag + " " + something + " #randomPlaces"
print(tweet)



