#-*- coding:utf-8 -*-
import sys
sys.path.append('../')
from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
from kuaidi100 import KuaiDi100

app = Flask(__name__)


@app.route('/api/kuaidi100/<num>',methods=['GET', 'POST'])
def kuaidi(num):
    if request.method == 'GET':
        num = num.split('=')[1]
        data = KuaiDi100(num).post()
        if data:

            result = jsonify({"message":"success","data":data})
        else:
            result = jsonify({"message":"failed","data":"未找到相关物流信息"})
        return result


if __name__ == '__main__':
    app.config["JSON_AS_ASCII"] = False
    WSGIServer(('0.0.0.0', 6002), app).serve_forever()