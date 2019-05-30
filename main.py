# -*- coding: utf-8 -*-
# by Hank 2019/5/30

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from pynvml import *
from get_gpu_info import get_gpu_info, getProcessInfo
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

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

if __name__ == "__main__":
    app.run(debug=True)
