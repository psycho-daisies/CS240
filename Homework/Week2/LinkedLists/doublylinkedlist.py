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

    # Add a new node to the end of list
    def add(self, data):
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

    # Insert a new node at the specified index
    def insert(self, data, index):
        if index < 0:
            print(f"{index} not a valid Index")
            return
        if index == 0:
            self.add_to_front(data=data)
            return
        node = Node(data=data)
        current = self.head
        counter = 0
        while current and counter < index:
            current = current.next
            counter += 1
        if current is None:
            self.add(data)
            return
        else:
            self.size += 1
            node.next = current
            node.prev = current.prev
            current.prev.next = node
            current.prev = node

    # Prints list to console by traversing each node
    def display(self):
        current = self.head
        while current:
            print(f"[{current.data}]", end="<-->")
            current = current.next
        print("None")  # End of list

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
                current = current.next
                counter += 1
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
            return
        else:
            while current is not None and position < index - 1:
                position += 1
                current = current.next
            if current is not None:
                self.size -= 1
                current.next = current.next.next
            # else:
            #     print("Index not present")

    # Removes the first node
    def remove_first_node(self):
        if self.head is None:
            return
        self.size -= 1
        self.head = self.head.next

    # Returns the value from specified index
    def read(self, index):
        if index < 0 or index >= self.size:
            print(f"{index} not a valid Index!")
            return
        current = self.head
        for i in range(index):
            if current is None or index >= self.size:
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
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.add_to_front(2)
doubly_linked_list.add(3)
doubly_linked_list.add(4)
doubly_linked_list.add(5)
doubly_linked_list.add(6)
doubly_linked_list.add_to_front(1)

doubly_linked_list.insert(8, 6)
doubly_linked_list.add_to_front(7)

print(doubly_linked_list.get_size())
print(doubly_linked_list.count_nodes())

doubly_linked_list.display()
doubly_linked_list.linear_search(4)

doubly_linked_list.selection_sort()

doubly_linked_list.display()
doubly_linked_list.linear_search(5)

doubly_linked_list.delete(6)
doubly_linked_list.display()
index = 3
print(f"[Index: {index}, Data: {doubly_linked_list.read(index)}]")
