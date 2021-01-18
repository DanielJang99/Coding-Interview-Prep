import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    
    length1 = len(my_list)
    length2 = len(alices_list)
    
    length = length1 + length2
    # merged_list = [None] * length
    merged_list = []

    index_mine = 0
    index_alices = 0
    index_merged = 0
    
    while index_merged < length: 
        is_my_list_exhausted = index_mine >= length1
        is_alices_list_exhausted = index_alices >= length2
        
        if (not is_my_list_exhausted and (is_alices_list_exhausted or my_list[index_mine] < alices_list[index_alices])):
            merged_list.append(my_list[index_mine])
            index_mine += 1
        else:
            merged_list.append(alices_list[index_alices])
            index_alices += 1
        index_merged += 1


    return merged_list


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)