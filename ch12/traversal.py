class Node:
    def __init__(self, k, left, right, p=None):
        self.key = k
        self.left = left
        self.right = right
        self._p = p
    
    @property
    def p(self):
        return self._p
    @p.setter
    def p(self, p):
        self._p = p
    @staticmethod
    def in_order(x):
        if x is not None:
            Node.in_order(x.left)
            print(x.key, end=',')
            Node.in_order(x.right)
    @staticmethod
    def post_order(x):
        if x is not None:
            Node.post_order(x.left)
            Node.post_order(x.right)
            print(x.key, end=',')
    @staticmethod
    def pre_order(x):
        if x is not None:
            print(x.key, end=',')
            Node.pre_order(x.left)
            Node.pre_order(x.right)

    @staticmethod
    def tree_min(x):
        if x.left is None:
            return x
        if x.left is not None:
            x = x.left
            return Node.tree_min(x)

    @staticmethod  
    def tree_max(x):
        if x.right is None:
            return x
        if x.left is not None:
            x = x.right
            return Node.tree_max(x)


    @staticmethod
    def tree_predecessor(x):
        if x.left is not None:
            return Node.tree_max(x.left)
        y = x.p
        while y is not None and x == y.left:
            x = y
            y = y.p
        return y 

    @staticmethod
    def tree_successor(x):
        if x.right is not None:
            return Node.tree_min(x.right)
        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y 

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
                Node.tree_insert(T.left, z, T)
            else:
                Node.tree_insert(T.right, z, T)
            

if __name__ == "__main__":
    #      10
    #   4      17
    # 1   5   16  21

    n1 = Node(k=1, left=None, right=None)
    n5 = Node(k=5, left=None, right=None)
    n16 = Node(k=16, left=None, right=None)
    n21 = Node(k=21, left=None, right=None)
    n4 = Node(k=4, left=n1, right=n5)
    n17 = Node(k=17, left=n16, right=n21)
    r = Node(k=10, left=n4, right=n17)
    n1.p = n4
    n5.p  = n4
    n4.p = r
    n17.p = r
    n16.p = n17
    n21.p = n17
    # print("in order traversal:")
    # Node.in_order(r)
    # print("\n")
    # print("pre order traversal:")
    # Node.pre_order(r)
    # print("\n")
    # print("post order traversal:")
    # Node.post_order(r)
    # print(Node.tree_predecessor(r).key)
    # print(Node.tree_successor(r).key)
    z = Node(left=None, right=None, k=0, p=None)
    r.tree_insert(r, z, r.p)
    Node.in_order(r)
    print("\n")
    z = Node(left=None, right=None, k=6, p=None)
    r.tree_insert(r, z, r.p)
    Node.in_order(r)
    print("\n")
    z = Node(left=None, right=None, k=22, p=None)
    r.tree_insert(r, z, r.p)
    Node.in_order(r)
    print("\n")