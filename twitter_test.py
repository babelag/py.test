from twitter import Twitter
import pytest

@pytest.fixture
def twitter():
    twitter = Twitter()
    yield twitter
    twitter.delete()

def test_twitter_initialization(twitter):
    assert twitter

def test_tweet_single_message(twitter):
    #When
    twitter.tweet("Test message")
    #Than
    assert twitter.tweets == ["Test message"]

def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet("test"*41)
    assert twitter.tweets == []

# def test_tweet_with_hashtag():
#     twitter = Twitter()
#     message = "This is #first message"
#     twitter.tweet(message)
#     assert "first" in twitter.find_hashtag(message)
#
#
# def test_tweet_with_hashtag_on_beginning():
#     twitter = Twitter()
#     message = "#first This is message"
#     twitter.tweet(message)
#     assert "first" in twitter.find_hashtag(message)
#
# def test_tweet_with_hashtag_on_uppercase():
#     twitter = Twitter()
#     message = "#FIRST This is message"
#     twitter.tweet(message)
#     assert "FIRST" in twitter.find_hashtag(message)
#
# @pytest.mark.parametrize("message, hashtag", (
#     ("This is #first message", "first"),
#     ("#first This is message", "first"),
#     ("#FIRST This is message", "FIRST")
#                          ))
# def test_tweet_with_hashtag(message, hashtag):
#     twitter = Twitter()
#     assert hashtag in twitter.find_hashtag(message)
#
#
@pytest.mark.parametrize("message, expected", (
                                    ("This is #first message", ["first"]),
                                    ("#first This is message", ["first"]),
                                    ("#FIRST This is message", ["FIRST"]),
                                    ("#FIRST #SECOND This is message", ["FIRST", "SECOND"])
                                    ))

def test_tweet_with_hastag_expected(twitter, message, expected):
    assert twitter.find_hashtag(message) == expected


# @pytest.mark.parametrize("message, expected", (
#                                     ("This is #first message", ["first"]),
#                                     ("#first This is message", ["first"]),
#                                     ("#FIRST This is message", ["first"]),
#                                     ("#FIRST #SECOND This is message", ["first", "second"])
#                                     ))
#
# def test_tweet_with_hastag_expected(twitter, message, expected):
#     assert twitter.find_hashtag_small_letters(message) == expected
