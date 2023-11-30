class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node

    def get_by_index(self, index):
        if index >= 0:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data
        else:
            return None

    def delete_by_index(self, index):
        if index >= 0:
            current = self.head
            for _ in range(index):
                current = current.next
            if current.next is not None:
                current.next = current.next.next
            else:
                self.tail = current
        else:
            return None

    def len(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
