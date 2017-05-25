from lxml.html import parse
import json

dlist = []
it = 1
ito = 0
itc = 0
doc = "" 
currlink = []
doc1 = ""

def moveforward(url):
	nextlink = ""
	for link1 in doc.cssselect('PLACE_THE_CSS_TAGS_YOU_WANT_TO_RETRIEVE'):
		nextlink = link1.get('href')
	
	if nextlink=="" :
		return 

	dupl = 1
	for check in currlink:
		if nextlink == check :
			dupl = 0
			break	
	
	if dupl == 1 :
		iterate(nextlink)


def execute(url):
	init(url)
	operations()
	

def iterate(url):
	global currlink
	currlink.append(url)
	execute(url)
	moveforward(url)
	

def init(url):
	global doc
	doc = parse(url).getroot()
	doc.make_links_absolute()
	
def operations():
	pass

def result(file):
	global dlist
	print dlist
	json.dump(dlist, open(file,'w'))
	

def allclear():
	global dlist
	global it
	global ito
	global itc
	global doc
	global currlink
	dlist[:] = []
	currlink[:] = []
	it = 1
	ito = 0
	itc = 0
	doc = "" 