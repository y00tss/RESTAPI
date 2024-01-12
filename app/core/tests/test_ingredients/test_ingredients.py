"""
Test for ingredients model
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user():
    """Create and return a new user"""
    user = get_user_model().objects.create_user(
        email='test@example.com',
        password='testpass123',
    )
    return user


class ModelTests(TestCase):

    def test_create_ingredient(self):
        """Test creating an ingredient is successful"""
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Cucumber',
        )

        self.assertEqual(str(ingredient), ingredient.name)
