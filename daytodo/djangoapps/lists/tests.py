from django.test import TestCase
from django.urls import resolve
from djangoapps.lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/') #function to map
		self.assertEqual(found.func,home_page) #match function called and the one that should be.

