#### Impelement a stack with a singly linked list
class Node:
    def __init__(self, x, next=None) -> None:
        self.x = x
        self.next = next
    def __str__(self) -> str:
        return f'{self.x}'

class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
    
    def push(self, x):
        prev_head = self.head
        self.head = Node(x, next=prev_head)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return 'stack empty'
        top = self.head
        self.head = self.head.next
        self.size -= 1
        return top
    
    def __str__(self) -> str:
        vals = ''
        node = self.head
        while node:
            vals += f"{node.x},"
            node = node.next
        return vals
    

# stack = Stack()
# stack.push(1)
# stack.push(2)
# print(stack)
# stack.push(3)
# print(stack)
# print(stack.pop())
# print(stack)
