import string
import pickle
import urllib2
import re

def level_0():
	print 2 ** 38

def level_1_1():
	origin = "g fmnc wms bgblr rpylqjyrc gr zw fylb. \
	rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq \
	glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle \
	 qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."  
	code = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")  
	translated = origin.translate(code)
	print translated
	print "map".translate(code)

def translate(origin, code_map):  
    t = ""  
    for c in origin:  
        if c in string.ascii_lowercase:  
            t += code_map.get(c)  
        else:  
            t += c  
    return t  

def level_1_2():
	ascii = string.ascii_lowercase  
	code = "cdefghijklmnopqrstuvwxyzab"  
	code_map = {}  
	for i in range(26):
		code_map[ascii[i]] = code[i]
	print translate(origin, code_map)
	print translate("map", code_map)  

def level_2():
	html = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()  
	b = html.find("\n%%")  
	html = html[b:]  
	print "".join(re.findall("[a-zA-Z]", html))

def level_3():
	html = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()  
	b = html.find("\n<!--")  
	html = html[b:]  
	print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", html))  

def level_4(startNumber):
	url_string = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
	nothing = startNumber
	count = 1
	while True:
		try:
			response = urllib2.urlopen(url_string % nothing).read()
			print str(count) + "  " +response
			count += 1
			nothing = re.search(r'and the next nothing is (\d+)', response).group(1)
		except:
			break

def level_5():
	f = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
	raw = pickle.load(f)
	f.close()
	print '\n'.join([''.join([letter*number for letter,number in row]) for row in raw])
