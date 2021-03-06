import unittest


def find_rotation_point(words):

    # Find the rotation point in the list

    floor_index = 0
    ceiling_index = len(words)-1

    while (ceiling_index > floor_index):
        half_index = (ceiling_index+floor_index)//2
        if ord(words[floor_index][0]) > ord(words[half_index][0]):
            ceiling_index = half_index 
        else:
            floor_index = half_index

        if (ceiling_index-floor_index == 1):
            return ceiling_index
            

    return -1
    


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)