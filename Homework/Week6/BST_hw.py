"""
# Assignment: Binary Search Tree
# Authors: Troy Brunette

# This program constructs a data structure called Binary Search Tree
# A Binary Search tree organizes elements in a tree-like structure.
# Each node can have a left and right child node
# The left child node must be less than its root node
# and the nodes in the right subtree are greater than its root node.
# A BST is efficient at searching, insertion, and deletion operations.


- Pre-Order Traversal: root -> left subtree -> right subtree
    - visit root node first
    - then recursively traverse the left subtree
    - finally recursively traverse the right subtree

- In-Order Traversal: left subtree -> root -> right subtree
    - first recursively traverse the left subtree
    - then visit the root
    - and then finally traverse the right subtree


- Post-Order Traversal: left subtree -> right subtree -> root
    - first recursively traverse left subtree
    - then recursively traverse right subtree
    - finally visit the root node
"""


class TreeNode:
    """CONSTRUCTS TreeNode objects for a Binary Search Tree"""
    # Each TreeNode has these properties:
    # Can have a maximum of two children nodes
    # TreeNodes on the left subtree are less than the root node
    # TreeNodes on the right subtree are greater than the root node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """CONSTRUCTS AN EMPTY TREE"""
    def __init__(self):
        self.size = 0
        self.root = None

    # Add a new node to the Binary Search Tree
    def add(self, data):
        if data is None:
            return print("Error! Check for Null")
        self.size += 1
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None:
            return TreeNode(data)
        # Add to the LEFT side if data is less than the root node
        if data < root.data:
            root.left = self._add(root.left, data)
        # Add to the RIGHT side if data is greater than the root node
        elif data > root.data:
            root.right = self._add(root.right, data)
        elif data == root.data:  # DUPLICATES NOT ALLOWED
            self.size -= 1
            return root
        return root

    # Search using a binary search algorithm of comparisons
    def search(self, target):
        """Searches for a target value by searching certain side of tree depending on comparisons"""
        return self._search(self.root, target)

    def _search(self, root, target):
        if root is not None:
            # Check if target is found
            if target == root.data:
                return root
            # if target less than the current node, check the left side
            if target < root.data:
                return self._search(root.left, target)
            # if target greater than the current node, check the right side
            else:
                return self._search(root.right, target)
        # Target not found
        return None

    # Pre-Order Traversal: goes from root -> left subtree -> right subtree
    # Uses a stack to help with the ordering
    def preorder_traversal(self):
        result = []
        stack = [self.root]

        while len(stack) > 0:
            current = stack.pop()
            if current:
                result.append(current.data)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)

        return result

    # Post-Order Traversal: goes from left subtree -> right subtree -> root
    # Uses Recursion
    def postorder_traversal(self):
        post_order_list = []
        self._postorder(self.root, post_order_list)
        return post_order_list

    def _postorder(self, root, post_order_list):
        if root is not None:
            self._postorder(root.left, post_order_list)
            self._postorder(root.right, post_order_list)
            post_order_list.append(root.data)

    # In Order Traversal: goes from left subtree -> root -> right subtree
    def inorder_traversal(self):
        if self.root is None:
            return []
        result = []
        stack = []
        current = self.root  # The root node we are looking at
        while current or stack:
            # Check the left side first
            if current:
                stack.append(current)
                current = current.left
            else:  # If current is None, pop from the stack, visit it, and move to its right child
                current = stack.pop()
                result.append(current.data)
                current = current.right

        return result


# Constructing and adding to a Binary Search Tree
binarySearchTree = BinarySearchTree()
nums = [7, 3, 1, 6, 5, 4, 6, 2, 8]

for num in nums:
    binarySearchTree.add(num)


# Traversals
print("IN ORDER traversal:", binarySearchTree.inorder_traversal())
print("PRE-ORDER traversal:", binarySearchTree.postorder_traversal())
print("POST-ORDER traversal:", binarySearchTree.preorder_traversal())

# Searching
target = 22
result = binarySearchTree.search(target)
if result is not None:
    print(f"{target} found in the tree.")
else:
    print(f"{target} NOT found.")



