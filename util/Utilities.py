from urllib import urlopen

url_ip = "http://api.externalip.net/ip"

def getIP():
    """
    get the ip address using the web api
    """
    ip = urlopen(url_ip).read()
    return ip
