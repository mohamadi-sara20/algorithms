import unittest
from selection import selection_sort
from insertion import insertion_sort
from merge import merge_sort
from merge_nosentinel import merge_nosentinel
import random
from insertion_recursive import insertion_recursive
from insertion_binary import insertion_binary
from p4.inversion import count_inversions
from insertion_decreasing import insertion_sort_decreasing
from p2.bubble_sort import bubble_sort

class TestSort(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSort, self).__init__(*args, **kwargs)
        self.A = [5, 2, 4, 6, 1, 3]
        self.B = [4, 1, 3, 9, 7]
        self.C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.D = [1,2,3,4,5,6]
        self.F = [random.randint(1, 10000) for i in range(2**5)]
        self.F = [random.randint(1, 10000) for i in range(3**3)]


    
    def test_selection(self):
        self.assertEqual(selection_sort(self.A), sorted(self.A))
        self.assertEqual(selection_sort(self.B), sorted(self.B))
        self.assertEqual(selection_sort(self.C), sorted(self.C))
        self.assertEqual(selection_sort(self.D), self.D)
        self.assertEqual(selection_sort(self.F), sorted(self.F))

    def test_insertion(self):
        self.assertEqual(insertion_sort(self.A), sorted(self.A))
        self.assertEqual(insertion_sort(self.B), sorted(self.B))
        self.assertEqual(insertion_sort(self.C), sorted(self.C))
        self.assertEqual(insertion_sort(self.D), self.D)
        self.assertEqual(insertion_sort(self.F), sorted(self.F))
    
    def test_merge(self):
        self.assertEqual(merge_sort(self.A, 0, len(self.A) - 1), sorted(self.A))
        self.assertEqual(merge_sort(self.B, 0, len(self.B) - 1), sorted(self.B))
        self.assertEqual(merge_sort(self.C, 0, len(self.C) - 1), sorted(self.C))
        self.assertEqual(merge_sort(self.D, 0, len(self.D) - 1), self.D)
        self.assertEqual(merge_sort(self.F, 0, len(self.F)-1), sorted(self.F))

    
    def test_merge_nosentinel(self):
        self.assertEqual(merge_nosentinel(self.A, 0, len(self.A) - 1), sorted(self.A))
        self.assertEqual(merge_nosentinel(self.B, 0, len(self.B) - 1), sorted(self.B))
        self.assertEqual(merge_nosentinel(self.C, 0, len(self.C) - 1), sorted(self.C))
        self.assertEqual(merge_nosentinel(self.D, 0, len(self.D) - 1), self.D)
        self.assertEqual(merge_nosentinel(self.F, 0, len(self.F)-1), sorted(self.F))

    def test_insertion_recursive(self):
        self.assertEqual(insertion_recursive(self.A, len(self.A)-1), sorted(self.A))
        self.assertEqual(insertion_recursive(self.B, len(self.B)-1), sorted(self.B))
        self.assertEqual(insertion_recursive(self.C, len(self.C)-1), sorted(self.C))
        self.assertEqual(insertion_recursive(self.D, len(self.D)-1), self.D)
        self.assertEqual(insertion_recursive(self.F, len(self.F)-1), sorted(self.F))

    def test_insertion_binary(self):
        self.assertEqual(insertion_binary(self.A), sorted(self.A))
        self.assertEqual(insertion_binary(self.B), sorted(self.B))
        self.assertEqual(insertion_binary(self.C), sorted(self.C))
        self.assertEqual(insertion_binary(self.D), self.D)
        self.assertEqual(insertion_binary(self.F), sorted(self.F))
    
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.A), sorted(self.A))
        self.assertEqual(bubble_sort(self.B), sorted(self.B))
        self.assertEqual(bubble_sort(self.C), sorted(self.C))
        self.assertEqual(bubble_sort(self.D), self.D)
        self.assertEqual(bubble_sort(self.F), sorted(self.F))
    
    def test_insertion_decreasing(self):
        self.assertEqual(insertion_sort_decreasing(self.A), sorted(self.A, reverse=True))
        self.assertEqual(insertion_sort_decreasing(self.B), sorted(self.B, reverse=True))
        self.assertEqual(insertion_sort_decreasing(self.C), sorted(self.C, reverse=True))
        self.assertEqual(insertion_sort_decreasing(self.D), sorted(self.D, reverse=True))
        self.assertEqual(insertion_sort_decreasing(self.F), sorted(self.F, reverse=True))

    def test_count_inversion(self):
        self.assertEqual(count_inversions([8, 4, 1, 2], 0, 3), 5)
        self.assertEqual(count_inversions([6,5,4,3,2,1], 0, 5), 15)
        self.assertEqual(count_inversions([3], 0, 0), 0)
        self.assertEqual(count_inversions([2, 4, 1, 3, 5], 0, 4), 3)
    
    

if __name__ == "__main__":
    unittest.main()