from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        query_result = connectToMySQL(DATABASE).query_db(query)
        # the if query result and return [] are saying that if dojos is an empty list (no values found in the table), then it would normally return false, but we want to avoid that, so return and empty list if query_result is empty list with no dictionaries.
        if query_result:
            dojos = []
            for dojo in query_result:
                dojos.append(cls(dojo))
            return dojos
        return []

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos(name) "
        query += "VALUES(%(name)s);"

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        result = connectToMySQL(DATABASE).query_db(query, data)
        # print to visualize what steps need to be taken next to make an instance of a dojo and create instances of ninjas in the dojo.
        # print(result)

        if result:
            # we are making an instance of a dojo. Bc it is an object, we can add an attribute and the list will be an attribute.
            one_dojo = cls(result[0])
            print(result[0])
            ninjas_list = []
            for row in result:
                one_ninja = {
                    # do ninjas.column because ninjas is the table that it comes from.
                    'id' : row['ninjas.id'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'created_at' : row['ninjas.created_at'],
                    'updated_at' : row['ninjas.updated_at'],
                    'dojo_id' : row['dojo_id'],
                    'age' : row['age']
                }
                # create instance of a ninja
                ninja = Ninja(one_ninja)
                # put ninja instances in a list
                ninjas_list.append(ninja)
            # make an instance of dojo with an attribute that equals a list of ninjas.
            one_dojo.ninjas_list = ninjas_list
            print(one_dojo.ninjas_list)
            return one_dojo
        return []

"""
How to name functions based on what you doing in the database:

SELECT:
def get_all()
def get_one()

INSERT:
def create()

DELETE:
def delete_one()

UPDATE:
def update_one()
def edit_one()
"""