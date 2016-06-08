import urllib.request
import random

def downloadWebImg(url):
    name = random.randrange(1,1000)						#generates a number in 1 to 1000
    fullName = str(name) + ".jpg"						#generates a name with .jpg extension for downloaded image
    urllib.request.urlretrieve(url,fullName)					#downloads image,fullName can be used as the path of file


