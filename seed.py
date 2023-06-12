import os
from crud import create_Health_Condition
from server import app
from model import connect_to_db, db


os.system('dropdb health')
os.system('createdb health')

connect_to_db(app)
db.create_all()

data = open('health_data.csv')
for line in data:
    condition_name, condition_description, minCarbs, maxCarbs, minCholesterol, maxCholesterol, minSaturatedFat, maxSaturatedFat, minSugar, maxSugar, minIron = line.split('|')
    create_Health_Condition(condition_name, condition_description, minCarbs, maxCarbs, minCholesterol, maxCholesterol, minSaturatedFat, maxSaturatedFat, minSugar, maxSugar, minIron)