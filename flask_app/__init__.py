from flask import Flask
app = Flask(__name__)
# If we were using session in contollers, we would add the following line here
app.secret_key = "shhhhhh"

# The following allows easy changing of database name throughout our files
DATABASE = 'dojos_and_ninjas_schema'