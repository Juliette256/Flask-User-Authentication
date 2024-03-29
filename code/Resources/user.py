
import sqlite3
from flask_restful import Resource, reqparse

from Models.user_model import UserModel

class RegisterUser(Resource):
 parser=reqparse.RequestParser()
 parser.add_argument('username', type=str, required=True, help="Can not be empty")
 parser.add_argument('password', type=str, required=True, help="Can not be empty")
    
 def post(self):
     data=RegisterUser.parser.parse_args()
     if UserModel.find_by_username(data['username']):
         return {"message":"User already exists"},400

     user=UserModel(**data)
     user.save_to_db()
     return {"message":"User created successfully"},201
