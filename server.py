from flask import Flask, render_template, request, session
import crud
import requests
from pprint import pprint
import os

app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'

API_KEY = os.environ['SPOONACULAR_KEY']

@app.route('/') 
def index():
    """Homepage"""
    return render_template('index.html') 

@app.route("/health", methods=["POST"]) 
def health_condition():
    """Displays recipes based on the health condition selected by the user."""

    user_input = request.form.get("condition") # "diabetes"
    print(user_input)

    # read the .csv file based on the value of "user_input"
    # if user_input="diabetes" then we need to read/extract the data from .csv corresponding to "diabetes"
    data = open('health_data.csv')
    for line in data:
        line = line.split("|") # [condition, description, minCarbs]

        if line[0] == user_input:
            condition_name = line[0] 
            condition_description = line[1] 
            minCarbs = int(line[2])
            maxCarbs = int(line[3])
            minCholesterol = int(line[4])
            maxCholesterol = int(line[5])
            minSaturatedFat = int(line[6])
            maxSaturatedFat = int(line[7])
            minSugar = int(line[8])
            maxSugar = int(line[9])
            minIron = int(line[10])

            new_condition = crud.create_Health_Condition(condition_name, 
                                                     condition_description, 
                                                     minCarbs, 
                                                     maxCarbs, 
                                                     minCholesterol, 
                                                     maxCholesterol, 
                                                     minSaturatedFat, 
                                                     maxSaturatedFat, 
                                                     minSugar, 
                                                     maxSugar, 
                                                     minIron)
            
    headers = {"Content-Type": "application/json"}

    payload = {
            'apiKey': API_KEY
            }
    if maxCarbs > 0:
         payload["maxCarbs"] = maxCarbs
    elif maxCholesterol > 0:
         payload["maxCholesterol"] = maxCholesterol
    elif maxSaturatedFat > 0:
         payload["maxSaturatedFat"] = maxSaturatedFat
    elif maxSugar > 0:
         payload["maxSugar"] = maxSugar
    elif minIron > 0:
         payload["minIron"] = minIron    
    
    print(payload)

    res = requests.get('https://api.spoonacular.com/recipes/complexSearch', headers=headers, params=payload)
    print(res)

    res = res.json()
    #print(res)
    return render_template("health_conditions.html", results=res)

@app.route('/instructions/<recipe_id>') #review this route 
def instructions(recipe_id):
    
        payload = {
            "apiKey": API_KEY,
            "id": recipe_id
        }

        headers = {"Content-Type": "application/json"}

        url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?includeNutrition=false'

        res = requests.get(url, headers=headers, params=payload)
        print(res)

        data = res.json()
        pprint(data)
        
        #return recipe_id

        return render_template("instructions.html", results=data)



# https://fellowship.hackbrightacademy.com/materials/serft18/lectures/flask/#variables-in-a-url

# get individual recipe info from
# https://api.spoonacular.com/recipes/{id}/information
# docs: https://spoonacular.com/food-api/docs#Get-Recipe-Information

if __name__ == '__main__':
    from model import connect_to_db
    connect_to_db(app)
    app.run(debug=True)