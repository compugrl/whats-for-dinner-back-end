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
        "shareAs": "https://www.whats-for-dinner.com/testingredient"
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