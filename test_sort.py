import unittest
from selection import selection_sort
from insertion import insertion_sort
from bubble import *

class TestInsertionSort():
    def __init__(self):
        self.A = [5, 2, 4, 6, 1, 3]
        self.B = [4, 1, 3, 9, 7]
        self.C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.D = [1,2,3,4,5,6]

    
    def test_selection(self):
        self.assertEqual(selection_sort(self.A), [1, 2, 3, 4, 5, 6])
        self.assertEqual(selection_sort(self.B), [1, 3, 4, 7, 9])
        self.assertEqual(selection_sort(self.C), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(selection_sort(self.D), self.D)

    def test_insertion(self):
        self.assertEqual(insertion_sort(self.A), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insertion_sort(self.B), [1, 3, 4, 7, 9])
        self.assertEqual(insertion_sort(self.D), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(insertion_sort(self.D), self.D)
    


if __name__ == "__main__":
    unittest.main()