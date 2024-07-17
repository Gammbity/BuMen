from django.test import TestCase
from user import models


class UserTest(TestCase):

    def test_user_create(self):
        user = {
            'first_name': 'Ali',
            'last_name': 'Aliyev',
            'email': 'ali@gmail.com',
            'phone': '+998997776655',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post('/api/v1/user/user/create/', data=user)
        self.assertEqual(response.status_code, 201)
