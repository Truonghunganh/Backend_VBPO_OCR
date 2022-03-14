from flask_restful import  Resource,reqparse
from flask import abort, request
import cv2
import uuid
import datetime
from Controller.Service import Service

class Ocr(Resource):
    def post(self):
        token=request.headers.get("token")
        user=Service.checkToken(token)
        if user == None:
            abort(401,"token not found")
        if user["role"]=="user":
            lineimg= "static/VBPO/image/"+str(user["id"])+".jpg" 
            img = request.files["img"]
            img.save(lineimg)
            img=cv2.imread(lineimg)
            listdata=[["226","953","438","1358"]]
            for item in listdata:
                cv2.rectangle(img, (int(item[0]), int(item[1])),
                            (int(item[2]), int(item[3])), (0, 255, 0), 5)
            cv2.imwrite(lineimg, img)
            return Service.getJsonSuccess("data", lineimg)

    