# Test client that allows test requests to the app in our unit tests
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
# Helper function to generate urls for django admin page
from django.urls import reverse


class AdminSiteTests(TestCase):

    # set up function runs before any other test is run
    def setUp(self):
        # Test client
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='menwa.codes@gmail.com',
            password='password123')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@tTEST.com',
            password='password123',
            name='Sammy')

    def test_users_listed(self):
        """ Test that users are listed on user page """
        # Reverse used to dyamically get FQDN
        #  Can update the url here and not update everywhere in the tests
        url = reverse('admin:core_user_changelist')
        # response based on above url via HTTP GET
        resp = self.client.get(url)
        # assertContains
        #  Custom django assertion that checks response for a given item
        #  Also checks for response 200
        self.assertContains(resp, self.user.name)
        self.assertContains(resp, self.user.email)

    def test_user_change_page(self):
        """ Test that the user edit page works """
        # Gen the url
        url = reverse('admin:core_user_change', args=[self.user.id])
        # Get a response
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_user_page(self):
        """ Test that the user add page works """
        url = reverse('admin:core_user_add')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
