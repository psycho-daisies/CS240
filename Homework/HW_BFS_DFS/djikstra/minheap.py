"""
Troy Brunette
CS240

Heap Structure:
- implemented with an array
- Allows efficient storage and retrieval of elements
- Great for accessing the minimum or maximum element
- can be used in a Priority Queue implementation

Heap Operations:
- maintain the heap property, keeping the tree structure balanced
- Push: add a new element to the heap
- Pop: removing and returning the min or max element
- Peek: retrieving the min or max element without removing it

Efficiency:
- useful for problems that require quickly finding and removing the minimum or maximum element.
- used in Dijkstra's algorithm for finding the shortest path in a graph and heap sort

Searching:
- Heaps are not designed for efficient searching like the binary search tree
- Uses a Linear search for finding a specific element
- Time Complexity: O(n), n is the size of the heap
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, data):
        """Add a new element to the heap"""
        self.heap.append(data)

        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the minimum element"""
        if self.heap is None:
            print("Can't pop from an empty Heap!")

        # swap the last element with the minimum element
        self.swap(0, len(self.heap) - 1)
        popped = self.heap.pop()

        # Restore the Heap by heapifying
        if self.heap:
            self._heapify_min(0)

        return popped

    def peek(self):
        """Retrieve the minimum element without removing it"""
        if self.heap:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

    def bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_min(self, i):
        """heapify_min maintains the min-heap property.
        Min-Heap Property: the value of each node is less than or equal to the values of its children
        ::Parameters::
            i: index of starting node"""
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # check if left child exists and is smaller than current smallest node
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left  # update smallest to the left child index
        # check if right child exists and is smaller than current smallest node
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right  # update smallest to the right child index
        # if current node value is not the smallest, swap the values at current node with the smallest node
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]  # swap
            self._heapify_min(smallest)  # Recursively call on the smallest child to ensure min-heap property

    def search(self, value):
        """Search Heap for a target value using a Linear Search"""
        for element in self.heap:
            if element == value:
                return True
            return False

    def __str__(self):
        return self.heap.__str__()


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, data):
        """Add a new element to the heap"""
        self.heap.append(data)
        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the minimum element"""
        if not self.heap:
            print("Can't pop from an empty Heap!")

        # Swap the last element with the root
        self.swap(0, len(self.heap) - 1)
        popped = self.heap.pop()

        # Restore max heap property by heapifying
        if self.heap:
            self._heapify_max(0)

        return popped

    def peek(self):
        """Retrieve the maximum element without removing it"""
        if self.heap:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_max(self, i):
        """heapify_max maintains the max-heap property.
        Max-Heap Property: the value of each node is greater than or equal to the values of its children
        ::Parameters::
            i: index of starting node"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # check if left child exists and is greater than current largest node
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left  # update smallest to the left child index
        # check if right child exists and is greater than current largest node
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right  # update smallest to the right child index
        # if current node value is not the largest, swap the values at current node with the largest node
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]  # swap
            self._heapify_max(largest)  # Recursively call on the largest child to ensure max-heap property

    def bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def search(self, value):
        """Search Heap for a target value using a Linear Search"""
        for element in self.heap:
            if element == value:
                return True
            return False

    def __str__(self):
        return self.heap.__str__()

"""
Troy Brunette
CS240

Heap Structure:
- implemented with an array
- Allows efficient storage and retrieval of elements
- Great for accessing the minimum or maximum element
- can be used in a Priority Queue implementation

Heap Operations:
- maintain the heap property, keeping the tree structure balanced
- Push: add a new element to the heap
- Pop: removing and returning the min or max element
- Peek: retrieving the min or max element without removing it

Efficiency:
- useful for problems that require quickly finding and removing the minimum or maximum element.
- used in Dijkstra's algorithm for finding the shortest path in a graph and heap sort

Searching:
- Heaps are not designed for efficient searching like the binary search tree
- Uses a Linear search for finding a specific element
- Time Complexity: O(n), n is the size of the heap
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, data):
        """Add a new element to the heap"""
        self.heap.append(data)

        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the minimum element"""
        if self.heap is None:
            print("Can't pop from an empty Heap!")

        # swap the last element with the minimum element
        self.swap(0, len(self.heap) - 1)
        popped = self.heap.pop()

        # Restore the Heap by heapifying
        if self.heap:
            self._heapify_min(0)

        return popped

    def peek(self):
        """Retrieve the minimum element without removing it"""
        if self.heap:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

    def bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_min(self, i):
        """heapify_min maintains the min-heap property.
        Min-Heap Property: the value of each node is less than or equal to the values of its children
        ::Parameters::
            i: index of starting node"""
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # check if left child exists and is smaller than current smallest node
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left  # update smallest to the left child index
        # check if right child exists and is smaller than current smallest node
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right  # update smallest to the right child index
        # if current node value is not the smallest, swap the values at current node with the smallest node
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]  # swap
            self._heapify_min(smallest)  # Recursively call on the smallest child to ensure min-heap property

    def search(self, value):
        """Search Heap for a target value using a Linear Search"""
        for element in self.heap:
            if element == value:
                return True
            return False

    def __str__(self):
        return self.heap.__str__()


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, data):
        """Add a new element to the heap"""
        self.heap.append(data)
        self.bubble_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return the minimum element"""
        if not self.heap:
            print("Can't pop from an empty Heap!")

        # Swap the last element with the root
        self.swap(0, len(self.heap) - 1)
        popped = self.heap.pop()

        # Restore max heap property by heapifying
        if self.heap:
            self._heapify_max(0)

        return popped

    def peek(self):
        """Retrieve the maximum element without removing it"""
        if self.heap:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_max(self, i):
        """heapify_max maintains the max-heap property.
        Max-Heap Property: the value of each node is greater than or equal to the values of its children
        ::Parameters::
            i: index of starting node"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # check if left child exists and is greater than current largest node
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left  # update smallest to the left child index
        # check if right child exists and is greater than current largest node
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right  # update smallest to the right child index
        # if current node value is not the largest, swap the values at current node with the largest node
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]  # swap
            self._heapify_max(largest)  # Recursively call on the largest child to ensure max-heap property

    def bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] > self.heap[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def search(self, value):
        """Search Heap for a target value using a Linear Search"""
        for element in self.heap:
            if element == value:
                return True
            return False

    def __str__(self):
        return self.heap.__str__()

