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
            self.items = [None] * size
            self.max_size = size
        else:
            self.items = []
            self.max_size = size


    # Push adds an item to the top of the Stack; except if the Stack is full
    def Push(self, item):
        if not self.IsFull():
            self.items.append(item)
        else:
            print(f"Can't add {item} to a full stack! ")

    # Pop removes from the top of the stack
    def Pop(self):
        if not self.IsEmpty():  # If stack is not empty we Pop
            return self.items.pop()
        else:
            print("Can't Pop! ~ Stack is Empty!")

    # Returns True if the stack is empty
    def IsEmpty(self):
        return len(self.items) == 0

    # Returns True if the Stack is full by checking size of array to the max Stack size
    def IsFull(self):
        if len(self.items) == self.max_size:
            return True
        else:
            return False


    # Peek looks at the top item
    def Peek(self):
        if not self.IsEmpty():
            return self.items[-1]  # Using -1 removes the last element in a python list
        else:
            print("Can't Peek! ~ Stack is Empty")

    def size(self):
        return len(self.items)


# Testing Stack functions
array_stack = Stack(4)
array_stack.Push(1)
print("Top element:", array_stack.Peek())

array_stack.Push(2)

print("Take a PEEK at the top of the stack:", array_stack.Peek())
print("Popped item: ", array_stack.Pop())

print("Is the stack full?", array_stack.IsFull())

print("Stack size is: ", array_stack.size())
array_stack.Push(3)
array_stack.Push(4)
array_stack.Push(5)
print("Stack size:", array_stack.size())
print("Is the stack full?", array_stack.IsFull())


array_stack.Push(6)  # Can't Push 6 on to Stack because it's full
print("Take a PEEK at the top of the stack:", array_stack.Peek())
print("Popped item: ", array_stack.Pop())
print("Popped item: ", array_stack.Pop())
print("Popped item: ", array_stack.Pop())
print("Popped item: ", array_stack.Pop())

array_stack.Pop()  # Can't Pop because the stack is now empty


print("Stack size:", array_stack.size())
print("Is the stack full?", array_stack.IsFull())

array_stack2 = Stack()
array_stack2.Push(1)
array_stack2.Push(2)
array_stack2.Push(3)
array_stack2.Push(4)
print("Take a PEEK at the top of the stack:", array_stack2.Peek())
print("Popped item: ", array_stack2.Pop())
array_stack2.Push(4)

array_stack2.Push(4)
print("Is the stack full?", array_stack2.IsFull())

print("Stack size is: ", array_stack2.size())
