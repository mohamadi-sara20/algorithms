class BiStack():
    def __init__(self, A):
        self._A = A
        self._len1 = 0
        self._len2 = 0

    def push(self, stack_no, x):
        if self._len1 + self._len2 == len(self._A):
            raise Exception('stack overflow')
        if stack_no == '1':
            self._A[self._len1] = x
            self._len1 += 1
        elif stack_no == '2':
            self._A[len(self._A) - self._len2 - 1] = x
            self._len2 += 1

    def pop(self, stack_no):
        if self._len1 + self._len2 == 0:
            raise Exception('stack underflow')
        if stack_no == '1':
            el = self._A[self._len1 - 1] 
            self._A[self._len1 - 1] = 0
            self._len1 -= 1
            return el
        
        elif stack_no == '2':
            el = self._A[len(self._A) - self._len2]
            self._A[len(self._A) - self._len2 ] = 0
            self._len2 -= 1
            return el

    def __str__(self) -> str:
        res = ','.join(str(x) for x in self._A)
        return res

# A = BiStack([0 for i in range(5)])
# # A.push('1', 5)
# # A.push("2", 7)
# # A.push("2", 9)
# # A.push('1', 10)
# # A.push('1', 12)
# # print(A)
# # print(A.pop("1"))
# # print(A)
# # print(A.pop("2"))
# # print(A)
# # print(A.pop("1"))
# # print(A)
# # print(A.pop("2"))
# # print(A)
# # print(A.pop("1"))

# A.push("2", 5)
# print(A.pop("2"))
# print(A)