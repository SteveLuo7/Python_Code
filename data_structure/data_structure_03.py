class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def insert(self, position, data):
        if position < 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        for _ in range(position - 1):
            if current_node is None:
                print("Invalid position")
                return
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def travel(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def is_empty(self):
        return self.head is None

    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"{data} not found in the list.")
            return
        prev_node.next = current_node.next

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

if __name__ == "__main__":
    # Create a singly linked list and perform operations
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.add(0)
    singly_linked_list.insert(2, 1.5)
    singly_linked_list.travel()

    print("Is the list empty?", singly_linked_list.is_empty())

    singly_linked_list.remove(1)
    singly_linked_list.travel()

    print("Is 1.5 in the list?", singly_linked_list.search(1.5))

    print("Length of the list:", singly_linked_list.length())

    print('==============ADD=================')
    singly_linked_list.add(618)
    print(singly_linked_list.is_empty())
    singly_linked_list.travel()

