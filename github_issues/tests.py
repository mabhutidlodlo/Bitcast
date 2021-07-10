from django.test import TestCase
from rest_framework.test import APITestCase
from django.test import Client
import json

# Create your tests here.
c = Client()

class YourTestClass(TestCase):


    def test_status_code(self):
        response = self.client.get('/issues/mabhutidlodlo/ivent')
        self.assertEqual(response.status_code, 200)

    def test_status_data_pass(self):
        response = self.client.get('/issues/mabhutidlodlo/ivent')
        expected_data = {
          "result": [
             {
                "number": 2,
                "title": "another 1"
              },
              {
            "number": 1,
            "title": "new issue"
            }
          ] 
        }
        self.assertEqual(json.loads(response.content),expected_data)