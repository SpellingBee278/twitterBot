import io
import random
import time
import urllib
import requests
import tweepy
from PIL import Image

consumer_key = 'CONSUMER_KEY/API_KEY'
consumer_secret = 'CONSUMER_SECRET/API_SECRET'

# access token and secret
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def random_line(placeNames):
    lines = open(placeNames).read().splitlines()
    return random.choice(lines)


placeName = random_line('placeNames.txt')
parsePlaceName = urllib.parse.quote(placeName)
googleMapLink = "https://www.google.co.uk/maps/search/" + parsePlaceName

splitter = placeName.split(',')
cityName = splitter[0]
countryName = splitter[1]
countryNameHashTag = "#" + countryName
cityNameHashtag = "#" + cityName
countryNameHashTagReplacement = countryNameHashTag
countryNameHashTagReplace = countryNameHashTagReplacement.replace("'", "").replace("-", "").replace(" ", "")
cityNameHashtagReplacement = cityNameHashtag
cityNameHashtagReplace = cityNameHashtagReplacement.replace("'", "").replace('-', '').replace(" ", "").replace(".", "")
language = "en"  # can be "en" or "ru"
place = cityName  # can be any city, place, street, or site, geocoder automatically selects location.
timestamp = round(time.time())  # optional timestamp, can be any unix timestamp from now, to now + three days
r = requests.get(f"https://vwapi.herokuapp.com?lang={language}&city={place}&timestamp={timestamp}")
image = Image.open(io.BytesIO(r.content))
image.save("twitter-weather.jpg")

tweet = cityName + " - " + countryName + "\n\n" + googleMapLink + "\n\n" + countryNameHashTagReplace + " " + cityNameHashtagReplace + " #randomPlaces"
print(tweet)


media = api.media_upload('twitter-weather.jpg')
tweeter = api.update_status(status=tweet, media_ids=[media.media_id])
