from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from model import User, db
import crud
import requests
from pprint import pprint
import os

app = Flask(__name__)
app.secret_key = 'eat_well_live_well'

#configuring Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

API_KEY = os.environ['SPOONACULAR_KEY']

@login_manager.user_loader
def load_user(user_id):
     """Callback to load user object based on user_id"""
     return User.query.get(int(user_id))

@app.route('/') 
def index():
    """Homepage"""
    return render_template('index.html') 

@app.route('/register', methods=['GET', 'POST'])
def register():
     """User registration"""
     if request.method == 'POST':
          username = request.form['username']
          password = request.form['password']

          #Checking if username already exists
          existing_user = User.query.filter.by(username=username).first()
          if existing_user:
               # Display error message or redirect to registration page
            return 'Username already exists'
          
          # Create a new user
          new_user = User(username=username, password=generate_password_hash(password))
          db.session.add(new_user)
          db.session.commit()

        # Log in the user after registration
          login_user(new_user)
        
        # Redirect to the user's dashboard or any other page
          return redirect(url_for('dashboard'))

     return render_template('register.html')



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

if __name__ == '__main__':
    from model import connect_to_db
    connect_to_db(app)
    app.run(debug=True)