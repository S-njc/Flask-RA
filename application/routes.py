from flask import request, jsonify
from werkzeug import exceptions
from application import app
from application.models import Character

@app.route('/')
def hello():
    return jsonify({
        "message": "Welcome",
        "description": "Characters API",
        "endpoints": [
            "GET / 200",
            "GET /characters"
        ]
    }), 200

# @app.route('/characters', methods=['GET', 'POST'])
# def characters():
#     if request.method == 'GET':
#         characters = Character.query.all()
#         return jsonify([char.json for char in characters]), 201

#     elif request.method == 'POST':
#         data = request.get_json()
#         new_character = Character(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase'])
#         db.session.add(new_character)
#         db.session.commit()
#         return jsonify(new_character.json), 200

# @app.route('/characters/<int:char_id>', methods=['GET', 'PATCH', 'DELETE'])
# def character(char_id):
#     char = Character.query.get_or_404(char_id)

#     if request.method == 'GET':
#         return jsonify(char.json), 200

#     elif request.method == 'PATCH':
#         data = request.get_json()
#         if 'name' in data:
#             char.name = data['name']
#         if 'age' in data:
#             char.age = data['age']
#         if 'catch_phrase' in data:
#             char.catch_phrase = data['catch_phrase']
#         db.session.commit()
#         return jsonify(char.json)

#     elif request.method == 'DELETE':
#         db.session.delete(char)
#         db.session.commit()
#         return jsonify({'message': 'Character deleted'}), 204
    
# @app.errorhandler(exceptions.NotFound)
# def handle_404(err):
#     return { "error": f"Oops {err}"}, 404