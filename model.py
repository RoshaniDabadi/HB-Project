from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Health_Condition(db.Model):
    """Data model for health condition."""
    __tablename__= "health_conditions"

    condition_id = db.Column(db.Integer, primary_key = True, autoincrement=True, nullable = False)
    condition_name = db.Column(db.String(50), nullable = False)
    condition_description = db.Column(db.String(), nullable = False)
    min_carbs = db.Column(db.Integer)
    max_carbs = db.Column(db.Integer)
    min_Cholesterol = db.Column(db.Integer)
    max_Cholesterol = db.Column(db.Integer)
    min_SaturatedFat = db.Column(db.Integer)
    max_SaturatedFat = db.Column(db.Integer)
    min_Sugar = db.Column(db.Integer)
    max_Sugar = db.Column(db.Integer)
    min_Iron = db.Column(db.Integer)


class User(db.Model):
    __tablename__ = "users"
    """"""
    user_id = db.Column(db.Integer, primary_key = True, autoincrement=True, nullable = False)
    username = db.Column(db.String(25), unique=True, nullable = False)
    password = db.Column(db.String(), nullable = False)
    condition_id = db.Column(db.Integer, db.ForeignKey('health_conditions.condition_id'))

    favorites = db.relationship("Favorite", back_populates="user")
    
    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'
    
    #create a recipe class with their titles, image, etc. 

class Recipe(db.Model):
    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, primary_key = True, nullable = False) #API generated recipe_id
    title = db.Column(db.String())
    image = db.Column(db.String())
    source_url = db.Column(db.String())

    favorites = db.relationship("Favorite", back_populates="recipe")

    def __repr__(self):
        return f'<Recipe recipe_id={self.recipe_id} title={self.title}>'

    
class Favorite(db.Model):
    __tablename__ = "favorites"

    favorite_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    user = db.relationship('User', back_populates='favorites')
    recipe = db.relationship('Recipe', back_populates='favorites')

    def __repr__(self):
        return f"<Favorite(favorite_id={self.favorite_id})>" #not sure how to get recipe title after the favorite id here using recipe_id
    

def connect_to_db(flask_app, db_uri="postgresql:///health", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



    


