from app.models.user import User
from app.models.shopping_list import Shopping_list
import pytest


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_list_no_saved_items(client, one_user):
    # Act
    response = client.get("/shopping_list/1/items")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# # @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_list_one_saved_item(client, one_user, one_item):
    # Act
    response = client.get("/shopping_list/1/items")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "uid": 1,
            "id": 1,
            "item": "sliced cheese",
            "completed": False
        }
    ]

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_item(client, one_user):
    # Act
    response = client.post("/shopping_list/1", json={
        "item": "blueberries",
        "completed": False,
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "shopping_list" in response_body
    assert response_body == {
        "shopping_list": {
            "id": 1,
            "uid": 1,
            "item": "blueberries",
            "completed": False
        }
    }
    new_shopping_list = Shopping_list.query.get(1)
    assert new_shopping_list
    assert new_shopping_list.item == "blueberries"
    assert new_shopping_list.completed == False

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_shopping_list_item(client, one_user, one_item):
    # Act
    response = client.get("/shopping_list/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "shopping_list" in response_body
    assert response_body == {
        "shopping_list": {
            "id": 1,
            "uid": 1,
            "item": "sliced cheese",
            "completed": False
        }
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_specific_shopping_list_item(client, one_user, one_item):
    # Act
    response = client.delete("/shopping_list/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'success': f'Shopping list item: sliced cheese successfully deleted'}

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_shopping_list_item_not_found(client):
    # Act
    response = client.get("/shopping_list/25")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == "Shopping list item 25 not found"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_shopping_list_bad_data(client):
    # Act
    response = client.get("/shopping_list/shayla")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        'error': 'Invalid shopping list id: shayla'
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_shopping_list_item(client, one_user, one_item):
    # Act
    response = client.patch("shopping_list/1/item/1", json={
        "item": "strawberries",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"updated list": {
            "id": 1, 
            "uid": 1,
            "item": "strawberries",
            "completed": False
            }
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_shopping_list_completed(client, one_user, one_item):
    # Act
    response = client.patch("shopping_list/1/item/1", json={
        "completed": True
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"updated list": {
            "id": 1, 
            "uid": 1,
            "item": "sliced cheese",
            "completed": True
            }
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_patch_item_bad_data(client, one_user, one_item):
    # Act
    response = client.patch("shopping_list/1/item/coke")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        'error': 'Invalid shopping list id: coke'
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_specific_item(client, one_user, one_item):
    # Act
    response = client.delete("/shopping_list/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'success': 'Shopping list item: sliced cheese successfully deleted'}