import smtplib
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from urllib import urlopen

url_ip = "http://api.externalip.net/ip"
url_ip_detail = "http://api.hostip.info/get_json.php"

def getIP():
    """
    get the ip address using the web api
    """
    ip = urlopen(url_ip).read()
    return ip


def getIPDetail():
    """
    get the ip details including contry, city, ip
    """
    raw = urlopen(url_ip_detail).read()
    raw = json.loads(raw)
    contry = raw["country_name"]
    city = raw["city"]
    ip = raw["ip"]
    return contry, city, ip
    

def sendEmail(from_addr, to_addr_list, cc_addr_list,
        subject, message, username, password,
        smtpserver='smtp.gmail.com:587'):
    """
    send a mail.
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ','.join(to_addr_list)
    msg['Cc'] = ','.join(cc_addr_list)
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtpserver)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    text = msg.as_string()
    problems = server.sendmail(from_addr, to_addr_list, text)
    server.quit()
    return problems

