"""
Stack / Array
Troy Brunette
CS240

Implement a stack for both a Linked List & Array. Use your HW 1 implementation of a Linked List.

    Push
    Pop
    IsEmpty
    IsFull
    Peek
"""


class Stack:
    def __init__(self, size=None):
        if size is not None:
            self.items = []
            self.max_size = size
        else:
            # Default constructor
            self.items = []

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print(f"Can't add {item} to a full stack! ")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Can't pop from an empty Stack!")

    def custom_pop(self):
        if not self.is_empty():
            popped_item = self.items[-1]
            del self.items[-1]
            return popped_item
        else:
            print("Can't pop from an empty Stack!")

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.max_size

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Can't Peek! ~ Stack is Empty")

    def size(self):
        return len(self.items)


# Example usage:
array_stack = Stack(4)
array_stack.push(1)
print("Top element:", array_stack.peek())

array_stack.push(2)


array_stack.custom_pop()
print("Top element:", array_stack.peek())
array_stack.pop()

print("Is the stack full?", array_stack.is_full())

print("Stack size:", array_stack.size())
array_stack.push(3)
array_stack.push(4)
array_stack.push(5)
array_stack.push(5)
array_stack.push(5)
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
print("Stack size:", array_stack.size())
print("Is the stack full?", array_stack.is_full())
