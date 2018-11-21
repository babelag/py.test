from twitter import Twitter
import pytest

#inicjalizacja backend
@pytest.fixture
def backend(tmpdir):
    tmp_file = tmpdir.join('test.txt)')
    tmp_file.write("")
    return tmp_file

@pytest.fixture(params=['list', 'backend'], name= 'twitter')
def fixture_twitter(backend, request):
    if request.param == 'list':
        twitter = Twitter()
    elif request.param == 'backend':
        twitter = Twitter(backend=backend)
    return twitter



def test_twitter_initialization(twitter):
    assert twitter

def test_tweet_single_message(twitter):
    #When
    twitter.tweet("Test message")
    #Than
    assert twitter.tweet_messages == ["Test message"]

def test_tweet_long_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet("test"*41)
    assert twitter.tweet_messages == []

def test_initializing_two_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    twitter1.tweet('Test 1')
    twitter1.tweet('Test 2')

    assert twitter2.tweet_messages == ['Test 1', 'Test 2']

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
