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
    def __init__(self, max_size=None):
        self.head = None
        self.size = 0
        self.max_size = max_size

    # Push a new node onto the stack / linked list
    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.size = self.size + 1
            self.head = node
        elif self.size < self.max_size:
            self.size = self.size + 1
            current = self.head
            self.head = node
            self.head.next = current
        else:
            print("Can't add to a full stack!")

    # Pop from the top of the stack
    def pop(self):
        if not self.is_empty():
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item
        else:
            print("Can't Pop from an empty stack!")

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.size == self.max_size

    # Peek at the top of the stack
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("Can't Peek! ~ Stack is Empty")

    # Returns the size of the list
    def get_list_size(self):
        return self.size

    # Counts the number of elements in the list
    def count_size(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        self.size = counter  # update size
        return int(counter)


s = Stack(5)
s.push(1)
print(s.peek())
s.push(2)
s.push(3)
s.push(4)
s.push(4)


print(f"Size : {s.count_size()}")
print(f"Total size: {s.max_size}")
print(f"Is full?  {s.is_full()}")
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()

print(f"Is empty?  {s.is_empty()}")
