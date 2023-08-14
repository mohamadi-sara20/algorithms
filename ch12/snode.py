class SNode:
    def __init__(self, k, left, right, s=None):
        self.key = k
        self.left = left
        self.right = right
        self._s = s
    
    @property
    def s(self):
        return self._s
    @s.setter
    def s(self, s):
        self._s = s
    @staticmethod
    def search(x, z):
        while x is not None and x.key != z.key:
            if z.key < x.key:
                x = x.left
            else: 
                x = x.right
        return x


    @staticmethod
    def get_parent(self, x)
    @staticmethod
    def tree_insert(T, z, p):
        if T is None:
            z.p = p
            if p.key < z.key:
                p.right = z
            else:
                p.left = z 
        else:
            if z.key < T.key:
                SNode.tree_insert(T.left, z, T)
            else:
                SNode.tree_insert(T.right, z, T)
          
            
if __name__ == "__main__":
    #      10
    #   4      17
    # 1   5   16  21

    n1 = SNode(k=1, left=None, right=None)
    n5 = SNode(k=5, left=None, right=None)
    n16 = SNode(k=16, left=None, right=None)
    n21 = SNode(k=21, left=None, right=None)
    n4 = SNode(k=4, left=n1, right=n5)
    n17 = SNode(k=17, left=n16, right=n21)
    r = SNode(k=10, left=n4, right=n17)
    n1.s = n4
    n5.s  = r
    n4.s = n5
    n17.s = n21
    n16.s = n17
    r.s = n16
    