import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def get_img(firstname, lastname):
	image_url = "https://nba-players.herokuapp.com/players/" + lastname +"/" + firstname
	fml = urllib.request.urlretrieve(image_url, "assets" + "/" + firstname +lastname+ '.png')
	# print(fml)
	return None
# print(get_img("kemba","walker"))