class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.insert(0, item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)


# Example usage:
my_queue = Queue()

# Enqueueing elements
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Checking the size of the queue
print("Size of the queue:", my_queue.size())

# Dequeueing elements
dequeued_item = my_queue.dequeue()
print("Dequeued element:", dequeued_item)

# Checking if the queue is empty
print("Is the queue empty?", my_queue.is_empty())
