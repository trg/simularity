import unittest
import os

import brain

class TestBrain(unittest.TestCase):

    def setUp(self):
        brainfile = os.path.join(
                        os.path.dirname(
                            os.path.realpath(__file__)
                        ), 'braintest.shelve'
                     )
        self.brain = brain.Brain(brainfile = brainfile)

        # Set up some dummy data:
        self.brain.learn(['alpha', 'beta', 'delta', 'gamma'])
        self.brain.learn(['alpha', 'beta',])
        self.brain.learn(['alpha', 'beta', 'gamma'])


    def test_most_popular_hashtag_for_hashtag(self):
        self.assertIs(self.brain.most_popular_hashtag_for_hashtag('alpha'), 'beta')