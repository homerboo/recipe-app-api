from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    """ Creates a new test class """

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'test@testing.com'
        password = 'testpass123'
        # Calls the create user function on the user manager on the user model
        user = get_user_model().objects.create_user(
                email=email,
                password=password)

        self.assertEqual(user.email, email)
        # Cannot check password directly but can use
        #   check_password helper function
        # assertTrue checks a condition
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = 'test@TESTING.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user without an email raises an error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test creating a superuser """
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
