# -*- coding: utf-8 -*-
# by Hank 2019/5/30

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from pynvml import *
from get_gpu_info import get_gpu_info, getProcessInfo
from auth import login
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('email', type=str)
parser.add_argument('pwd', type=str)

class Login(Resource):
    def post(self):
        args = parser.parse_args()
        user = login.find_user(args.email)
        if user == -1:
            return -1
        elif user.pwd != args.pwd:
            return -2
        else:
            return user


class GPUInfo(Resource):
    def get(self):
        GPUS = get_gpu_info()
        GPUS = json.dumps(GPUS)
        return GPUS

class GPUProcess(Resource):
    def get(self):
        process = getProcessInfo()
        return process

api.add_resource(GPUInfo, '/api/gpuinfo')
api.add_resource(GPUProcess, '/api/gpuprocess')
api.add_resource(Login, '/api/login')

if __name__ == "__main__":
    app.run(debug=True)
