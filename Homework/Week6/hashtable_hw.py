"""
Troy Brunette
CS240
Hash Tables Assignment

This Hash Table uses Horner's method to calculate the hash value.
Horner's Method:
        * Evaluates a polynomial to calculate the hash value for an input string
        * The characters of the string are the coefficients of a polynomial

Handling Collisions:
- Instead of storing key/value pairs directly in an array, they are stored in a Linked List
- Each element of the array will have a pointer to its particular Linked List
- For any collisions, the Linked List at that particular index will contain those key/value pairs

"""
class Node:
    # For the "data" part of a node, key and value are used instead
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node to the front of list
    def add_to_front(self, key, value):
        node = Node(key, value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            self.head.next = node.next

    def search(self, key):
        """Traverses the Linked List and returns the value for a specified key
        returns None if the key is not in the Linked List."""
        current = self.head
        while current:
            if current.key == key and current.value is not None:
                return current.value
            current = current.next
        # return print(f"{key} not a valid key!")


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash_function(self, key):
        return self.horner_method(key)

    def horner_method(self, input_string):
        """Horner's Method:
            :: Uses a polynomial to calculate the hash value for an input string
            :: The characters of the string are the coefficients of a polynomial
        Arguments:
        - input_string: Input string
        - base: Base for the polynomial hash (a prime number)
        - mod: Modulus to avoid integer overflow
        - return: Hash value of the string
        """
        base = get_prime(20)
        mod = get_prime(self.size)
        hash_value = 0
        for char in input_string:  # Goes through each char of input string
            hash_value = (hash_value * base + ord(char))
        return hash_value % mod

    def insert(self, key, value):
        """Inserts a key/value pair into the table"""
        index = self.hash_function(key)
        self.table[index].add_to_front(key, value)

    def remove(self, key):
        """Using key and hash function to calculate index for removal"""
        index = self.hash_function(key)
        current = self.table[index].head

        # Check the first node for key
        if current and current.key == key:
            # Remove node by setting heads' pointer to current.next
            self.table[index].head = current.next
            return print(f"Key: {key} removed")

        # Traverse through linked list checking for the key
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return print(f"Key: {key} removed")
            current = current.next

        return print(f"{key} not a valid key!")

    def search(self, key):
        """Uses hash_function to get the index for a specified key
        and returns its value"""
        index = self.hash_function(key)
        if 0 <= index <= self.size and self.table[index].head is not None:

            return self.table[index].search(key)
        else:
            # print(f"{key} not a valid key!")
            return

    def get_keys(self):
        """Returns a list of all the keys in the table"""
        keys = []
        for llist in self.table:
            current = llist.head
            while current:
                keys.append(current.key)
                current = current.next
        return keys

    def get_values(self):
        """Returns a list of the values in the table"""
        values = []
        for llist in self.table:
            current = llist.head
            while current:
                values.append(current.value)
                current = current.next
        return values

    def get_pairs(self):
        """Returns a list of the key/value pairs in the table"""
        pairs = []
        for llist in self.table:
            current = llist.head
            while current:
                pairs.append((current.key, current.value))
                current = current.next
        return pairs


# Checks for and returns prime numbers to help with Horner's Method
def check_if_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Reminder-to-self: n ** 0.5 is the square root of n
        if n % i == 0:
            return False
    return True


# Find the smallest prime number greater than or equal to the minimum value
def get_prime(min_value):
    prime = min_value
    while True:
        if check_if_prime(prime):
            return prime
        prime += 1


# Testing Hash Table functions
hash_table = HashTable(size=100)

hash_table.insert("Juice", "3.00")
hash_table.insert("Banana", "0.89")
hash_table.insert("Avocado", "1.25")
hash_table.insert("Milk", "2.99")
hash_table.insert("Bread", "3.99")
hash_table.remove("Avocado")  # Testing remove
print(hash_table.search("Juice"))  # Search for "Juice" returns 3.00
print(hash_table.search("Pizza"))  # Search for "Pizza" returns 3.00
hash_table.search("Pizza")

print(hash_table.get_pairs())
print(hash_table.get_values())
print(hash_table.get_keys())
