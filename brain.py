#!/usr/bin/env python

import signal
import sys
import shelve
import os

DEFAULT_SHELVEFILE = os.path.join(
                        os.path.dirname(
                            os.path.realpath(__file__)
                        ), 'hashtags.shelve'
                     )

class Brain:

    def __init__(self, filepath=DEFAULT_SHELVEFILE):
        self.db = shelve.open(filepath, writeback=True)
        signal.signal(signal.SIGINT, self.signal_handler)


    # API

    def learn(self, hashtag_list):
        """ Consumes sets of hashtags, eg: ['foo', 'bar', 'baz'] """
        for tag_1 in hashtag_list:
            for tag_2 in hashtag_list:
                if tag_1 != tag_2:
                    self._associate_tag_with_tag(tag_1, tag_2)
        self.sync()

    def most_popular_hashtag_for_hashtag(self, hashtag):
        max_tag_value = 0
        most_popular_tag = None
        if self.db.has_key(hashtag):
            associate_array = self.db[hashtag]
            for hashtag in associate_array:
                hashtag_count = associate_array[hashtag]
                if hashtag_count > max_tag_value:
                    max_tag_value = hashtag_count
                    most_popular_tag = hashtag

        return most_popular_tag

    # Shelve Utils

    def sync(self):
        """ Syncs the DB to the filesystem """
        self.db.sync()

    def close(self):
        """ Syncs + Closes the db """
        self.db.close()

    def signal_handler(self, signal, frame):
        self.close()
        sys.exit(0)


    # Utility Methods

    def _find_or_create_with_key(self, key):
        if not self.db.has_key(key):
            self.db[key] = {}
        return self.db[key]

    def _associate_tag_with_tag(self, tag_1, tag_2):
        associate_array = self._find_or_create_with_key(tag_1)
        if associate_array.has_key(tag_2):
            associate_array[tag_2] += 1
        else:
            associate_array[tag_2] = 1

#
# Console Usage:
# python brain.py somehashtaghere
#

if __name__ == "__main__":
    b = Brain()
    hashtag = sys.argv[1]
    print(b.db[hashtag])
    print(b.most_popular_hashtag_for_hashtag(hashtag))



