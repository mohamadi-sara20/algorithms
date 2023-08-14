#### Impelement a queue with a singly linked list
class Node:
    def __init__(self, x, next=None) -> None:
        self.x = x
        self.next = next
    def __str__(self) -> str:
        return f'{self.x}'

class Queue:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None
    
    def enqueue(self, x):
        if self.size == 0:
            self.head = Node(x, next=None)
            self.tail = self.head
        else: 
            newNode = Node(x, next=None)
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return 'queue empty'
        top = self.head
        self.head = self.head.next
        self.size -= 1
        return top.x
    
    def __str__(self) -> str:
        vals = ''
        node = self.head
        while node:
            vals += f"{node.x},"
            node = node.next
        return vals
    

# q = Queue()
# q.enqueue(1)
# print(q)
# q.enqueue(2)
# q.enqueue(3)
# print(q)
# print(q.dequeue())
# print(q)
# print(q.dequeue())
# print(q)
