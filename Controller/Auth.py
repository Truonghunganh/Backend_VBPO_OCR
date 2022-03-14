import jwt
import datetime
from flask_restful import  Resource,reqparse
from flask import abort, request
from  Controller.Service import Service
dk_User = reqparse.RequestParser()
dk_User.add_argument('phone', type=str, required=True, default=None)
dk_User.add_argument('password', type=str, required=True, default=None)

class Login(Resource):
    'log out '
    def get(self):
        token = request.headers.get('token')
        user = Service.checkToken(token)
        if user is None:
            abort(401, 'token not found')
        data=("1",user["id"])
        sql = "UPDATE User SET token=? WHERE id=?"
        Service.executeSqlHasData(sql, data)
        return{"message ": "Log out successfully"}
    'log in'
    def post(self):
        data = request.json        
        dk_User.parse_args()
        sdt=data['phone']
        user=Service.getUserByPhone(sdt)
        if len(user) == 0:
            abort(401, "bạn nhập số điện thoại sai")
        else:        
            try:
                key=Service.getPassword(Service.getData("select password from user where phone='"+sdt+"'")[0][0])
                if key==data["password"]:
                    user['exp']=datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=10)
                    token = jwt.encode(user, key)
                    data=(token,user['id'])
                    sql = "UPDATE User SET token =? where id=?"
                    Service.executeSqlHasData(sql, data)
                    user['token'] = token
                    user['exp']=str(user['exp'])
                    return Service.getJsonSuccess("data",user)
                else:
                    abort(401,"mật khẩu sai")
            except Exception as e:
                abort(404, 'mật khẩu sai')



        # data = request.json        
        # dk_User.parse_args()
        # sdt=data['phone']
        # sql="SELECT token from User where phone='"+sdt+"'"
        # users=Service.getData(sql)
        # if len(users) == 0:
        #     abort(401, "bạn nhập số điện thoại sai")
        # else:        
        #     try:
        #         dataJson=jwt.decode(users[0][0], data["password"], algorithms="HS256")
        #         dataJson["token"]=users[0][0]
        #         return Service.getJsonSuccess("user", dataJson)
        #     except Exception as e:
        #         abort(401, 'mật khẩu sai')
class CheckToken(Resource):
    def get(self):
        print(request.headers.get('token'))
        user = Service.checkToken(request.headers.get('token'))
        if user is None:
            abort(401,"mật khẩu sai")
        success=Service.getJsonSuccess("user",user)
        return success
        
class Register(Resource):
    def post(self):
        data=request.json
        