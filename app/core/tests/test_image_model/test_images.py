"""
Test for ingredients model
"""
from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from core import models


def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)


class ModelTests(TestCase):
    """Test for images model"""
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.client.force_authenticate(user=self.user)

    @patch('core.models.uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test_uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads/recipe/{uuid}.jpg')
