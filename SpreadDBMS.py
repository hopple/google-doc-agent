import gdata.spreadsheet.service
import gdata.spreadsheet.text_db

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

    def existDB(self, name):
        """
        check if the database is exist given the database name.
        """

    def getDB(self, name):
        """
        get the database object.
        """
        database = self.client.GetDatabases(name = name)[0]
        return database

    def createTable(self, db, name, schema):
        """
        create a table given the database, table name, and the list of schema.
        """
        table = db.CreateTable(name, schema)
        return table

    def existTable(self, db, name):
        """
        check if the table is exist given the table name.
        """

    def getTable(self, db, name):
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


