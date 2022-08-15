import pytest
from app import create_app
from app.models.shopping_list import Shopping_list
from app.models.user import User
from app.models.recipe import Recipe
from app.models.user_recipe import UserRecipe
from app import db

@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

# This fixture gets called in every test that
# references "one_user"
# This fixture creates one user and saves it in the database
@pytest.fixture
def one_user(app):
    new_user = User(
        uid="H5F3cCBqWUYfwRSLUMpNcijZmSf2", 
        name="Shayla Logan", 
        email="shayla@adastudent.com")
    db.session.add(new_user)
    db.session.commit()

# This fixture gets called in every test that
# references "one_recipe"
# This fixture creates one recipe and saves it in the database
@pytest.fixture
def one_recipe(app):
    new_recipe = Recipe(rhash="6cddaef7d51e5ee16fd39363d2355286", shareAs="https://www.whats-for-dinner.com/testingredient", label="Slow Cooker Chicken and Dumplings")
    db.session.add(new_recipe)
    db.session.commit()

# This fixture gets called in every test that
# references "one_ingredient"
# This fixture creates one shopping list ingredient and saves it in the database
@pytest.fixture
def one_ingredient(app):
    new_ingredient = Shopping_list(
        ingredient="sliced cheese", completed=False, uid="H5F3cCBqWUYfwRSLUMpNcijZmSf2")
    db.session.add(new_ingredient)
    db.session.commit()

# This fixture gets called in every test that
# references "one_user_recipe"
# This fixture adds one user + one recipe and saves it in the database
@pytest.fixture
def one_user_recipe(app, one_user, one_recipe):
    new_user_recipe = UserRecipe(
        rhash="6cddaef7d51e5ee16fd39363d2355286", uid="H5F3cCBqWUYfwRSLUMpNcijZmSf2", 
        favorite=True, 
        menu_date="Aug 01 2022")
    db.session.add(new_user_recipe)
    db.session.commit()