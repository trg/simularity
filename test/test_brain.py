import unittest
import os

from .. import brain

class TestBrain(unittest.TestCase):

    def setUp(self):
        self.brainfilepath = os.path.join(
                        os.path.dirname(
                            os.path.realpath(__file__)
                        ), 'braintest.shelve'
                     )
        # Remove old test data first
        if os.path.exists(self.brainfilepath):
            os.remove(self.brainfilepath)
        self.brain = brain.Brain(filepath = self.brainfilepath)

        # Set up some dummy data:
        self.brain.learn(['alpha', 'beta', 'delta', 'gamma'])
        self.brain.learn(['alpha', 'beta',])
        self.brain.learn(['alpha', 'beta', 'gamma'])

    def tearDown(self):
        os.remove(self.brainfilepath + ".db")

    def test_most_popular_hashtag_for_hashtag(self):
        assert self.brain.most_popular_hashtag_for_hashtag('alpha') == 'beta'
        assert self.brain.most_popular_hashtag_for_hashtag('beta') == 'alpha'
        assert self.brain.most_popular_hashtag_for_hashtag('delta') == 'alpha'
        assert self.brain.most_popular_hashtag_for_hashtag('gamma') == 'alpha'
