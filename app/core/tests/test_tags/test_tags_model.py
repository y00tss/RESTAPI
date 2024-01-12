"""
Test for tags models
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

    def test_create_tag(self):
        """Test creating a new tag"""
        user = create_user()
        tag = models.Tag.objects.create(
            user=user,
            name='Vegan',
        )

        self.assertEqual(str(tag), tag.name)
