import unittest
from quicksort import quicksort
import random

class TestSort(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSort, self).__init__(*args, **kwargs)
        self.A = [5, 2, 4, 6, 1, 3]
        self.B = [4, 1, 3, 9, 7]
        self.C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.D = [1,2,3,4,5,6]
        self.F = [random.randint(1, 10000) for i in range(2**5)]
        self.F = [random.randint(1, 10000) for i in range(3**3)]

    def test_quick_sort(self):
        self.assertEqual(quicksort(self.A), sorted(self.A))
        self.assertEqual(quicksort(self.B), sorted(self.B))
        self.assertEqual(quicksort(self.C), sorted(self.C))
        self.assertEqual(quicksort(self.D), self.D)
        self.assertEqual(quicksort(self.F), sorted(self.F))
    
    def test_quick_sort_decreasing(self):
        self.assertEqual(quicksort(self.A, descending=True), sorted(self.A, reverse=True))
        self.assertEqual(quicksort(self.B, descending=True), sorted(self.B, reverse=True))
        self.assertEqual(quicksort(self.C, descending=True), sorted(self.C, reverse=True))
        self.assertEqual(quicksort(self.D, descending=True), sorted(self.D, reverse=True))
        self.assertEqual(quicksort(self.F, descending=True), sorted(self.F, reverse=True))



if __name__ == "__main__":
    unittest.main()