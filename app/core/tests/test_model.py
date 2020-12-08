from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@gmail.com', password='testing321'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email"""
        email = 'savchenko@gmail.com'
        password = 'testing321'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'savchenko@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email, password='testing321')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testing321')

    def test_create_new_superuser_successful(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser('taras', 'testing321')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name='Vegan')

        self.assertEqual(tag.name, str(tag))

    def test_ingredients_str(self):
        """Test the ingredient test representation"""
        ingredient = models.Ingredient.objects.create(user=sample_user(), name='Tomato')
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(user=sample_user(), title='Steak Osso Bucco', time_minutes=5, price=5.00)

        self.assertEqual(str(recipe), recipe.title)
