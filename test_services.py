
import unittest
from services import UserService, ArtworkService, OrderService
from repositories import UserRepository, ArtworkRepository, OrderRepository

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repository = UserRepository('test_database.db')
        self.user_service = UserService(self.user_repository)

    def test_get_user_profile(self):
        user = self.user_service.get_user_profile(1)
        self.assertIsNotNone(user)
        self.assertEqual(user.user_id, 1)

class TestArtworkService(unittest.TestCase):
    def setUp(self):
        self.artwork_repository = ArtworkRepository('test_database.db')
        self.artwork_service = ArtworkService(self.artwork_repository)

    def test_get_artwork_details(self):
        artwork = self.artwork_service.get_artwork_details(1)
        self.assertIsNotNone(artwork)
        self.assertEqual(artwork.artwork_id, 1)

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.order_repository = OrderRepository('test_database.db')
        self.order_service = OrderService(self.order_repository)

    def test_get_order_details(self):
        order = self.order_service.get_order_details(1)
        self.assertIsNotNone(order)
        self.assertEqual(order.order_id, 1)

if __name__ == '__main__':
    unittest.main()
    