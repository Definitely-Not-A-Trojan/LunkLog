from mongo_api import MongoAPI

from flask         import Flask, request
from flask_restful import Resource, Api

# Put your connection string into a file named "test_connection_str"
# in LunkLog/src/api
with open("./test_connection_str", "r") as in_file:
    test_connection_str = in_file.readline()

global mi_mongo


class Exercises(Resource):
    def get(self):
        pass
    
    def post(self):
        print(request.form['data'])
        return mi_mongo.lookup_exercise(request.form['data'])

class Sets(Resource):
    def get(self):
        return mi_mongo.getall_sets()
    
    def put(self):
        pass

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
        return mi_mongo.lookup_user(username, data_type="JSON")

    def post(self):
        pass

class UsersGroups(Resource):
    def get(self, username, groupname):
        return mi_mongo.get_usergroup(username, groupname, data_type="JSON")

class UsersGroupsSets(Resource):
    def get(self, username, groupname):
        return mi_mongo.getall_usergroupsets(username, groupname, data_type="JSON")
    
    def put(self, username, groupname):
        pass

class UsersSets(Resource):
    def get(self, username):
        return mi_mongo.getall_userssets(username, data_type="JSON")
    
    # This is one that takes in data: specific filters
    def put(self, username):
        pass


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)

    mi_mongo = MongoAPI(host=test_connection_str)

    api.add_resource(Sets, "/sets")
    api.add_resource(Exercises, "/exercises")
    api.add_resource(Measurements, "/measurements")
    api.add_resource(Users, "/users/<string:username>")
    api.add_resource(UsersGroups, "/users/<string:username>/groups/<string:groupname>")
    api.add_resource(UsersGroupsSets, "/users/<string:username>/groups/<string:groupname>/sets")
    api.add_resource(UsersSets, "/users/<string:username>/sets")

    app.run(debug=True)
