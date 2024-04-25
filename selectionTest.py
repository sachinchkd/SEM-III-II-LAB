import unittest
from selection import selection

class TestSum(unittest.TestCase):

    def selectionTest(self):

        input_data = [23, 45, 97, 12, 0]
        result = selection(input_data)
        self.assertEqual(result, [12, 23, 45, 97, 0])

        input_data = []
        result = selection(input_data)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()