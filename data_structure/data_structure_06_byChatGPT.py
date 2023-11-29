class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack."""
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0


# Example usage:
my_stack = Stack()

# Pushing elements onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Checking the size of the stack
print("Size of the stack:", my_stack.size())

# Peeking at the top element
print("Top element:", my_stack.peek())

# Popping elements from the stack
popped_item = my_stack.pop()
print("Popped element:", popped_item)

# Checking if the stack is empty
print("Is the stack empty?", my_stack.is_empty())
