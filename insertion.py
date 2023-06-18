import unittest

class TestInsertionSort(unittest.TestCase):
    def test_unsorted(self):
        A = [5, 2, 4, 6, 1, 3]
        B = [4, 1, 3, 9, 7]
        C = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort(A), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insertion_sort(B), [1, 3, 4, 7, 9])
        self.assertEqual(insertion_sort(C), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


    def test_sorted(self):
        D = [1,2,3,4,5,6]
        self.assertEqual(insertion_sort(D), D)


# Loop Invariant: A[0 : i-1] is always sorted
def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        # Start from the end of the loop invariant to find where to insert the new element
        j = i - 1
        # While we reach the first element and the element at hand is bigger than than A[i]
        while j >= 0 and A[j] > key:
            # Move the element at hand one to the right
            A[j+1] = A[j]
            # Go back one element in the loop invariant
            j -= 1 
        # When the element at hand (j) is not bigger than A[i], then the place to insert j is found. It is not j 
        # (because A[j] < A[i]), rather j+1. 
        A[j+1] = key
    return A



if __name__ == "__main__":
    unittest.main()