from operator import and_
from app.models.user import User
from app.models.recipe import Recipe
from app.models.user_recipe import UserRecipe
import pytest
from sqlalchemy import and_

def test_create_user_recipe(client, one_user, one_recipe):
    # Act
    response = client.post("/ur", json={
        "favorite": True,
        "uid": 1,
        "rhash": "6cddaef7d51e5ee16fd39363d2355286"
    })

    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    
    user_recipe = UserRecipe.query.get(1)
    assert user_recipe
    assert user_recipe.uid == 1
    assert user_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_user_recipe_fave(client, one_user, one_recipe, one_user_recipe):
    # Act
    response = client.patch("/ur/1", json={
        "favorite": True
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
        
    new_user_recipe = UserRecipe.query.get(1)
    assert new_user_recipe
    assert new_user_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"
    assert new_user_recipe.uid == 1
    assert new_user_recipe.favorite == True

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_user_recipe_date(client, one_user, one_recipe, one_user_recipe):
    # Act
    response = client.patch("/ur/1", json={
        "menu_date": "Aug 01 2022"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
        
    new_user_recipe = UserRecipe.query.get(1)
    assert new_user_recipe
    assert new_user_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"
    assert new_user_recipe.uid == 1
    assert new_user_recipe.menu_date == "Aug 01 2022"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_recipes_per_user(client, one_user, one_recipe, one_user_recipe):
    # Act
    response = client.get("/ur/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
        
    new_user_recipe = UserRecipe.query.get(1)
    assert new_user_recipe
    assert new_user_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"
    assert new_user_recipe.uid == 1

def test_get_specific_user_recipe(client, one_user, one_recipe, one_user_recipe):
    # Act
    response = client.get("/ur/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "user_recipe" in response_body
    
    new_user_recipe = UserRecipe.query.get(1)
    assert new_user_recipe
    assert new_user_recipe.uid == 1
    assert new_user_recipe.rhash == "6cddaef7d51e5ee16fd39363d2355286"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_user_recipe(client, one_user, one_recipe, one_user_recipe):
    # Act
    response = client.delete("/ur/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'success': 'User recipe 1 successfully deleted'}

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_user_favorite_recipes(client, one_user, one_recipe, one_user_recipe):
    # Act
    response = client.get("/ur/user/1/fave")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_user_menu_itemss(client, one_user, one_recipe, one_user_recipe):
    # Act
    response = client.get("/ur/user/1/date?menu_date=Aug 01 2022")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200