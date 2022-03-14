import random
import base64
import uuid
import jwt
import datetime
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


def executeSqlHasData(sql, data):
    conn = sqlite3.connect(namedatabase)
    cursor = conn.cursor()
    cursor.execute("pragma journal_mode=memory")
    cursor.execute(sql, data)
    conn.commit()
    conn.close()
    print("Executed SQL")


def executeSql(sql):
    conn = sqlite3.connect(namedatabase)
    cursor = conn.cursor()
    cursor.execute("pragma journal_mode=memory")
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("Executed SQL")


'user'
diachis = ["quảng nam", "đà nẵng", "Huế", "quảng Bình", "quảng Trị", "quảng Ngãi",
           "phú yên", "Bình định", "Nha Trang ", "khánh hòa", "hồ chí minh"]
phones = ["0374894100", "0374894101", "0374894102", "0374894103", "0374894104",
          "0374894105", "0374894106", "0374894107", "0374894108", "0374894109", "0374894110"]
tens = ["trương ngọc hào", "ngô trí đạt", "nguyễn hoàng", "đinh văn Huy", "nguyễn hoàng Huy",
        "phậm đình điệp", "nguyễn hoàng Phi", "nguyễn đình trường", "trần anh thư", "ngô thị thúy hiền", "nguyễn thái học"]
for i in range(11):
    id = str(uuid.uuid1())
    print(id)
    password = str(
        base64.b64encode(phones[i].encode("utf-8"))).split("'")[1]
    data = (id, "user", True, tens[i], phones[i], phones[i] +
            "gmail.com", diachis[i], password, datetime.datetime.now())
    sql = "INSERT INTO User(id,role,status,name,phone,gmail,address,password,Create_time) VALUES (?,?,? ,?,?,? ,?,?,?)"
    executeSqlHasData(sql, data)
    user = {
        'id': id,
        'role': 'user',
        'trangthai': True,
        "name": tens[i],
        "phone": phones[i],
        "gmail": phones[i]+"gmail.com",
        "address": diachis[i],
        'exp': datetime.datetime.now()
    }

    token = jwt.encode(user, phones[i], algorithm="HS256")
    sql = "UPDATE User SET token='"+token+"' WHERE id='"+id+"'"
    executeSql(sql)
print("thành công")

"innkeeper"
# diachis=["quảng nam","đà nẵng","Huế","quảng Bình","quảng Trị","quảng Ngãi",
#     "phú yên","Bình định","Nha Trang ","khánh hòa","hồ chí minh"];
# phones=["0812250590", "0354658717", "0337265910","0356899335" ,"0356899336","0787179937","0935291246"];
# tens=["Trương Hùng Anh", "Vỏ Dức Hùng Sơn", "Nguyễn Thái Quyên","Trương Ngọc Hào","Trương Ánh Diệu", "Trương Phú Một","Trần Thị Lệ Hương"];
# for i in range(7):
#     id=str(uuid.uuid1())
#     password=str(
#         base64.b64encode(phones[i].encode("utf-8"))).split("'")[1]
#     data=(id,"innkeeper",True,tens[i],phones[i],phones[i]+"gmail.com",diachis[i],password,datetime.datetime.now())
#     sql = "INSERT INTO User(id,role,status,name,phone,gmail,address,password,Create_time) VALUES (?,?,? ,?,?,? ,?,?,?)"
#     executeSqlHasData(sql, data)
#     user={
#         'id': id,
#         'role': "innkeeper",
#         'trangthai': True,
#         "name":tens[i],
#         "phone": phones[i],
#         "gmail": phones[i]+"gmail.com",
#         "address":diachis[i]
#     }
#     token = jwt.encode(user, phones[i], algorithm="HS256")
#     sql = "UPDATE User SET token='"+token+"' WHERE id='"+id+"'"
#     executeSql(sql)
# print("thành công")


'admin'
# id=str(uuid.uuid1())
# phone="0919257806"
# ten="Đỗ Thị Minh Thúy"
# password=str(
#     base64.b64encode(phone.encode("utf-8"))).split("'")[1]
# data=(id,'admin',True,ten,phone,phone+"gmail.com","Đà Nẵng",password,datetime.datetime.now())
# sql = "INSERT INTO User(id,role,status,name,phone,gmail,address,password,Create_time) VALUES (?,?,? ,?,?,? ,?,?,?)"
# executeSqlHasData(sql, data)
# user={
#     'id': id,
#     'role': 'admin',
#     'trangthai': True,
#     "name":ten,
#     "phone": phone,
#     "gmail": phone+"gmail.com",
#     "address":"Đà Nẵng"
# }
# token = jwt.encode(user, phone, algorithm="HS256")
# sql = "UPDATE User SET token='"+token+"' WHERE id='"+id+"'"
# executeSql(sql)
# print("thành công")


'quán'
# sql="delete from Shop"
# executeSql(sql)
# names = ["Khu Bóng Đá Thủy Lợi", "Sân bóng đá Phương Tuấn-Hội An", "Sân vận động Hội An"
#     ,"Sân vận động Cẩm Châu", "Sân Bóng Đá Cỏ Tự Nhiên"];
# images = ['image/Quan/a.jpg', 'image/Quan/b.jpg', 'image/Quan/c.jpg', 'image/Quan/d.jpg', 'image/Quan/e.jpg'];
# diachis = ["24 Phan Bá Phiến, Tân An, Hội An, Quảng Nam", "02B Thái Phiên, Phường Minh An, Hội An, Quảng Nam 560000, Việt Nam", "18 Lý Thường Kiệt, Sơn Phong, Hội An, Quảng Nam, Việt Nam",
#     "Cẩm Châu, Hội An, Quảng Nam, Việt Nam", "168 Nguyễn Trãi, Tây Lộc, Thành phố Huế, Thừa Thiên Huế, Việt Nam"];
# phones = ["0374894200", "0374894201", "0374894202", "0374894203", "0374894204"];

# linkaddress = [
#     "https://www.google.com/maps/place/24+Phan+Bá+Phiến,+Tân+An,+Hội+An,+Quảng+Nam,+Việt+Nam/@15.8777916,108.3194347,17z/data=!4m13!1m7!3m6!1s0x31420e70f774b22f:0x9481a7e45e60d5c1!2zMjQgUGhhbiBCw6EgUGhp4bq_biwgVMOibiBBbiwgSOG7mWkgQW4sIFF14bqjbmcgTmFtLCBWaeG7h3QgTmFt!3b1!8m2!3d15.8871269!4d108.3241001!3m4!1s0x31420e70f774b22f:0x9481a7e45e60d5c1!8m2!3d15.8871269!4d108.3241001?hl=vi-VN",
#     "https://www.google.com/maps/place/Sân+bóng+đá+Phương+Tuấn-Hội+An/@15.881449,108.3268398,17z/data=!4m13!1m7!3m6!1s0x31420e791a6930ff:0x18f239fe251c1720!2zMiBUaMOhaSBQaGnDqm4sIFBoxrDhu51uZyBNaW5oIEFuLCBI4buZaSBBbiwgUXXhuqNuZyBOYW0sIFZp4buHdCBOYW0!3b1!8m2!3d15.8814439!4d108.3290285!3m4!1s0x0:0x8792a03837874555!8m2!3d15.8811413!4d108.3314402?hl=vi-VN",
#     "https://www.google.com/maps/place/Sân+vận+động+Hội+An/@15.881449,108.3268398,17z/data=!4m13!1m7!3m6!1s0x31420e791a6930ff:0x18f239fe251c1720!2zMiBUaMOhaSBQaGnDqm4sIFBoxrDhu51uZyBNaW5oIEFuLCBI4buZaSBBbiwgUXXhuqNuZyBOYW0sIFZp4buHdCBOYW0!3b1!8m2!3d15.8814439!4d108.3290285!3m4!1s0x31420e78f76c34bf:0xfd515cbe1ce08065!8m2!3d15.8818761!4d108.3308107?hl=vi-VN",
#     "https://www.google.com/maps/place/Sân+vận+động+Cẩm+Châu,+Cẩm+Châu,+Hội+An,+Quảng+Nam,+Việt+Nam/@15.8816799,108.3425788,17z/data=!4m13!1m7!3m6!1s0x31420e791a6930ff:0x18f239fe251c1720!2zMiBUaMOhaSBQaGnDqm4sIFBoxrDhu51uZyBNaW5oIEFuLCBI4buZaSBBbiwgUXXhuqNuZyBOYW0sIFZp4buHdCBOYW0!3b1!8m2!3d15.8814439!4d108.3290285!3m4!1s0x31420dd04ee838e7:0x30b2fe82d10b9b07!8m2!3d15.8817063!4d108.3428624?hl=vi-VN",
#     "https://www.google.com/maps/place/Sân+Bóng+Đá+Cỏ+Tự+Nhiên/@16.4724469,107.5684767,17z/data=!4m8!1m2!2m1!1zc8OibiBiw7NuZyDhu58gSHXhur8!3m4!1s0x0:0xbbb0edcac33334b1!8m2!3d16.4734158!4d107.5682927?hl=vi-VN"

# ];
# vidos=[15.8871269, 15.8811413, 15.8818761, 15.8817063, 16.4734158];
# kinhdos = [108.3241001, 108.3314402, 108.3308107, 108.3428624, 107.5682927];


# sql = "SELECT id FROM User where role='innkeeper'"
# users=getData(sql)
# print(users[0][0])

# for i in range(5):
#     data=(str(uuid.uuid1()),names[i],images[i],diachis[i],linkaddress[i],vidos[i],kinhdos[i],True,datetime.datetime.now(),0,users[i][0])
#     sql="insert into Shop(id,name,image,address,linkaddress,latitude,longitude,status,Create_time,review,id_user) values(?,?,?,? ,?,?,?,? ,?,?,?)"
#     executeSqlHasData(sql, data)


'sân'
# sql="delete from Pitch"
# executeSql(sql)
# tiens5=[130000,140000, 150000, 160000];
# tiens11 = [300000, 310000, 320000, 330000];
# tiens7= [200000, 210000, 220000, 230000];
# sql="SELECT id FROM Shop"
# datas=getData(sql)
# print (datas)
# print (random.randint(0,3))
# for i in datas :
#     data = (str(uuid.uuid1()),"Sân A",11,True,tiens11[random.randint(0,3)],datetime.datetime.now(),i[0]);
#     sql="insert into Pitch(id,name,numberpeople,status,priceperhour,Create_time,id_shop) values(?,?,?,?, ?,?,?)"
#     executeSqlHasData(sql, data)
#     data = (str(uuid.uuid1()),"Sân B",5,True,tiens5[random.randint(0,3)],datetime.datetime.now(),i[0]);
#     sql="insert into Pitch(id,name,numberpeople,status,priceperhour,Create_time,id_shop) values(?,?,?,?, ?,?,?)"
#     executeSqlHasData(sql, data)
#     data = (str(uuid.uuid1()),"Sân C",7,True,tiens7[random.randint(0,3)],datetime.datetime.now(),i[0]);
#     sql="insert into Pitch(id,name,numberpeople,status,priceperhour,Create_time,id_shop) values(?,?,?,?, ?,?,?)"
#     executeSqlHasData(sql, data)
