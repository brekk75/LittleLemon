from django.test import TestCase
from ..models import Menu,Booking

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title='Far breton', price=8.50, menu_item_description="Gateux à la part 1")
        self.item2 = Menu.objects.create(title='Tarte aux fraises', price=5.50, menu_item_description="Gateux à la part 2")
        self.item3 = Menu.objects.create(title='Tarte au citron', price=4.50, menu_item_description="Gateux à la part 3")
        self.item4 = Menu.objects.create(title='Flan nature', price=7.99, menu_item_description="Gateux à la part 4")

    def test_getall(self):
        farbreton = Menu.objects.get(title='Far breton')
        tarteauxfraises = Menu.objects.get(title='Tarte aux fraises')
        tarteaucitron = Menu.objects.get(title='Tarte au citron')
        flannature = Menu.objects.get(title='Flan nature')

        self.assertEqual(str(farbreton), 'Far breton : 8.50')
        self.assertEqual(farbreton.menu_item_description,"Gateux à la part 1")
        self.assertEqual(str(tarteauxfraises), 'Tarte aux fraises : 5.50')
        self.assertEqual(tarteauxfraises.menu_item_description,"Gateux à la part 2")
        self.assertEqual(str(tarteaucitron), 'Tarte au citron : 4.50')
        self.assertEqual(tarteaucitron.menu_item_description,"Gateux à la part 3")
        self.assertEqual(str(flannature), 'Flan nature : 7.99')
        self.assertEqual(flannature.menu_item_description,"Gateux à la part 4")
