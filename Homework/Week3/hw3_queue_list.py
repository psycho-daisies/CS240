"""
Doubly Linked List
Troy Brunette
CS240
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Add a new node to the end
    def append(self, data):
        node = Node(data=data)
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

    # Add a new node to the front of list
    def add_to_front(self, data):
        node = Node(data=data)
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.next = node.next

    # Returns the size of the list
    def get_size(self):
        return self.size

# Still a WIP 
class DoublyLinkedListQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def is_empty(self):
        return self.queue.head is None

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue.head is None:
            return "Queue is empty"

        dequeued_data = self.queue.head.data

        self.queue.head = self.queue.head.next

        # Update previous pointer of the new front node to null
        if self.queue.head is not None:
            self.queue.head.prev = None

        return dequeued_data


# Testing out the list and different functions
test_list = DoublyLinkedListQueue()
test_list.enqueue(5)
test_list.enqueue(6)
test_list.enqueue(7)
num = test_list.dequeue()

print(num)
num = test_list.dequeue()


