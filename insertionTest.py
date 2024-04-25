import unittest
from insertion import insertion

class TestSum(unittest.TestCase) :

    def insertionTest(self):

        input_data = [12, 23, 45, 97]
        result = insertion(input_data)
        self.assertEqual(result, [12, 23, 45, 97])

        input_data = []
        result = insertion(input_data)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()