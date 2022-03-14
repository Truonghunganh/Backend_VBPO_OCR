from operator import ge
import sqlite3
namedatabase = "F:/ky2nam5/python/VBPO/BVPO_web_api/Backend_VBPO_OCR/database/OCR_db.db"

def getData(sql):
    conn = sqlite3.connect(namedatabase)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data

# sql="select * from Shop where status=1"
# datas=getData(sql)
# print( datas)
# sql="select * from Pitch"
# datas=getData(sql)
# print( datas)

# sql="select distinct s.id,u.phone from Shop s,User u where u.id=s.id_user"
# sql="select distinct s.id,s.name,s.image,s.address,s.linkaddress,s.latitude,s.longitude,s.status,s.Create_time,s.review,s.id_user,u.phone from Shop s,User u where s.id_user=u.id and s.status=1" 
# datas=getData(sql)
# print( datas)


# sql="select * from PutPitch"
# datas=getData(sql)
# print( datas)

sql="select * from User"
datas=getData(sql)
print( datas)
