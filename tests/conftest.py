import pytest
from app import create_app
from app import db
from app.models.planet import Planet
from flask import jsonify


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def eight_planets(app):
    eight_planets = [
        Planet(name="mercury", description="the littlest planet", color="gray"),
        Planet(name="venus", description="the hottest planet", color="maroon"),
        Planet(name="earth", description="the liveliest planet", color="green"),
        Planet(name="mars", description="the reddest planet", color="red"),
        Planet(name="jupiter", description="the biggest planet", color="orange"),
        Planet(name="saturn", description="the ring planet", color="yellow"),
        Planet(name="uranus", description="the most sidways planet", color="purple"),
        Planet(name="neptune", description="the boring planet", color="blue"),
    ]
    db.session.add_all(eight_planets)
    db.session.commit()
    planets_response = []
    for planet in eight_planets:
        planets_response.append(planet.to_json())
    return planets_response
