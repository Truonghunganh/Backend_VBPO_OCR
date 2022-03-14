from operator import le
import numpy as np
import jwt
import base64
import sqlite3
namedatabase = "F:/ky2nam5/python/VBPO/BVPO_web_api/Backend_VBPO_OCR/database/OCR_db.db"
class Service:
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
    'khi mà chưa commit  thì cơ sở dữ liệu không thây đổi'
    def executeSqlsHasDatas(sqls,sqlsnodatas, datas):
        conn = sqlite3.connect(namedatabase)
        cursor = conn.cursor()
        cursor.execute("pragma journal_mode=memory")
        # cursor.execute("BEGIN TRANSACTION")
        for sql in sqlsnodatas:
            cursor.execute(sql)
        for i in range(len(datas)):
            cursor.execute(sqls[i], datas[i])
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
    def get1TruongListJson(truong,dulieu):
        datas=[]
        for dl in dulieu:
            data={}
            for i in range(len(dl)):
                data[truong]=dl[i]
            datas.append(data)
        return datas
    def getListJson(truong,dulieu):
        datas=[]
        for dl in dulieu:
            data={}
            for i in range(len(dl)):
                data[truong[i]]=dl[i]
            datas.append(data)
        return datas
    def getJson(truong,dulieu):
        data={}
        for i in range(len(truong)):
            data[truong[i]]=dulieu[i]
        return data 
    def getJsonSuccess(truong,dulieu):
        datas={}
        datas["status"]=True
        datas["code"]=200
        datas[truong]=dulieu
        return datas
    def getListJsonSuccess(truongs,dulieus):
        datas={}
        datas["status"]=True
        datas["code"]=200
        for i in range(len(truongs)):
            datas[truongs[i]]=dulieus[i]
        return datas
        return datas
    def getPassword(password):
        return str(base64.b64decode(password)).split("'")[1]
        

    def checkToken(token):
        try:
            sql="SELECT password FROM User where token='"+token+"'"
            data=Service.getData(sql)
            key=Service.getPassword(data[0][0])
            if len(data):
                return jwt.decode(token, key, algorithms="HS256")
            return None
        except:
            return None
    def getUserByToken(token):
            sql="SELECT id,role,status,name,phone,gmail,address,Create_time FROM User where token='"+token+"'"
            data=Service.getData(sql)
            if len(data)==0:
                return None
            truong=["id","role","status","name","phone","gmail","address","Create_time"]
            return Service.getJson(truong,data[0])
    def getUserByToken(token):
            sql="SELECT id,role,status,name,phone,gmail,address,Create_time FROM User where token='"+token+"'"
            data=Service.getData(sql)
            if len(data)==0:
                return None
            truong=["id","role","status","name","phone","gmail","address","Create_time"]
            return Service.getJson(truong,data[0])

    def getUserByPhone(phone):
            sql="SELECT id,role,status,name,phone,gmail,address,Create_time FROM User where phone='"+phone+"'"
            data=Service.getData(sql)
            if len(data)==0:
                return None
            truong=["id","role","status","name","phone","gmail","address","Create_time"]
            return Service.getJson(truong,data[0])
