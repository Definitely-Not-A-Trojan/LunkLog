from mongo_api import MongoAPI

from flask         import Flask, request
from flask_restful import Resource, Api


global mi_mongo


class Exercises(Resource):
    def get(self):
        pass
    
    def post(self):
        print(request.form['data'])
        return mi_mongo.lookup_exercise(request.form['data'])

class Sets(Resource):
    def get(self):
        return {"hello": "world"}

    def post(self):
        pass

class Measurements(Resource):
    def __init__(self, mongo_api):
        pass

    def get(self):
        pass

    def post(self):
        pass

class Users(Resource):
    def get(self, username):
        return mi_mongo.lookup_user(username)

    def post(self):
        pass

if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)

    mi_mongo = MongoAPI(host=test_connection_str)

    api.add_resource(Sets, "/")
    api.add_resource(Exercises, "/exercises")
    api.add_resource(Measurements, "/measurements")
    api.add_resource(Users, "/users/<string:username>")

    app.run(debug=True)
