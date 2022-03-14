import sqlite3
namedatabase = "F:/ky2nam5/python/VBPO/BVPO_web_api/Backend_VBPO_OCR/database/OCR_db.db"


def executeSql(sql):
    conn = sqlite3.connect(namedatabase)
    cursor = conn.cursor()
    cursor.execute("pragma journal_mode=memory")
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("Executed SQL")


# sql = "DROP TABLE User"
# executeSql(sql)


sql = '''CREATE TABLE User(
   id nvarchar PRIMARY KEY ,
   role         nvarchar NOT NULL,
   status   BOOLEAN  NOT NULL,
   name         nvarchar NOT NULL,
   phone         nvarchar NOT NULL,
   gmail        nvarchar NOT NULL,
   address        nvarchar NOT NULL,
   password     varchar,
   Create_time    timestamp,
   token    nvarchar 
);'''
executeSql(sql)
sql = "CREATE UNIQUE INDEX phone ON User(phone)"
executeSql(sql)
