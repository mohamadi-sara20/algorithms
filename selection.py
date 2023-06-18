import unittest

class TestInsertionSort(unittest.TestCase):
    def test_unsorted(self):
        A = [5, 2, 4, 6, 1, 3]
        B = [4, 1, 3, 9, 7]
        C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(selection_sort(A), [1, 2, 3, 4, 5, 6])
        self.assertEqual(selection_sort(B), [1, 3, 4, 7, 9])
        self.assertEqual(selection_sort(C), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


    def test_sorted(self):
        D = [1,2,3,4,5,6]
        self.assertEqual(selection_sort(D), D)

# Loop Invariant: A[:i]
def selection_sort(A):
    for i in range(len(A)):
        ind_smallest = i
        for j in range(i+1, len(A)):
            if A[j] < A[ind_smallest]:
                ind_smallest = j
        tmp = A[i]
        A[i] = A[ind_smallest]
        A[ind_smallest] = tmp
    return A

if __name__ == "__main__":
    unittest.main()
