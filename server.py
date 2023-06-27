from flask import Flask, render_template, request, session, redirect, jsonify
from model import User, Recipe, Favorite, db
import crud
import requests
from pprint import pprint
import os


app = Flask(__name__)
app.secret_key = 'eat_well_live_well'

API_KEY = os.environ['SPOONACULAR_KEY']


@app.route('/') 
def index():
    """Homepage"""
    return render_template('index.html') 


@app.route('/register', methods=['GET', 'POST'])
def register():
#User registration
    if request.method == 'POST':
          # <form> <input>...</input> </form>
        username = request.form['username'] # <input name="username">
        password = request.form['password'] # <input name="password">

          #Checking if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
               # Display error message or redirect to registration page
            return 'Username already exists'
          
          # Create a new user
        user = crud.create_user(username, password)

        """add the session feature with the user_id"""

        session['user_id'] = user.user_id
        session['username'] = user.username
        
        # Redirect to the user's dashboard or any other page
        return redirect('/dashboard')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
#User login
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username exists
        user = crud.get_user_by_username(username)
        
        if not user or user.password != password:
            # Display error message or redirect to login page
            return 'Invalid username or password'

        session['user_id'] = user.user_id
        session['username'] = user.username
        # Log in the user
        #login_user(user)
        """use session instead"""

        # Redirect to the user's dashboard or any other page
        return redirect('/dashboard')

    return render_template('login.html')


@app.route('/logout')
def logout():
#User logout
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect('/')


@app.route("/health", methods=["POST"]) 
def health_condition():
#Displays recipes based on the health condition selected by the user.

    user_input = request.form.get("condition") # "diabetes"
    print(user_input)
    condition = crud.get_condition_by_name(user_input)

            
    headers = {"Content-Type": "application/json"}

    payload = {
            'apiKey': API_KEY
            }
    if condition.max_carbs > 0:
        payload["maxCarbs"] = condition.max_carbs
    elif condition.max_Cholesterol > 0:
        payload["maxCholesterol"] = condition.max_Cholesterol
    elif condition.max_SaturatedFat > 0:
        payload["maxSaturatedFat"] = condition.max_SaturatedFat
    elif condition.max_Sugar > 0:
        payload["maxSugar"] = condition.max_Sugar
    elif condition.min_Iron > 0:
        payload["minIron"] = condition.min_Iron    
    
    print(payload)

    res = requests.get('https://api.spoonacular.com/recipes/complexSearch', headers=headers, params=payload)
    print(res)

    recipes_data = res.json()

    return render_template("health_conditions.html", results=recipes_data)


@app.route('/instructions/<recipe_id>', methods=['GET']) #review this route 
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

        is_user_logged_in = 'user_id' in session

        return render_template("instructions.html", results=data, is_user_logged_in=is_user_logged_in)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    is_user_logged_in = 'user_id' in session

    if is_user_logged_in:
        user_id = session['user_id']

        # Retrieve the user's favorite recipes
        favorite_recipes = crud.retrieve_favorite_recipes(user_id)

        if request.method == 'POST':
            recipe_id = request.json.get('recipe_id')
            recipe_title = request.json.get('recipe_title')
            recipe_image = request.json.get('recipe_image')
        
            print("\n\n",recipe_id, recipe_title, recipe_image, "\n\n")

            recipe = crud.recipe_query(recipe_id)

            if recipe is None:
                crud.populate_api_recipes(recipe_id, recipe_title, recipe_image)

            
            favorite_recipe = crud.add_to_favorites(user_id, recipe_id)

            return {"Success": True}

    
    
        return render_template('dashboard.html', favorite_recipes=favorite_recipes, is_user_logged_in=is_user_logged_in)
    
    
    return ("You must be logged in to access the dashboard!")
    



if __name__ == '__main__':
    from model import connect_to_db

    connect_to_db(app)

    app.run(debug=True)