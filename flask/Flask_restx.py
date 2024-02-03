# Flask restx 기본 구조 예시

from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app)

@api.route('/testing')
class test_endpoint(Resource):
    def post(self):
        
        return {
            "hello fxxking world" : "post"
        }
        
    def get(self):
        
        return {
            "hello fxxking world" : "get"
        }
        
app.run(debug=True,host='localhost',port=9999,use_reloader=False)