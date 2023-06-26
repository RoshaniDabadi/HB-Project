import os
from crud import create_Health_Condition
from server import app
from model import connect_to_db, db, Recipe


os.system('dropdb health')
os.system('createdb health')

connect_to_db(app)
db.create_all()

data = open('health_data.csv')

for line in data:
    condition_name, condition_description, minCarbs, maxCarbs, minCholesterol, maxCholesterol, minSaturatedFat, maxSaturatedFat, minSugar, maxSugar, minIron = line.split('|')
    create_Health_Condition(condition_name, condition_description, minCarbs, maxCarbs, minCholesterol, maxCholesterol, minSaturatedFat, maxSaturatedFat, minSugar, maxSugar, minIron)

data.close()

# Populate the recipes table in model.py by retrieving the data from the API call made in server.py
# recipes_data = app.config['recipes_data']

# for recipe_data in recipes_data:
#     recipe = Recipe(
#         recipe_id=recipe_data['id'],
#         title=recipe_data['title'],
#         image=recipe_data['image'],
#         sourceUrl=recipe_data['sourceUrl']
#     )
#     db.session.add(recipe)

# db.session.commit()