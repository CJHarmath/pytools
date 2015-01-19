import sys
import os
import re
from subprocess import call

def processLinks(fileName):
	file = open(fileName,'r')
	links = file.readlines()
	file.close()

	for link in links:
		link = link.replace('\n','')
		if (isUrl(link)):
			downloadMp3(link)
		else:
			print '%s does not seem to be a valid url starting with http(s)://' % (link)

#def checkAndInstallPackage(package):
#	res = !dpkg -s $package | grep Status
#	if res.grep('install ok installed') != None:

def downloadMp3(link):
	call(["youtube-dl", "--extract-audio", "--audio-format", "mp3", link])

def isUrl(input):
	if re.match('http[s]?://.*', input):
		return True
	else:
		return False

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	if len(argv) < 2:
		print >>sys.stderr, 'needs an input file with the youtube links'
		return 2
   
	#checkAndInstallPackage(youtube-dl)
	fileName = argv[1]
	if os.path.exists(fileName):
		processLinks(fileName)
	elif isUrl(fileName):
		downloadMp3(fileName)
	else:
		print >>sys.stderr,'input must be a link or a file containing links'



if __name__ == "__main__":
	sys.exit(main())


