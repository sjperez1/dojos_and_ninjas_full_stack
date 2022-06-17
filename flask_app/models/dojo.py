from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

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
        ninjas_list = []

        for row in result:
            one_ninja = {
                "id" = row["ninja.id"],
                "first_name" = row['first_name'],
                "last_name" = row['last_name'],
                "created_at" = row['ninja.created_at'],
                "updated_at" = row['ninja.updated_at'],
                "dojo_id" = row['dojo_id']
            }

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