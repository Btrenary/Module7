import unittest
from fun_with_collections import sort_and_search_array


class SortAndSearchTestCase(unittest.TestCase):
    def test_search_array_found(self):
        self.assertTrue(sort_and_search_array.search_array('Reds'))

    def test_search_array_not_found(self):
        result = sort_and_search_array.search_array('Yankees')
        self.assertEqual(result, '-1')

    def test_sort_array_(self):
        result = sort_and_search_array.sort_array()
        self.assertEqual(result, ['Brewers', 'Cardinals', 'Cubs', 'Pirates', 'Reds'])


if __name__ == '__main__':
    unittest.main()
