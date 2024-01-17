"""
Singly Linked List
Troy Brunette
CS240
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Add a new node to the end of list
    def add(self, data):
        node = Node(data=data)
        self.size += 1
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    # Add a new node to the front of list
    def add_to_front(self, data):
        node = Node(data=data)
        self.size += 1
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            self.head.next = node.next

    # Insert a new node at the specified index
    def insert(self, data, index):
        if index < 0:
            print(f"{index} not a valid Index!")
            return
        node = Node(data)
        self.size += 1
        if index == 0:
            node.next = self.head
            self.head = node
            return
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                print(f"{index} not a valid Index!")
                return
            else:
                current = current.next
        node.next = current.next
        current.next = node

    # Prints list to console
    def display(self):
        current = self.head
        while current:
            print(f"[{current.data}]", end="-->")
            current = current.next
        print("None")

    # Returns the size of the list
    def get_size(self):
        return self.size

    # Counts each node in the list and returns the size
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

    # Deletes node at specified index
    def delete(self, index):
        if self.head is None or index < 0 or index >= self.size:
            print(f"{index} not a valid Index to delete!")
            return
        current = self.head
        position = 0
        if index == 0:
            self.remove_first_node()
        else:
            while current is not None and position < index - 1:
                position += 1
                current = current.next
            if current is not None:
                current.next = current.next.next
            # else:
            #     print("Index not present")
            self.size = self.size - 1

    # Removes the first node
    def remove_first_node(self):
        if self.head is None:
            return
        self.size = self.size - 1
        self.head = self.head.next

    # Returns the value from specified index
    def read(self, index):
        if index < 0 or index >= self.size:
            print(f"{index} not a valid Index!")
            return
        current = self.head
        for i in range(index):
            if current is None or index >= size:
                print(f"{index} not a valid Index!")
                return
            else:
                current = current.next
        return current.data

    # Performs a Linear Search for specified value
    def linear_search(self, value):
        current = self.head
        counter = 0
        while current:
            if current.data == value:
                print(f"{value} found at index {counter}")
                return
            else:
                counter += 1
                current = current.next
        print(f"{value} not found!")

    # Sorts the list using the Selection Sort Algorithm
    def selection_sort(self):
        current = self.head
        while current:
            min_num = current
            selection = current.next
            # Find the minimum value in the unsorted part
            while selection:
                if selection.data < min_num.data:
                    min_num = selection
                selection = selection.next
            # Swap the current node with the minimum value node
            temp = current.data
            current.data = min_num.data
            min_num.data = temp
            current = current.next


# Testing out the list and different functions
linked_list = LinkedList()
linked_list.add(4)
linked_list.add(6)
linked_list.add(2)
linked_list.add_to_front(11)
linked_list.add(3)

linked_list.insert(5, 4)
linked_list.display()
size = linked_list.count_nodes()
print(f"Linked List has {size} elements.")

linked_list.delete(1)


index = 3

print(f"[Index: {index}, Data: {linked_list.read(index)}]")
linked_list.linear_search(11)
linked_list.selection_sort()
linked_list.linear_search(11)
linked_list.display()
