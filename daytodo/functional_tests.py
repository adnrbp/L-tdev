from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		#exits site
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		#Go to homepage
		self.browser.get('http://localhost:8000')

		#page title and header say: "to-do Lists"
		#incorporates the print of actual browser.title
		self.assertIn('To-Do', self.browser.title)
		self.fail("Finish the test!")
		#enter a to-do item straight away

		#types an item in text box (hobby)
		#hits enter, page updates, page lists: 1:"item"



		#textbox: add anorther item. he types another.
		#page updates, show both items in list

		#site remember items? generated unique URL for him
		#visit and they are still there.

if __name__ == '__main__':
	unittest.main(warnings='ignore')