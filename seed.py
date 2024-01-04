from application import db
from application.models import Character

def seed_characters():
    characters_data = [
        {"name": "Naruto Uzumaki", "age": 17, "catch_phrase": "Believe it!"},
        {"name": "Uchiha Sasuke", "age": 17, "catch_phrase": "Katon goukakyuu no justu"},
        {"name": "Sakura Haruno", "age": 17, "catch_phrase": "Shannaro!"},
        {"name": "Kakashi Hatake", "age": 39, "catch_phrase": "I'm always on time."},
        {"name": "Jiraiya", "age": 54, "catch_phrase": "I'm a super pervert!"}
    ]

    for char_data in characters_data:
        character = Character(**char_data)
        db.session.add(character)

    db.session.commit()

if __name__ == '__main__':
    from application import app

    with app.app_context():
        db.create_all()
        seed_characters()