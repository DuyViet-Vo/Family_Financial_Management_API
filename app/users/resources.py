from flask import request
from users.models import User
from config import db
from users.schemas import user_schema
from flask_restful import Resource
from flask_jwt_extended import jwt_required, create_access_token
from datetime import timedelta

class UserResource(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        
        # Kiểm tra xem email đã tồn tại trong cơ sở dữ liệu hay chưa
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {'message': 'Email already exists'}, 400
        
        # Nếu email chưa tồn tại, thêm người dùng mới vào cơ sở dữ liệu
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201

class LoginResource(Resource):
    def post(self):
        # Login user
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        user = User.query.filter_by(email=email).first()

        if not user or not user.check_password(password):
            return {'message': 'Invalid username or password'}, 401
        
        # Create access token
        access_token = create_access_token(identity=email, expires_delta=timedelta(minutes=60))
        return {'access_token': access_token}, 200