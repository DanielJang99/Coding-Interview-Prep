import unittest


def highest_product_of_3(list_of_ints):
    
    if len(list_of_ints) < 3:
        raise ValueError('Getting highest product requires at least three integers')

    # Calculate the highest product of three numbers
    
    highest_product_of_2_max = max(list_of_ints[0], list_of_ints[1], list_of_ints[2])
    lowest_product_of_2_min = min(list_of_ints[0], list_of_ints[1], list_of_ints[2]) 

    highest_product_of_2_min = 0 
    lowest_product_of_2_max = 0

    for i in range(3):
        if (list_of_ints[i]!=highest_product_of_2_max) and (list_of_ints[i] != lowest_product_of_2_min):
            highest_product_of_2_min = list_of_ints[i]
            lowest_product_of_2_max = list_of_ints[i]

    highest_product_of_2 = max(list_of_ints[0]*list_of_ints[1], list_of_ints[1]*list_of_ints[2], list_of_ints[0]*list_of_ints[2])
    lowest_product_of_2 = min(list_of_ints[0]*list_of_ints[1], list_of_ints[1]*list_of_ints[2], list_of_ints[0]*list_of_ints[2])
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    for val in list_of_ints[3:]:
        if highest_product_of_3 < highest_product_of_2 * val:
            highest_product_of_3 = highest_product_of_2 * val 
            if val > highest_product_of_2_max: 
                highest_product_of_2_min = highest_product_of_2_max
                highest_product_of_2_max = val 
            elif val > highest_product_of_2_min:
                highest_product_of_2_min = val 
            highest_product_of_2 = highest_product_of_2_max * highest_product_of_2_min
        elif highest_product_of_3 < lowest_product_of_2 * val:
            highest_product_of_3 = lowest_product_of_2 * val
            if val < lowest_product_of_2_min:
                lowest_product_of_2_max = lowest_product_of_2_min
                lowest_product_of_2_min = val 
            elif val < lowest_product_of_2_max:
                lowest_product_of_2_max = val 
            lowest_product_of_2 = lowest_product_of_2_max * lowest_product_of_2_min
    
    return highest_product_of_3





#Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)
