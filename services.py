
from repositories import UserRepository, ArtworkRepository, OrderRepository

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user_profile(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

class ArtworkService:
    def __init__(self, artwork_repository):
        self.artwork_repository = artwork_repository

    def get_artwork_details(self, artwork_id):
        return self.artwork_repository.get_artwork_by_id(artwork_id)

class OrderService:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def get_order_details(self, order_id):
        return self.order_repository.get_order_by_id(order_id)
    