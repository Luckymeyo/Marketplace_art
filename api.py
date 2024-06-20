
from flask import Flask, jsonify, request
from services import UserService, ArtworkService, OrderService
from repositories import UserRepository, ArtworkRepository, OrderRepository

app = Flask(__name__)

user_repository = UserRepository('database.db')
user_service = UserService(user_repository)

artwork_repository = ArtworkRepository('database.db')
artwork_service = ArtworkService(artwork_repository)

order_repository = OrderRepository('database.db')
order_service = OrderService(order_repository)

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_profile(user_id)
    return jsonify(user.__dict__)

@app.route('/artworks/<artwork_id>', methods=['GET'])
def get_artwork(artwork_id):
    artwork = artwork_service.get_artwork_details(artwork_id)
    return jsonify(artwork.__dict__)

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = order_service.get_order_details(order_id)
    return jsonify(order.__dict__)

if __name__ == '__main__':
    app.run(debug=True)
    