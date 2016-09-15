#! /usr/bin/env python
import sys
import json
import requests
import xml.etree.cElementTree as ET

url = 'https://archive.org/advancedsearch.php?q=%27faith+family+church%27+%27taylors%2Csc%27&fl%5B%5D=avg_rating&fl%5B%5D=call_number&fl%5B%5D=collection&fl%5B%5D=contributor&fl%5B%5D=coverage&fl%5B%5D=creator&fl%5B%5D=date&fl%5B%5D=description&fl%5B%5D=downloads&fl%5B%5D=foldoutcount&fl%5B%5D=format&fl%5B%5D=headerImage&fl%5B%5D=identifier&fl%5B%5D=imagecount&fl%5B%5D=language&fl%5B%5D=licenseurl&fl%5B%5D=mediatype&fl%5B%5D=members&fl%5B%5D=month&fl%5B%5D=num_reviews&fl%5B%5D=oai_updatedate&fl%5B%5D=publicdate&fl%5B%5D=publisher&fl%5B%5D=reviewdate&fl%5B%5D=rights&fl%5B%5D=scanningcentre&fl%5B%5D=source&fl%5B%5D=subject&fl%5B%5D=title&fl%5B%5D=type&fl%5B%5D=volume&fl%5B%5D=week&fl%5B%5D=year&sort%5B%5D=date+desc&sort%5B%5D=&sort%5B%5D=&rows=500&page=1&output=json'

response = requests.get(url)
json_object = response.json()
	
for collection in json_object['response']['docs']:
	print (collection['title']+' - '+collection['creator']+' - '+collection['identifier'])
	ctitle = collection['title']
	ccreator = collection['creator']
	cid = collection['identifier']
	cdatetime = collection['date']
	cdate = cdatetime.split('T')[0]
	tags = collection['subject']
	tags = [tag.upper() for tag in tags]
	for t in tags:
		print t
	if 'FAITH FAMILY CHURCH' in tags:
		tags.remove('FAITH FAMILY CHURCH')
	if 'TAYLORS,SC' in tags:
		tags.remove('TAYLORS,SC')
	if 'TAYLORS, SC' in tags:
		tags.remove('TAYLORS, SC')
	if 'TAYLORS' in tags:
		tags.remove('TAYLORS')
	if 'TAYLORS SC' in tags:
		tags.remove('TAYLORS SC')
	if 'JESUS' in tags:
		tags.remove('JESUS')
	if 'PASTOR FRANK JONES' in tags:
		tags.remove('PASTOR FRANK JONES')
	if 'RHEMA' in tags:
		tags.remove('RHEMA')
	if 'RHEAM' in tags:
		tags.remove('RHEAM')
	if 'FAITH FAMILY CHURCH, TAYLORS, SC' in tags:
		tags.remove('FAITH FAMILY CHURCH, TAYLORS, SC')
	if 'FAITH FAMILY CHURCH, TAYLORS' in tags:
		tags.remove('FAITH FAMILY CHURCH, TAYLORS')
	if 'FAITH FAMILY CHURCH. TAYLORS' in tags:
		tags.remove('FAITH FAMILY CHURCH. TAYLORS')
	if 'BRAD LOSH' in tags:
		tags.remove('BRAD LOSH')
	if 'GREENVILLE' in tags:
		tags.remove('GREENVILLE')
	if 'HAGIN' in tags:
		tags.remove('HAGIN')
	if 'JENNIFER LOSH' in tags:
		tags.remove('JENNIFER LOSH')
	if 'PASTOR BRAD LOSH' in tags:
		tags.remove('PASTOR BRAD LOSH')
	if 'PASTOR FRANK JONES' in tags:
		tags.remove('PASTOR FRANK JONES')
	if 'PASTOR FRANK JONE' in tags:
		tags.remove('PASTOR FRANK JONE')
	if 'PASTOR JENNIFER LOSH' in tags:
		tags.remove('PASTOR JENNIFER LOSH')
	if 'PASTOR JUDI JONES' in tags:
		tags.remove('PASTOR JUDI JONES')
	if 'PASTOR ROGER BREWER' in tags:
		tags.remove('PASTOR ROGER BREWER')
	if 'REV BILLY BARBEE' in tags:
		tags.remove('REV BILLY BARBEE')
	if 'REV RANDALL GRIER' in tags:
		tags.remove('REV RANDALL GRIER')
	if 'REV RANDY GRIER' in tags:
		tags.remove('REV RANDY GRIER')
	if 'SC' in tags:
		tags.remove('SC')

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
	
	nmarkdown = ""
	nmarkdown = "Title: "+ctitle+"\n"
	nmarkdown += "Author: "+ccreator+"\n"
	nmarkdown += "PostDate: "+cdate+"\n"
	nmarkdown += "Date: "+cdate+"\n"
	nmarkdown += "Category: Sermons"+"\n"
	nmarkdown += "Slug: "+cdate.split('-')[0]+"/"+cdate.split('-')[1]+"/"+cid+"\n"
	nmarkdown += "Icon: microphone\n"
	nmarkdown += 'AudioLink: '+cid+'\n'
	nmarkdown += 'Tags: '+', '.join(tags)+'\n'
	nmarkdown += 'mp3: '+cid+'/'+mp3file+'\n'
	nmarkdown += 'ogg: '+cid+'/'+oggfile+'\n'
	print (nmarkdown)
	try:
		file= open('content/sermons/'+cid+'.md','a')
		file.write(nmarkdown)
		file.close()
	
	except:
		print('Something wrong')
		sys.exit(0)

#for avr in tree.findall("Collection"):
#	for avi in avr.getiterator():
#		print (avr.tag, avr.attrib)
