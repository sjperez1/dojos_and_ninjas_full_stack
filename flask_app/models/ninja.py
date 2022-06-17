from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        # what is in the constructor function matches the table columns from the schema.
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.age = data['age']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas(dojo_id, first_name, last_name, age) "
        query += "VALUES(%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);"

        return connectToMySQL(DATABASE).query_db(query, data)
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