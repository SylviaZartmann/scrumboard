import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CustomUser
from rest_framework.authtoken.models import Token

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = CustomUser.objects.create_user(**self.user_data)
        self.login_url = '/login/'
        self.logout_url = '/logout/'

    def test_registration(self):
        response = self.client.post('/register/', data=self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        response = self.client.post(self.login_url, data={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', json.loads(response.content))

    def test_login_with_email(self):
        response = self.client.post(self.login_url, data={'username': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', json.loads(response.content))

    def test_logout(self):
        login_response = self.client.post(self.login_url, data={'username': 'testuser', 'password': 'testpassword'})
        token = json.loads(login_response.content)['token']

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)