import unittest
from twitter import Twitter


class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()

    def test_initialization(self):
        self.assertTrue(self.twitter)

    def test_tweet(self):
        #When
        self.twitter.tweet("Test message")
        #Then
        self.assertEqual(self.twitter.tweets, ["Test message"])
        self.assertEqual(self.twitter.tweets, ["Test mesage"])



if __name__ == '__main__':
    unittest.main()
