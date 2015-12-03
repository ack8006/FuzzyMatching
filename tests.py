import fuzzy
import unittest

class TestFuzzyMatching(unittest.TestCase):
    def test_ratio_1(self):
        x = 'test'
        y = 'test'
        assert(fuzzy.ratio(x,y) == 1.0)
    def test_ratio_2(self):
        x = 'test'
        y = 'TEST'
        assert(fuzzy.ratio(x,y) == 0.0)
    def test_ratio_3(self):
        x = 'this is very similar'
        y = 'this is very similer'
        assert(fuzzy.ratio(x,y) > 0.9)
    def test_ratio_4(self):
        x = 'this is not very similar'
        y = 'here lies a random diff string'
        assert(fuzzy.ratio(x,y) < 0.5)

    def test_partial_1(self):
        x = 'this is longer'
        y = 'is lo'
        assert(fuzzy.partial_ratio(x,y) == 1.0)
    def test_partial_2(self):
        x = 'front matchers'
        y = 'front'
        assert(fuzzy.partial_ratio(x,y) == 1.0)
    def test_partial_3(self):
        x = 'matchbackend'
        y = 'backend'
        assert(fuzzy.partial_ratio(x,y) == 1.0)
    def test_partial_4(self):
        x = 'reverse'
        y = 'the reverse is longer'
        assert(fuzzy.partial_ratio(x,y) == 1.0)
    def test_partial_5(self):
        x = 'hump'
        y = 'the reverse is longer'
        assert(fuzzy.partial_ratio(x,y) < 0.5)

