import requests
from bs4 import BeautifulSoup
from ImgDir.imgDown import downloadWebImg

#last used on 8 June 2016
#Note: the class used on website may change later(after 8 june).But if it doesnt ,it will work


def downloadWallpapers(oUrl):
    url = oUrl                     	#gets the webpage url
    sourceCode = requests.get(url)	#gets the source code of visited page
    plainText = sourceCode.text		#gathers plain text
    soup = BeautifulSoup(plainText)	#creates a set of objects eg. div,a,li,etc.
    for link in soup.findAll('a', {'class':'image'}):	#finds the a(links) with respective class
        href = link.get('href')				# gets href
        projectImg(str(url)+str(href))			# used to open particular project on webpage

def projectImg(oUrl):
    url = oUrl                      	#gets the webpage url
    sourceCode = requests.get(url)	#gets the source code of visited page
    plainText = sourceCode.text		#gathers plain text
    soup = BeautifulSoup(plainText)	#creates a set of objects eg. div,a,li,etc.
    for div in soup.findAll('div', {'class': 'project-media-block'}):		#finds the div with respective class
        for img in div.findAll():						#gets all info in <img> tag
            src = img.get('src')						#gets src from img tag
            downloadWebImg( str(src))						#used to download the image

downloadWallpapers('http://www.justinmaller.com/')
