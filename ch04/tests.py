import unittest
from maxsubarray import maxsubarray_bruteforce, maxsubarray, maxsubarray_bfbase, maxsubarray_kadane

class TestCh4(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCh4, self).__init__(*args, **kwargs)
        self.A = [-1, 2, 4, -3, 5, -6]
        self.B = [5,4,-1,7,8]
        self.C = [-2,1,-3,4,-1,2,1,-5,4]
        self.D = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    
    def test_maxsubarray(self):
        self.assertEqual(maxsubarray_bruteforce(self.A), maxsubarray(self.A, 0, len(self.A)-1))
        self.assertEqual(maxsubarray_bruteforce(self.B), maxsubarray(self.B, 0, len(self.B)-1))
        self.assertEqual(maxsubarray_bruteforce(self.C), maxsubarray(self.C, 0, len(self.C)-1))
        self.assertEqual(maxsubarray_bruteforce(self.A), maxsubarray_bfbase(self.A, 0, len(self.A)-1))
        self.assertEqual(maxsubarray_bruteforce(self.B), maxsubarray_bfbase(self.B, 0, len(self.B)-1))
        self.assertEqual(maxsubarray_bruteforce(self.C), maxsubarray_bfbase(self.C, 0, len(self.C)-1))
        self.assertEqual(maxsubarray_bruteforce(self.D), maxsubarray_bfbase(self.D, 0, len(self.D)-1))
        self.assertEqual(maxsubarray_bruteforce(self.A), maxsubarray_kadane(self.A))
        self.assertEqual(maxsubarray_bruteforce(self.B), maxsubarray_kadane(self.B))
        self.assertEqual(maxsubarray_bruteforce(self.C), maxsubarray_kadane(self.C))
        self.assertEqual(maxsubarray_bruteforce(self.D), maxsubarray_kadane(self.D))

        return

if __name__ == "__main__":
    unittest.main()