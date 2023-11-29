class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        """Add a node with the given data to the binary tree."""
        self.root = self._add(self.root, data)

    def _add(self, current_node, data):
        """Helper function for adding a node recursively."""
        if current_node is None:
            return Node(data)
        if data < current_node.data:
            current_node.left_child = self._add(current_node.left_child, data)
        elif data > current_node.data:
            current_node.right_child = self._add(current_node.right_child, data)
        return current_node

    def remove(self, data):
        """Remove a node with the given data from the binary tree."""
        self.root = self._remove(self.root, data)

    def _remove(self, current_node, data):
        """Helper function for removing a node recursively."""
        if current_node is None:
            return None
        if data < current_node.data:
            current_node.left_child = self._remove(current_node.left_child, data)
        elif data > current_node.data:
            current_node.right_child = self._remove(current_node.right_child, data)
        else:
            if current_node.left_child is None:
                return current_node.right_child
            elif current_node.right_child is None:
                return current_node.left_child
            current_node.data = self._get_min_value(current_node.right_child)
            current_node.right_child = self._remove(current_node.right_child, current_node.data)
        return current_node

    def _get_min_value(self, node):
        """Helper function to get the minimum value in a subtree."""
        while node.left_child is not None:
            node = node.left_child
        return node.data

    def travel_inorder(self):
        """Traverse the binary tree in inorder (left, root, right) and print the data."""
        self._travel_inorder(self.root)

    def _travel_inorder(self, current_node):
        """Helper function for inorder traversal."""
        if current_node:
            self._travel_inorder(current_node.left_child)
            print(current_node.data, end=" ")
            self._travel_inorder(current_node.right_child)

    def size(self):
        """Return the size (number of nodes) of the binary tree."""
        return self._size(self.root)

    def _size(self, current_node):
        """Helper function to calculate the size recursively."""
        if current_node is None:
            return 0
        return 1 + self._size(current_node.left_child) + self._size(current_node.right_child)


# Example usage:
binary_tree = BinaryTree()
binary_tree.add(10)
binary_tree.add(5)
binary_tree.add(15)
binary_tree.add(3)
binary_tree.add(7)

print("Inorder Traversal:")
binary_tree.travel_inorder()

print("\nSize of the Binary Tree:", binary_tree.size())

binary_tree.remove(5)

print("Inorder Traversal after removing 5:")
binary_tree.travel_inorder()

print("\nSize of the Binary Tree after removal:", binary_tree.size())
