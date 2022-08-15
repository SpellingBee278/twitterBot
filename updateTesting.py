import random
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
something = cityNameHashtagReplacement.replace("'", "").replace('-', '').replace(" ")

tweet = cityName + " - " + countryName + "\n\n" + googleMapLink + "\n\n" + countryNameHashTag + " " + something + " #randomPlaces"
print(tweet)
