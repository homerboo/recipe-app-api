from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):
  def test_add_numbers(self):
    """ Test that two numbers are added together """
    # Assertion
    self.assertEqual(add(3,8),11)

  def test_subtract_two_numbers(self):
    """ Test that two numbers are subtracted """
    self.assertEqual(subtract(10,7),3) 