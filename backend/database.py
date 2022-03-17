
#TINYDB!
from tinydb import TinyDB, Query, where


db = TinyDB('.\database\db.json')

# #create table
usertable=db.table("usertable")
# usertable.insert({"key":"value", "key2":4})

# #clear table
# db.drop_table("usertable")

# #get list of tables
# db.tables()

# #clear the database
# db.truncate()

#hashing function for secure passwords



# #insert
# db.insert({"key":"value", "key2":4})

# no duplicate insert
def uniqueInsert(db,data):
    query = Query()
    if db.search(query.fragment(data)) == []:
        id = db.insert(data)
        return "no duplicates found, inserted record successfully, heres your id " +str(id)
    else:
        return "value already exists"


#nested insert
# db.insert({"key":"value","nestedkey":{"key2":4,"key3":3}})

# #delete
# query=Query()
# db.remove(query.key2 > 3)

# #update values
# query=Query()
# db.update({'key2':10},query.key2==4)

# #print whole database
# print(db.all())

# # OR ITERATIVE APPROACH
# for item in db:
#     print(item)

# #searching for items
# query=Query()
# print(db.search(query.key2=="value"))
# print(db.search(query.key2 > 3))
# # no query object
# db.search(where('key2') == 4)

# #existance of key
# print(db.search(where('nestedkey1').exists()))

# # nested search
# print(db.search(query.nestedkey.key2==4))
# #OR
# print(db.search(query['nestedkey'].key2==4))









########################################################################



#SQLLITE3 CODE
# from multiprocessing.sharedctypes import Value
# import sqlite3
# import pandas as pd
# class Table:
#     def __init__(self,database,tableName):
#         self.database = database
#         self.tableName = tableName
#         try:
#             queryString = "SELECT name FROM sqlite_master WHERE type='table' AND name='" + self.tableName + "';"
#             results = self.database.cursor.execute(queryString).fetchall()
#             # if results == []:
#             #     raise ValueError
#         except:
#             raise ValueError

#     def insertRecord(self,record):
#         #inserts a single record into table.
#         try:
#             queryString = "INSERT INTO " + str(self.tableName) + " VALUES ("
#             for item in record:
#                 queryString += "'" + item + "', "
            
#             queryString = queryString[:-2] + ")"
#             x = self.database.connection.execute(queryString)
#             self.database.connection.commit()

#             return x

#         except Exception as e:
#             raise ValueError

#     def runQuery(self,query):
#         #takes a query and returns the results if it selects
#         try:
#             x= self.database.connection.execute(query).fetchall()
#             self.database.connection.commit()
#             return x
#         except Exception as e:
#             raise ValueError
    
#     def prettyPrint(self,query):
#         #takes a query and returns a pretty table
#         try:
#             conn = self.database.connection
#             return print(pd.read_sql_query(query, conn))
#         except Exception as e:
#             raise ValueError





# class Database:

#     def __init__(self,databaseFile):
#         try:
#             self.databaseFile = databaseFile
#             self.connection = sqlite3.connect(self.databaseFile,check_same_thread=False)
#             self.cursor = self.connection.cursor()
#         except Exception as e:
#             raise FileNotFoundError

#     def createTable(self, tableName, columnKeyPairs):
#         #creates a table with tablename and keypairs for the column name: column data type
#         try:
#             queryString = 'CREATE TABLE ' + str(tableName) + '('
            
#             for key,value in columnKeyPairs.items():
#                 queryString += key + ' ' + value + ', '

#             queryString = queryString[:-2] + ');'

#             self.cursor.execute(queryString)
#             self.connection.commit()
#             return True
#         except:
#             raise ValueError
    
#     def selectTable(self,tableName):
#         #creates a table object using the database and tablename
#         try:
#             return Table(self,tableName)
#         except:
#             raise ValueError
    
#     def checkIfTableExists(self,tableName):
#         try:
#             c = self.cursor.execute(f" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{tableName}' ")
#     #if the count is 1, then table exists
#             if c.fetchone()[0]!=1:
#                 return False
#             else:
#                 return True 
#         except:
#             raise ValueError

#     def dropTable(self, tableName):
#         #deletes table tablename
#         try:
#             queryString = "DROP TABLE " + str(tableName) + ";"
#             self.cursor.execute(queryString)
#             self.connection.commit()
#             return True
#         except:
#             raise ValueError

# #database initialization:
# def initializeDatabase():
#     database = Database('.\\database\\database.db')
#     tableName="usertable"
#     #database.dropTable(tableName)
#     testColumns={"username":'text',"password":'text'}
    
#     if not database.checkIfTableExists(tableName):
#         print("creating table")
#         database.createTable(tableName,testColumns)
#     table = database.selectTable(tableName)
#     return table
# table1=initializeDatabase()

# # database = Database('.\\database\\test.db')
# # tableName="testTable2"
# # testColumns={"textColumn":'text',"integerColumn":'integer',"realColumn":'real',"blobColumn":'blob',"booleanColumn":'integer'}
# # database.createTable(tableName,testColumns)
# # table1 = database.selectTable(tableName)
# # # print(database.cursor.execute((f"PRAGMA table_info({tableName})")).fetchall())
# # # #print (table1.database.schema)
# # # #table1.execute(query).fetchall()

