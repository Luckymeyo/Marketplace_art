
import sqlite3
from entities import User, Artwork, Order

class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_user_by_id(self, user_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, name, email FROM users WHERE user_id=?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return User(*user) if user else None

class ArtworkRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_artwork_by_id(self, artwork_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT artwork_id, title, artist, price, dimensions, medium, category FROM artworks WHERE artwork_id=?", (artwork_id,))
        artwork = cursor.fetchone()
        conn.close()
        return Artwork(*artwork) if artwork else None

class OrderRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_order_by_id(self, order_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT order_id, artwork_id, user_id, order_date, status FROM orders WHERE order_id=?", (order_id,))
        order = cursor.fetchone()
        conn.close()
        return Order(*order) if order else None
    