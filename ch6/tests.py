import unittest
from heapsort import heapsort
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

    def test_bubble_sort(self):
        self.assertEqual(heapsort(self.A), sorted(self.A))
        self.assertEqual(heapsort(self.B), sorted(self.B))
        self.assertEqual(heapsort(self.C), sorted(self.C))
        self.assertEqual(heapsort(self.D), self.D)
        self.assertEqual(heapsort(self.F), sorted(self.F))


if __name__ == "__main__":
    unittest.main()