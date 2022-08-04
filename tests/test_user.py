from app.models.user import User
import pytest
from datetime import datetime

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_users_no_saved_users(client):
    # Act
    response = client.get("/users")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_users_one_saved_user(client, one_user):
    # Act
    response = client.get("/users")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body == [
        {
            "uid": 1,
            "name": "Shayla Logan",
            "email": "shayla.logan709@gmail.com"
        }
    ]

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_user(client):
    # Act
    response = client.post("/users", json={
        "name": "Shayla Logan",
        "email": "shayla.logan709@gmail.com"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
        
    new_user = User.query.get(1)
    assert new_user
    assert new_user.name == "Shayla Logan"
    assert new_user.email == "shayla.logan709@gmail.com"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_user_name(client, one_user):
    # Act
    response = client.patch("/users/1", json={
        "name": "Shayla Shannel",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    
    new_user = User.query.get(1)
    assert new_user
    assert new_user.name == "Shayla Shannel"
    assert new_user.email == "shayla.logan709@gmail.com"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_user_email(client, one_user):
    # Act
    response = client.patch("/users/1", json={
        "email": "shayla_test@example.com",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    
    new_user = User.query.get(1)
    assert new_user
    assert new_user.name == "Shayla Logan"
    assert new_user.email == "shayla_test@example.com"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_specific_user(client, one_user):
    # Act
    response = client.get("/users/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "user" in response_body
    
    new_user = User.query.get(1)
    assert new_user
    assert new_user.name == "Shayla Logan"
    assert new_user.email == "shayla.logan709@gmail.com"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_delete_specific_user(client, one_user):
    # Act
    response = client.delete("/users/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {'success': 'User Shayla Logan successfully deleted'}

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_user_not_found(client):
    # Act
    response = client.get("/users/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == "User 1 not found"

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_user_bad_data(client):
    # Act
    response = client.get("/users/Shayla")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        'error': 'Invalid user id: Shayla'
    }
