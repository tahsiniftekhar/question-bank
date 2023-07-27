from rest_framework.test import APITestCase
from rest_framework import status

class QuestionTest(APITestCase):

    def test_post_question(self):
        _data = {
            "question": "Sum of 3+3 = ?",
            "option1": "2",
            "option2": "4",
            "option3": "5",
            "option4": "6",
            "option5": "8",
            "answer": 6,
            "explain": "3+3=6"
        }

        _response = self.client.post('/api/question', data = _data, format="json")
        _data = _response.json()
        self.assertEqual(_response.status_code, status.HTTP_201_CREATED)

    def test_get_question(self):
        _response = self.client.get('/api/question')
        _data = _response.json()

        self.assertEqual(_response.status_code, status.HTTP_200_OK)