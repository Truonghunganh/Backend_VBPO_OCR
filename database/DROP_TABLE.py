import sqlite3
path = "F:/ky2nam5/python/VBPO/API/BACKENDDATSANBONGDAPYTHON/"
namedatabase = path + "database/DangSanBongDa.db"


def executeSql(sql):
    conn = sqlite3.connect(namedatabase)
    cursor = conn.cursor()
    cursor.execute("pragma journal_mode=memory")
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("Executed SQL")


sql = "DROP TABLE User"
executeSql(sql)

sql = "DROP TABLE Shop"
executeSql(sql)
# sql = "DROP TABLE Pitch"
# executeSql(sql)
# sql = "DROP TABLE PutPitch"
# executeSql(sql)
# sql = "DROP TABLE Turnover"
# executeSql(sql)
# sql = "DROP TABLE Review"
# executeSql(sql)
# sql = "DROP TABLE ChooseShop"
# executeSql(sql)
# sql = "DROP TABLE Comment"
# executeSql(sql)
