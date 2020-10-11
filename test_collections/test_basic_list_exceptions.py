import unittest
from unittest.mock import patch
from fun_with_collections import basic_list_exceptions as basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_values='5')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [5, 5, 5])

    @patch('fun_with_collections.basic_list.get_input', return_values='ab')  # patch function for input
    def test_make_list_non_numeric(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()  # call the function!

    @patch('fun_with_collections.basic_list.get_input', return_values='-4')  # patch function for input
    def test_make_list_below_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()  # call the function!

    @patch('fun_with_collections.basic_list.get_input', return_values='51')  # patch function for input
    def test_make_list_above_range(self, input):  # pass input
        with self.assertRaises(ValueError):  # this is familiar
            basic_list.make_list()  # call the function!


if __name__ == '__main__':
    unittest.main()
