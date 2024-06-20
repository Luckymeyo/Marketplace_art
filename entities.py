
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

class Artwork:
    def __init__(self, artwork_id, title, artist, price, dimensions, medium, category):
        self.artwork_id = artwork_id
        self.title = title
        self.artist = artist
        self.price = price
        self.dimensions = dimensions
        self.medium = medium
        self.category = category

class Order:
    def __init__(self, order_id, artwork_id, user_id, order_date, status):
        self.order_id = order_id
        self.artwork_id = artwork_id
        self.user_id = user_id
        self.order_date = order_date
        self.status = status
    