from model import Health_Condition, db, User, Recipe, Favorite, connect_to_db
import requests


def create_Health_Condition(condition_name, condition_description, minCarbs, #creates a new health condition every time, need to assign them to users 
    maxCarbs, minCholesterol, maxCholesterol, minSaturatedFat,
    maxSaturatedFat, minSugar, maxSugar, minIron):

    condition = Health_Condition(
        condition_name=condition_name,
        condition_description=condition_description,
        min_carbs=minCarbs,
        max_carbs=maxCarbs,
        min_Cholesterol=minCholesterol,
        max_Cholesterol=maxCholesterol,
        min_SaturatedFat=minSaturatedFat,
        max_SaturatedFat=maxSaturatedFat,
        min_Sugar=minSugar,
        max_Sugar=maxSugar,
        min_Iron=minIron        
    )
    db.session.add(condition)
    db.session.commit()

    return condition


def create_user(username,password):
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_condition_by_name(user_input):
    return Health_Condition.query.filter_by(condition_name=user_input).first()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

    #queryHealthCondition function -- to be added later
    #projectracker n movieratings lab exercises 

def populate_api_recipes(recipe_id, title, image):
    api_recipe = Recipe(
        recipe_id=recipe_id,
        title=title,
        image=image
    )

    db.session.add(api_recipe)
    db.session.commit()

def retrieve_favorite_recipes(user_id):
    # Retrieve the user's favorite recipes from the database
    # Example: Assuming you have a "Recipe" model and a "User" model with a relationship between them
    user = User.query.get(user_id)
    favorite_recipes = (
        Recipe.query.join(Favorite)
        .filter(Favorite.user_id == user_id)
        .all()
    )

    # Return the favorite recipes as a list or any suitable data structure
    return favorite_recipes

def recipe_query(recipe_id):

    recipe = Recipe.query.get(recipe_id)
    
    return recipe

def add_to_favorites(user_id, recipe_id):
    
    add_favorite = Favorite(user_id=user_id, recipe_id=recipe_id)

    db.session.add(add_favorite)
    db.session.commit()


        
if __name__ == "__main__":
    from server import app

    connect_to_db(app)
