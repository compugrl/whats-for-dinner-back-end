import pytest
from app import create_app
from app.models.shopping_list import Shopping_list
from app.models.user import User
from app.models.recipe import Recipe
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
        name="Shayla Logan", email="shayla.logan709@gmail.com", days_to_display=1)
    db.session.add(new_user)
    db.session.commit()

# This fixture gets called in every test that
# references "one_recipe"
# This fixture creates one recipe and saves it in the database
@pytest.fixture
def one_recipe(app):
    new_recipe = Recipe(hash="6cddaef7d51e5ee16fd39363d2355286", shareAs="https://www.whats-for-dinner.com/testitem", label="Slow Cooker Chicken and Dumplings", image_url="https://edamam-product-images.s3.amazonaws.com/web-img/6ea/6ea9a1ee2dffa40c71bb8001c2351144-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLWVhc3QtMSJHMEUCIGbhTnheNwlVEJNVBETMVix8NacscZC%2F4OcTu9IeVytpAiEA6325IzZK8ik3zV6AnzDBy7%2BdaPwR7zspzruYXMoEQuUq2wQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwxODcwMTcxNTA5ODYiDAGc%2B3nOL0EgYZbspyqvBPUE4NV4kgRFky6vrvpinrURa%2FvQlUP8G9KU9fQvcJxD9vQX2hAD8ewtqM40am77mnX7iSmx%2FscXlA%2F9RM87H8CGrnM%2F%2F6EMOReY0JxnUfsjGk%2FYMwO5wwYOFBgawA%2Bz96D%2BjQJ7CT6Fw9NMO67hxZya1X6JFP1e58DkFnKXnF7IbyGieAYsV9yRhLM3kdf%2BJBkPlvhbF7ZglwRbRGP2esBmfM87hkqedx7hOHzSI7hPLjohvSC1oSS49uzzE5b8c48QSO8uFw823dVZJpZrV%2BiOmefk52NYT02XzK1s8HJPz8OO2MF7gnflfwWt18tOfH8uD2F%2F5829PVa7kzLH9yuxyZW7l%2BZAH%2B2XewjnHA0DMVVYpiva5Hd1C3Oy8a3TCTB0JabyP09RKhXAhqRgPKuWe4a5iY1cQ4cTrqSJ0k2pvAwLWM7%2BsLxAxgeql9J7%2BXUDq6GAtGhGJxREUJYbHjx6HFR23KNgw26r%2FqWTFummBaQfTyNWtk2SEFIUAzPmxd1i%2F3JWBTXxlMvK70Ywbr3xYtEtlkCdbhIg9qDi3CHEoDMYn4uWwCgkR6SjGymkAuWmvs%2Fdy6SlY%2FIPE3t3ugQld0%2Fla0IPrTvdCeSrqIs71Xyh9LR9oCVV8WUmsNG2wuUG4N6Fe41bBcbQWO%2BsevohD4q5TY%2BYGkvVUwLKPar1%2BGs8fgXMdKCL4QMcu9kd7cyNk5Am6ziMJDyyKfWV6Dzwxcp0qAXDPL%2FZ%2FEBPle4wxs%2F6lgY6qQFdNQl%2FbNYmfjiv8zT%2Blz5xPZHHZUEk%2ByMVZQlA3aua2ZlJOMQ00fa7ANNCKzfesUxXypoWpH2HzF%2FCULvNA98jyVjDq28pq5deANWNrxfJu5f5fSxEHOsCuQAX%2BP3pUS59Wykx%2BDu0v622YxjLlerU%2B9NA6%2FV6tfpIgUlnTuWQlfJ7kXIEZAYFMgc9LbbHxZuq2cmpU%2BAnYf5EUKuIAYnnlrKfY98a2chH&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220725T153201Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFFR3AL5MW%2F20220725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=489e80d3e8eb60a4dabde228fee52720c1a2325a6f2c119522ee39075031b2ca", menu_date="Aug 01 2022", favorite=False, user_id=1)
    db.session.add(new_recipe)
    db.session.commit()

# This fixture gets called in every test that
# references "one_item"
# This fixture creates one shopping list item and saves it in the database
@pytest.fixture
def one_item(app):
    new_item = Shopping_list(
        item="sliced cheese", completed=False, user_id=1)
    db.session.add(new_item)
    db.session.commit()