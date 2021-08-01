import json
import pymongo

from bson import json_util

class MongoAPI:
    """
    MongoAPI
        API for communicating to the MongoDB.

        TODO: write code
    """
    def __init__(self, host, port=27017, live_database=False):
        client = pymongo.MongoClient(host=host,port=port)
        
        if live_database:
            self.database = client.release
        else:
            # Current test database, name subject to change
            self.database = client.LunkLog_V0

    def parse_json(self, data):
        return json.loads(json_util.dumps(data))

    def add_exercise(self, json):
        """
        Add Exercise
            Creates a JSON representation of an exercise to be added
            to the Exercise collection.

        Args:
            json (dict): data to be added

        Returns:
            response (bool): True on success, False on failure

        Exercises are structured as so:
        json = {
            "name"           -> str,
            "target_group"   -> str,
            "muscle_groups"  -> [str],
            "primary_target" -> str,
            "user_created"   -> bool
        }
        """
        self.database.exercises.insert_one(json)

    def add_set(self, json):
        """
        Add Set
            Takes in a JSON representation from the front end to
            create a new set in the database.

        Args:
            json (dict): data to be added

        Returns:
            response (bool): True on success, False on failure

        Sets are structed as follows:
        
        set = {
            user_id         -> ObjectId,
            exercise        -> ObjectId,
            date            -> str,
            reps            -> int,
            weight          -> float,
            time            -> float,
            comment         -> str,
            personal_record -> bool
        }
        """
        pass

    def add_measurement(self, json):
        pass

    def get_set(self, json):
        pass

    def update_set(self, json):
        pass
    
    def lookup_set(self, name):
        pass
    
    def lookup_exercise(self, name): #TODO: update docs
        """
        Look up Exercise
            Returns an exercise object ID given a name

        Args:
            name (str): name of exercise to find

        Returns:
            object id of the exercise
        """
        response = self.database.exercises.find_one({"name": name})
        return self.parse_json(response)

    def lookup_user(self, name):
        """
        Look up User
            Looks up a user in the Users collection given
            a string name.

        Args:
            name (str): Name used to get user_id
        """
        response = self.database.users.find_one({"username": name})
        return self.parse_json(response)

