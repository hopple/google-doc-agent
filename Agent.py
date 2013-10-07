import getpass
from Utilities import getIPDetail
from SpreadDBMS import DBMS

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





