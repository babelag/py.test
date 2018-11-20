import re
import os


class Twitter(object):
    version = '1.0'

    def __init__(self, backend=None):
        self.backend = backend
        self._tweets = []
        if self.backend and not os.path.exists(self.backend):
            with open(self.backend,'w'):
                pass

    def tweet(self, message):
        if len(message)>160:
            raise Exception("This message is to long")
        self.tweets.append(message)
        if self.backend:
            with open(self.backend, 'w') as twitter_file:
                twitter_file.write("\n".join(self.tweets))

    @property
    def tweets(self):
        if self.backend and not self._tweets:
            with open(self.backend) as twitter_file:
                self._tweets = [line.rstrip('\n') for line in twitter_file]
        return self._tweets

    def delete(self):
        if self.backend:
            os.remove(self.backend)

    def find_hashtag(self, message):
        return re.findall("#(\w+)", message)

    def find_hashtag_small_letters(self, message):
        return [m.lower() for m in re.findall('#(\w+)', message)]