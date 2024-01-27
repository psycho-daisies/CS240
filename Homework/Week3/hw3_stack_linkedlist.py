"""
Stack / Linked List
Troy Brunette
CS240

Implement a stack for both a Linked List & Array. Use your HW 1 implementation of a Linked List.

    Push
    Pop
    IsEmpty
    IsFull
    Peek
"""

"""
Stack / Linked List
Troy Brunette
CS240

Implement a stack for both a Linked List & Array. Use your HW 1 implementation of a Linked List.

    Push
    Pop
    IsEmpty
    IsFull
    Peek
"""
from node import Node


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # Add a new node to the front of list
    def Push(self, data):
        node = Node(data=data)
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            self.head.next = node.next

    # Removes the first node
    def Pop(self):
        if self.head is None:
            return
        self.size = self.size - 1
        popped = self.head
        self.head = self.head.next
        return popped.data

    def IsEmpty(self):
        pass

    def IsFull(self):
        pass

    def Peek(self):
        pass

# Testing the Stack functions
test_stack = Stack()
test_stack.Push(1)
test_stack.Push(2)
test_stack.Push(3)

print(test_stack.Pop())
