from django.test import TestCase

# Create your tests here.
class SanpleTestCase(TestCase):
    def test_sample(self):
        self.assertEqual(1+2 , 3)