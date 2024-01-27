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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, max_size=None):
        self.head = None
        self.size = 0
        self.max_size = max_size

    # Push adds an item to the top of the Stack; except if the Stack is full
    def Push(self, data):
        if self.size == self.max_size:
            return print(f"Can't add {data} to a full stack! ")

        node = Node(data=data)
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            self.head.next = node.next

    # Pop removes from the top of the stack; the first node of the list
    def Pop(self):
        if self.head is None:
            return print("Can't Pop! ~ Stack is Empty!")
        self.size = self.size - 1
        popped = self.head
        self.head = self.head.next
        return popped.data

    # Returns True if the Stack is empty
    def IsEmpty(self):
        return self.head is None

    # Returns True if the Stack is full by checking size of Linked List to max Stack size
    def IsFull(self):
        return self.max_size == self.size

    # Peek looks at the top of Stack but does not Pop
    def Peek(self):
        if self.head is None:
            return print("Can't Peek! ~ Stack is Empty")
        return self.head.data

    # Returns the size of the Stack
    def get_size(self):
        return self.size

    # Counts each node in the Stack and returns the size
    def count_nodes(self):
        current = self.head
        counter = 0
        if current is None:
            return 0
        else:
            while current:
                counter += 1
                current = current.next
        self.size = counter  # update size
        return int(counter)


# Testing the Stack functions
test_stack = Stack(5)
print(test_stack.IsEmpty())
print(f"Current size of Stack: ", test_stack.get_size())
test_stack.Push(1)
test_stack.Push(2)
test_stack.Push(3)
test_stack.Push(4)
print(f"Is the Stack full? ", test_stack.IsFull())
test_stack.Push(5)
test_stack.Push(6)
print(f"Current size of Stack: ", test_stack.get_size())
print(f"Is the Stack Empty? ", test_stack.IsEmpty())
print(f"Is the Stack full? ", test_stack.IsFull())
print("Take a PEEK at the top of the stack:", test_stack.Peek())
print("Popped item: ", test_stack.Pop())
print("Take a PEEK at the top of the stack:", test_stack.Peek())
print("Popped item: ", test_stack.Pop())
print("Take a PEEK at the top of the stack:", test_stack.Peek())
print("Popped item: ", test_stack.Pop())
print(f"Is the Stack Empty? ", test_stack.IsEmpty())
print(f"Current size of Stack: ", test_stack.get_size())
