from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self, title="IceCream", price=100, inventory=100):
        return Menu.objects.create(title=title, price=price, inventory=inventory)

    def test_getall(self):
        menu = self.setup()
        self.assertTrue(isinstance(menu, Menu))