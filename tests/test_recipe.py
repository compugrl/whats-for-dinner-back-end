from app.models.recipe import Recipe
import pytest
import os

recipe_key = os.environ.get("RECIPE_KEY")
recipe_app = os.environ.get("RECIPE_APP")


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_recipes_no_saved_recipes(client):
    # Act
    response = client.get("/recipes")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_recipes_one_saved_recipe(client, one_recipe):
    # Act
    response = client.get("/recipes")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    new_recipe = Recipe.query.get("6cddaef7d51e5ee16fd39363d2355286")
    assert new_recipe
    assert new_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"
    assert new_recipe.label == "Slow Cooker Chicken and Dumplings"
    assert new_recipe.shareAs == "https://www.whats-for-dinner.com/testingredient"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_recipe(client):
    # Act
    response = client.post("/recipes", json={
        "rhash": "6cddaef7d51e5ee16fd39363d2355286",
        "label": "Slow Cooker Chicken and Dumplings",
        "shareAs": "https://www.whats-for-dinner.com/testingredient",
        "image_url": "https://edamam-product-images.s3.amazonaws.com/web-img/6ea/6ea9a1ee2dffa40c71bb8001c2351144-s.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLWVhc3QtMSJHMEUCIGbhTnheNwlVEJNVBETMVix8NacscZC%2F4OcTu9IeVytpAiEA6325IzZK8ik3zV6AnzDBy7%2BdaPwR7zspzruYXMoEQuUq2wQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwxODcwMTcxNTA5ODYiDAGc%2B3nOL0EgYZbspyqvBPUE4NV4kgRFky6vrvpinrURa%2FvQlUP8G9KU9fQvcJxD9vQX2hAD8ewtqM40am77mnX7iSmx%2FscXlA%2F9RM87H8CGrnM%2F%2F6EMOReY0JxnUfsjGk%2FYMwO5wwYOFBgawA%2Bz96D%2BjQJ7CT6Fw9NMO67hxZya1X6JFP1e58DkFnKXnF7IbyGieAYsV9yRhLM3kdf%2BJBkPlvhbF7ZglwRbRGP2esBmfM87hkqedx7hOHzSI7hPLjohvSC1oSS49uzzE5b8c48QSO8uFw823dVZJpZrV%2BiOmefk52NYT02XzK1s8HJPz8OO2MF7gnflfwWt18tOfH8uD2F%2F5829PVa7kzLH9yuxyZW7l%2BZAH%2B2XewjnHA0DMVVYpiva5Hd1C3Oy8a3TCTB0JabyP09RKhXAhqRgPKuWe4a5iY1cQ4cTrqSJ0k2pvAwLWM7%2BsLxAxgeql9J7%2BXUDq6GAtGhGJxREUJYbHjx6HFR23KNgw26r%2FqWTFummBaQfTyNWtk2SEFIUAzPmxd1i%2F3JWBTXxlMvK70Ywbr3xYtEtlkCdbhIg9qDi3CHEoDMYn4uWwCgkR6SjGymkAuWmvs%2Fdy6SlY%2FIPE3t3ugQld0%2Fla0IPrTvdCeSrqIs71Xyh9LR9oCVV8WUmsNG2wuUG4N6Fe41bBcbQWO%2BsevohD4q5TY%2BYGkvVUwLKPar1%2BGs8fgXMdKCL4QMcu9kd7cyNk5Am6ziMJDyyKfWV6Dzwxcp0qAXDPL%2FZ%2FEBPle4wxs%2F6lgY6qQFdNQl%2FbNYmfjiv8zT%2Blz5xPZHHZUEk%2ByMVZQlA3aua2ZlJOMQ00fa7ANNCKzfesUxXypoWpH2HzF%2FCULvNA98jyVjDq28pq5deANWNrxfJu5f5fSxEHOsCuQAX%2BP3pUS59Wykx%2BDu0v622YxjLlerU%2B9NA6%2FV6tfpIgUlnTuWQlfJ7kXIEZAYFMgc9LbbHxZuq2cmpU%2BAnYf5EUKuIAYnnlrKfY98a2chH&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220725T153201Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFFR3AL5MW%2F20220725%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=489e80d3e8eb60a4dabde228fee52720c1a2325a6f2c119522ee39075031b2ca"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    
    new_recipe = Recipe.query.get("6cddaef7d51e5ee16fd39363d2355286")
    assert new_recipe
    assert new_recipe
    assert new_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"
    assert new_recipe.label == "Slow Cooker Chicken and Dumplings"
    assert new_recipe.shareAs == "https://www.whats-for-dinner.com/testingredient"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_specific_recipe(client, one_recipe):
    # Act
    response = client.get("/recipes/6cddaef7d51e5ee16fd39363d2355286")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "recipe" in response_body
        
    new_recipe = Recipe.query.get("6cddaef7d51e5ee16fd39363d2355286")
    assert new_recipe
    assert new_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"
    assert new_recipe.label == "Slow Cooker Chicken and Dumplings"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_specific_recipe(client, one_recipe):
    # Act
    response = client.delete("recipes/6cddaef7d51e5ee16fd39363d2355286")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'success': 'Recipe Slow Cooker Chicken and Dumplings successfully deleted'}

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_recipe_not_found(client):
    # Act
    response = client.get("/recipes/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == "Recipe 1 not found"

# @pytest.mark.skip(reason="Skipping due to rate limit")
def test_get_recipes_from_edamam(client):
    # Act
    response = client.get("/search?q=chicken")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200