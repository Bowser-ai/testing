from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/brave'
        self.browser = webdriver.Chrome(options=options)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self) -> None:
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do lists', self.browser.title)
        self.fail("finish the test")


if __name__ == '__main__':
    unittest.main()
