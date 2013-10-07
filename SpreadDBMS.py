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


