import random
import urllib
import tweepy


# api key and secret
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
countryNameHashTag = "#" + countryName.replace(" ", "")
cityNameHashtag = "#" + cityName.replace(" ", "")

tweet = cityName + " - " + countryName + "\n\n" + googleMapLink + "\n\n" + countryNameHashTag + " " + cityNameHashtag + " #randomPlaces"
print(tweet)
# tweet out the tweet
tweeter = api.update_status(status=tweet)
