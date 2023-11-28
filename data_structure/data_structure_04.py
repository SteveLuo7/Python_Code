class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def insert(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Invalid position")
                return
            current_node = current_node.next
        new_node.next = current_node.next
        new_node.prev = current_node
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def is_empty(self):
        return self.head is None

    def travel(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def remove(self, data):
        current_node = self.head
        while current_node and current_node.data != data:
            current_node = current_node.next
        if current_node is None:
            print(f"{data} not found in the list.")
            return
        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next
        if current_node.next:
            current_node.next.prev = current_node.prev

if __name__ == "__main__":
    # Create a doubly linked list and perform operations
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.add(0)
    doubly_linked_list.insert(2, 1.5)
    doubly_linked_list.travel()

    print("Is the list empty?", doubly_linked_list.is_empty())

    doubly_linked_list.remove(1)
    doubly_linked_list.travel()

    print("Is 1.5 in the list?", doubly_linked_list.search(1.5))
