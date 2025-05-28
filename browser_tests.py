import unittest
from browser_history import *

class TestBrowserHistory(unittest.TestCase):

    def setUp(self):
        self.history = Stack()
        self.history.push("https://page1.com")
        self.history.push("https://page2.com")

    def test_push_url(self):
        self.assertEqual(self.history.peek(),"https://page2.com")


    def test_back(self):
        self.assertEqual(self.history.pop(), "https://page2.com")
        self.assertEqual(self.history.peek(),"https://page1.com")



if __name__ == "__main__":
    unittest.main()