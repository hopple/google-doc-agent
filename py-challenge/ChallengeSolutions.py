import string
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