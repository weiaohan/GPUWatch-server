import jwt, datetime, time
import login
from flask import jsonify
from app.users.model import Users


class Auth():
    @staticmethod
    def encode_auth_token(user_email, user_name):
        try:
            header = {
                "typ": "jwt",
                "alg": "HS265"
            }

            payload = {
                "iss": "GPU Watcher",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=0, minutes=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                "email": user_email,
                "name": user_name
            }

            signature = jwt.encode(payload, "this_is_my_secret", algorithm='HS256')
            return signature
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, "this_is_my_secret", options={'verify_exp': False})
            if payload:
                return payload
            else:
                raise jwt.InvalidTokenError
 
        except jwt.ExpiredSignatureError:
            return 'Token过期'
 
        except jwt.InvalidTokenError:
            return '无效Token'
    
    def identify(self, request):
        """
        用户鉴权
        :return: list
        """
        try:
            auth_token = jwt.decode(request.headers.get('Authorization'), "this_is_my_secret" algorithms='HS256')
            if auth_token:
                if not auth_token or auth_token['headers']['typ'] != 'JWT':
                    s = '请传递正确的验证头信息'
                else:
                    user = login.find_user(auth_token['payload']['email'])
                    if user is None:
                        s = '找不到该用户信息'
                    else:
                        s = '登陆成功'
 
                return s
        except jwt.ExpiredSignatureError:
            s = 'Token已过期'
            return s
 
        except jwt.InvalidTokenError:
            s = '未提供认证Token' 
            return s