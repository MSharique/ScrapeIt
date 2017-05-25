# This is a main driver file. it will accept the URL and the mode of retrieving data 
# from the webpage.

# Scrape file contains the main data retrieving logic.
from Scrape import *
import os

# createDir will create a new directory in the current folder so that data retrived 
# can be placed in the correct folder.
def createDir(name):
	newpath = name 
	if not os.path.exists(newpath):
		os.makedirs(newpath)

#InputURL contains the name of the parent link of the webapp.
inputurl = '<PLACE_YOUR_URL_HERE>'

# doc2 will parse the input URL and make all links absolute such that it can avoid 
# the exceptions which might occur in the given URL. doc is present in the Scrape.py. 
doc2 = parse(inputurl).getroot()
doc2.make_links_absolute()

# dsub is a dictionary which will stores all the hyperlinks present in the inputurl 
# webpage. It will store the value of anchor tag as key and the corresponding 
# link as value in the dictionary.
dsub = {}

# Since we are using CSS-Select, we will place the css/html tag which we want to
# search in the given webpage.
for link in doc2.cssselect('<PLACE_THE_CSS_TAGS_YOU_WANT_TO_RETRIEVE>'):
	# cnt is a temporary variable which will stores the content for the searched tag
	cnt = link.text_content()
	# we can get any value from our selected tag with the help of HTML attributes or 
	# any other value present in the selected tag. 
	# Here is an example of retrieving URL from anchor<a> tag 
	href = link.get('href')
	if href != "#":	#Ignoring invalid URLs
		dsub[cnt] = href


# Creating a directory to store the retrieved data in a JSON format. 
for key,val in dsub.items():
	createDir('Retrieved/'+key)
	iterate(val)
	file = '/data.json'
	file = 'Retrieved/'+key + file
	result(file)
	allclear()
