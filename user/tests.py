from rest_framework.test import APITestCase
from rest_framework import status

class UserTest(APITestCase):

    def test_post_question(self):
        _data = {
            "username": "tahsin",
            "full_name": "Tahsin Iftekar",
            "email": "tahsiniftekhar@gmail.com",
            "phone": "01795067044"
        }

        _response = self.client.post('/api/user', data = _data, format="json")
        _data = _response.json()
        self.assertEqual(_response.status_code, status.HTTP_201_CREATED)

    def test_get_question(self):
        _response = self.client.get('/api/user')
        _data = _response.json()

        self.assertEqual(_response.status_code, status.HTTP_200_OK)