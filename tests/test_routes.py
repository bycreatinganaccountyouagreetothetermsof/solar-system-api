def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_with_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == None


def test_get_all_planets(client, eight_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == eight_planets


def test_get_one_planet(client, eight_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "mercury",
        "description": "the littlest planet",
        "color": "gray",
    }


def test_post_one_planet(client):
    pluto = {
        "name": "pluto",
        "description": "the bravest planet",
        "color": "pink",
    }
    response = client.post("/planets", json=pluto)
    assert response.status_code == 201
