# -*- coding:utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api
from flask_docs import ApiDoc
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# Local loading
# app.config['API_DOC_CDN'] = False

# Disable document pages
# app.config['API_DOC_ENABLE'] = False

# RESTful Api documents to be excluded
app.config['RESTFUL_API_DOC_EXCLUDE'] = []

restful_api = Api(app)
ApiDoc(app)


class KuaiDi100(Resource):
    """Manage kuaidi100"""

    def get(self):
        """
        @@@
            开发环境

                - Python3.7.1
        #### method
                - GET
        #### args

        | args | nullable | type |
        |--------|-------|------|
        |  num  | false |  int |

        #### return
        - ##### json
        > {
  "data": [
    {
      "context": "已签收,签收人是：【请见电子面单】",
      "time": "2019-08-20 14:32:32"
    },
    {
      "context": "快件已到达【重庆南岸一部ZX】,站点客服电话【023-63760903】",
      "time": "2019-08-19 08:48:12"
    },
    {
      "context": "快件在【重庆南岸一部ZX】做了派件",
      "time": "2019-08-19 08:42:52"
    },
    {
      "context": "快件由【重庆南岸一部】发往【重庆南岸一部ZX】",
      "time": "2019-08-19 08:37:03"
    },
    {
      "context": "快件已到达【重庆南岸一部】",
      "time": "2019-08-19 07:09:15"
    },
    {
      "context": " 所有货物（共1件）已到达【重庆南岸一部】;",
      "time": "2019-08-19 07:09:15"
    },
    {
      "context": "快件由【重庆分拨】发往【重庆南岸一部】",
      "time": "2019-08-19 03:58:05"
    },
    {
      "context": "快件已到达【重庆分拨】",
      "time": "2019-08-17 14:56:45"
    },
    {
      "context": "快件由【杭州分拨】发往【重庆分拨】",
      "time": "2019-08-16 06:53:20"
    },
    {
      "context": "快件已到达【杭州分拨】",
      "time": "2019-08-16 03:27:25"
    }
  ],
  "message": "success"
}


>{
  "data": "未找到相关物流信息",
  "message": "failed"
}
        @@@
        """
        return {'todos': 'get todolist'}


restful_api.add_resource(KuaiDi100, '/https://118.25.84.115:9000/KuaiDi100-Api/num=91050449921')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5050, debug=True)
    WSGIServer(('0.0.0.0', 5050), app).serve_forever()

