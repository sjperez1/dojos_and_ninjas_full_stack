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

        dojos = []
        for dojo in query_result:
            dojos.append(cls(dojo))
        return dojos

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

        one_dojo = cls(result[0])
        print(one_dojo)
        ninjas_list = []

        for row in result:
            one_ninja = {
                # do ninjas.column because ninjas is the table that it comes from.
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at'],
                'dojo_id' : row['dojo_id']
            }
            # create instance of a ninja
            ninja = Ninja(one_ninja)
            # put ninja instances in a list
            ninjas_list.append(ninja)
        # make an instance of dojo with a list of ninjas
        one_dojo.ninjas_list = ninjas_list
        print(one_dojo)
        print(one_dojo.ninjas_list)
        return one_dojo

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