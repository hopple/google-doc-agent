import getpass
import smtplib
import json
import urllib2
import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#a wrapper of the gdata text_db.
class DBMS:
    """
    Simple dbms for managing the google spreadsheet based database.
    """

    def __init__(self, username,password):
        self.client = gdata.spreadsheet.text_db.DatabaseClient(username=username, password=password)

    def createDB(self, name):
        """
        to create a database.
        """
        database = self.client.CreateDatabase(name) 
        return database

    def getDB(self, name):
        """
        get the database object.
        """
        if not self.client.GetDatabases(name = name):
            return None
        else:
            database = self.client.GetDatabases(name = name)[0]
            return database

    def createTable(self, db, name, schema):
        """
        create a table given the database, table name, and the list of schema.
        """
        table = db.CreateTable(name, schema)
        return table

    def getTable(self, db, name):
        if not db.GetTables(name = name):
            return None 
        else:
            table = db.GetTables(name = name)[0]
            return table

    def insertRow(self, table, row):
        """
        insert a dict given the table, the row should be the dict.
        """
        record = table.AddRecord(row)
        return record

    def getRow(self, table, rowNumber):
        """
        get the row with specific row number.
        """
        row = table.GetRecord(row_number=rowNumber)
        return row

    def getRows(self, start, end):
        """
        get the rows between the start and end rows.
        """
        rows = table.GetRecords(start, end)
        return rows

    def updateRow(self, row):
        row.Push()


url_ip = "http://api.externalip.net/ip" #web site for detecting ip
url_ip_detail = "http://api.hostip.info/get_json.php" #more details of ip associated info

def getIP():
    """
    get the ip address using the web api
    """
    ip = urllib2.urlopen(url_ip).read()
    return ip


def getIPDetail():
    """
    get the ip details including contry, city, ip
    """
    raw = urllib2.urlopen(url_ip_detail).read()
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

def recordMyIP():
	contry, city, ip = getIPDetail()
	username = raw_input("Enter your username: ")
	pw = getpass.getpass()
	dbms = DBMS(username, pw)
	db = dbms.getDB('sysinfo')
	if not db:
		db = dbms.createDB('sysinfo')
	table = dbms.getTable(db, 'ip-table')
	if not table:
		schema = ["contry", "city", "ip"]
		table = dbms.createTable(db, 'ip-table', schema)
	row = {}
	row['contry'] = contry
	row['city'] = city
	row['ip'] = ip
	row = dbms.insertRow(table, row)



