import unittest
from fun_with_collections import sort_and_search_list


class SearchAndSortTestCase(unittest.TestCase):
    def test_search_list_found(self):
        self.assertTrue(sort_and_search_list.search_list('Ford'))

    def test_search_list_not_found(self):
        result = sort_and_search_list.search_list('Honda')
        self.assertEqual(result, '-1')

    def test_sort_list_(self):
        result = sort_and_search_list.sort_list()
        self.assertEqual(result, ['Chevrolet', 'Dodge', 'Ford', 'Jeep', 'Nissan'])


if __name__ == '__main__':
    unittest.main()
