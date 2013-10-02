import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from urllib import urlopen

url_ip = "http://api.externalip.net/ip"

def getIP():
    """
    get the ip address using the web api
    """
    ip = urlopen(url_ip).read()
    return ip

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

