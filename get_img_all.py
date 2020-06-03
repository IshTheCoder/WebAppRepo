import requests
from PIL import Image
# python2.x, use this instead  
# from StringIO import StringIO
# for python3.x,
from io import StringIO
from io import BytesIO
from skimage import io
import urllib.request
import io  # Note: io.BytesIO is StringIO.StringIO on Python2.
import requests

# import urllib
# resource = urllib.urlopen("https://nba-players.herokuapp.com/players/Harden/James")
# output = open("file01.jpg","wb")
# output.write(resource.read())
# output.close()



def get_img(fname, lastname):
	image_url = "https://nba-players.herokuapp.com/players/" + lastname +"/" + fname


	# response = requests.get(string)
	# file = open("sample_image.png", "wb")
	# file.write(response.content)
	# file.close()
	#i = Image.open(StringIO(r.content))
	#i.show()




	fml = urllib.request.urlretrieve(image_url, "assets" + "/" + fname +lastname+ '.png')





	# img_data = requests.get(image_url, stream = True).content
	# image = Image.open(img_data)

	# with open(fname + lastname + ".png", 'wb') as handler:
	# 	handler.write(img_data)







	#print(requests.get(string, stream=True).raw)


	#im = Image.open(requests.get(string, stream=True).raw)

	return None




print(get_img("kemba","walker"))