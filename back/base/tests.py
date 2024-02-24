from django.test import TestCase
from base.models import Category
# Create your tests here.



class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Тест", slug='test')

    def test_category(self):
        """Test for slug avaiability"""
        category = Category.objects.get(name="Тест")
        self.assertEqual(category.slug, 'The slug is "test"')