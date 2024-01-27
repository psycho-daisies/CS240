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
    def __init__(self, size=None):  # Constructor for Stack
        if size is not None:
            self.items = []
            self.max_size = size
        else:
            # Default constructor
            self.items = []
            
    # Push adds an item to the top of the Stack; except if the Stack is full
    def Push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            print(f"Can't add {item} to a full stack! ")
    # Pop removes the from the top of the stack
    def Pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Can't pop from an empty Stack!")

    # Returns True if the stack is empty
    def IsEmpty(self):
        return len(self.items) == 0

    # Returns True if the Stack is full
    def IsFull(self):
        return len(self.items) == self.max_size

    # 
    def Peek(self):
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



print("Take a PEEK at the top of the stack:", array_stack.peek())
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
