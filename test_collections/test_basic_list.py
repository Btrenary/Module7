import unittest
from unittest.mock import patch
from fun_with_collections import basic_list as topic1


class MyTestCase(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value= '5')
    def test_make_list(self, input):
        self.assertEqual(topic1.makelist(), [5, 5, 5])


if __name__ == '__main__':
    unittest.main()
