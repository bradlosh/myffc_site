#! /usr/bin/env python
import sys
import json
import requests
import xml.etree.cElementTree as ET

url = 'https://archive.org/advancedsearch.php?q=%27faith+family+church%27+%27taylors%2Csc%27&fl%5B%5D=avg_rating&fl%5B%5D=call_number&fl%5B%5D=collection&fl%5B%5D=contributor&fl%5B%5D=coverage&fl%5B%5D=creator&fl%5B%5D=date&fl%5B%5D=description&fl%5B%5D=downloads&fl%5B%5D=foldoutcount&fl%5B%5D=format&fl%5B%5D=headerImage&fl%5B%5D=identifier&fl%5B%5D=imagecount&fl%5B%5D=language&fl%5B%5D=licenseurl&fl%5B%5D=mediatype&fl%5B%5D=members&fl%5B%5D=month&fl%5B%5D=num_reviews&fl%5B%5D=oai_updatedate&fl%5B%5D=publicdate&fl%5B%5D=publisher&fl%5B%5D=reviewdate&fl%5B%5D=rights&fl%5B%5D=scanningcentre&fl%5B%5D=source&fl%5B%5D=subject&fl%5B%5D=title&fl%5B%5D=type&fl%5B%5D=volume&fl%5B%5D=week&fl%5B%5D=year&sort%5B%5D=date+desc&sort%5B%5D=&sort%5B%5D=&rows=500&page=1&output=json'
ccolumns = '"lunr","title","author","postdate","date","category","slug","icon","audiolink","tags","mp3","ogg","linkurl","ipath","layout"\n'
ccount = 0

response = requests.get(url)
json_object = response.json()
	
for collection in json_object['response']['docs']:
	ccount+=1
	print (collection['title']+' - '+collection['creator']+' - '+collection['identifier'])
	ctitle = collection['title']
	ccreator = collection['creator']
	cid = collection['identifier']
	cdatetime = collection['date']
	cdate = cdatetime.split('T')[0]
	tags = collection['subject']
	tags = [tag.lower() for tag in tags]
	for t in tags:
		print t
	if 'faith family church' in tags:
		tags.remove('faith family church')
	if 'taylors,sc' in tags:
		tags.remove('taylors,sc')
	if 'taylors, sc' in tags:
		tags.remove('taylors, sc')
	if 'taylors' in tags:
		tags.remove('taylors')
	if 'taylors sc' in tags:
		tags.remove('taylors sc')
	if 'jesus' in tags:
		tags.remove('jesus')
	if 'pastor frank jones' in tags:
		tags.remove('pastor frank jones')
	if 'rhema' in tags:
		tags.remove('rhema')
	if 'rheam' in tags:
		tags.remove('rheam')
	if 'faith' in tags:
		tags.remove('faith')
	if 'faith family church, taylors, sc' in tags:
		tags.remove('faith family church, taylors, sc')
	if 'faith family church, taylors' in tags:
		tags.remove('faith family church, taylors')
	if 'faith family church. taylors' in tags:
		tags.remove('faith family church. taylors')
	if 'brad losh' in tags:
		tags.remove('brad losh')
	if 'greenville' in tags:
		tags.remove('greenville')
	if 'hagin' in tags:
		tags.remove('hagin')
	if 'jennifer losh' in tags:
		tags.remove('jennifer losh')
	if 'pastor brad losh' in tags:
		tags.remove('pastor brad losh')
	if 'pastor frank jones' in tags:
		tags.remove('pastor frank jones')
	if 'pastor frank jone' in tags:
		tags.remove('pastor frank jone')
	if 'pastor jennifer losh' in tags:
		tags.remove('pastor jennifer losh')
	if 'pastor judi jones' in tags:
		tags.remove('pastor judi jones')
	if 'pastor roger brewer' in tags:
		tags.remove('pastor roger brewer')
	if 'rev billy barbee' in tags:
		tags.remove('rev billy barbee')
	if 'rev randall grier' in tags:
		tags.remove('rev randall grier')
	if 'rev randy grier' in tags:
		tags.remove('rev randy grier')
	if 'sc' in tags:
		tags.remove('sc')

	url = "https://archive.org/download/"+cid+"/"+cid+"_files.xml"
	print url
	mp3file = ''
	oggfile = ''
	try:
		response = requests.get(url)
		print response
		root = ET.fromstring(response.text)
		for child in root:
			cattrib = child.attrib
			filename=cattrib['name']
			if '.mp3' in filename:
				if '_vbr' in filename:
					print ""
				else:
					mp3file = filename
			if '.ogg' in filename:
				oggfile = filename
	except:
		print "could not reach file - "+cid
	columns = 'lunr,title,author,postdate,date,category,slug,icon,audiolink,tags,mp3,ogg,linkurl,ipath,layout"\n'
	nmarkdown = "---"+"\n"
	nmarkdown += 'lunr: "true"\n'
	nmarkdown += 'title: "'+ctitle+'"\n'
	nmarkdown += 'author: "'+ccreator+'"\n'
	pdate = cdate.split('-')
	pdate = pdate[1]+'-'+pdate[2]+'-'+pdate[0]
	nmarkdown += 'postDate: "'+pdate+'"\n'
	nmarkdown += 'date: '+cdate+'\n'
	nmarkdown += 'category: "sermons"'+'\n'
	slug = cdate.split('-')[0]+"/"+cdate.split('-')[1]+"/"+cid
	nmarkdown += 'slug: "'+cdate.split('-')[0]+"/"+cdate.split('-')[1]+"/"+cid+'"\n'
	nmarkdown += 'icon: microphone\n'
	nmarkdown += 'audioLink: "'+cid+'"\n'
	nmarkdown += 'tags: ['+', '.join(tags)+']\n'
	nmarkdown += 'mp3: "'+cid+'/'+mp3file+'"\n'
	nmarkdown += 'ogg: "'+cid+'/'+oggfile+'"\n'
	nmarkdown += 'linkurl: "'+url+'"\n'
	nmarkdown += 'ipath: "https://archive.org/download/'+cid+'/'+mp3file+'"\n'
	nmarkdown += 'layout: sermon.html'+'\n'
	nmarkdown += "---"
	cdata = '"true","'+ctitle+'","'+ccreator+'","'+pdate+'","'+cdate+'","sermons","'+slug+'","microphone",'+'"'+cid+'","'+'['+', '.join(tags)+']'+'","'+cid+'/'+mp3file+'","'+cid+'/'+oggfile+'","'+url+'","'+'https://archive.org/download/'+cid+'/'+mp3file+'","sermon.html"'
	print (cdata)
	ccolumns += cdata + '\n'
	
	
try:
	file= open('test.csn','w')
	file.write(ccolumns)
	file.close()
	
except:
	print('Something wrong')
	sys.exit(0)

#for avr in tree.findall("Collection"):
#	for avi in avr.getiterator():
#		print (avr.tag, avr.attrib)
