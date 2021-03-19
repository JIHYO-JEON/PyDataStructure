class Node:
    """Node class for Linked List"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # reference for next node
        self.prev = None  # reference for previous node


class LinkedList:
    """Linked list class"""

    def __init__(self):
        self.head = None  # the first node, head
        self.tail = None  # the last node, tail

    def find_node_with_key(self, key):
        """Find node with data(input), if there is no node, return None"""
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

    def append(self, key, value):
        """Append new node to linked list"""
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, node_to_delete):
        """Delete of Doubly Linked List"""
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.value

    def __str__(self):
        res_str = ""

        iterator = self.head

        while iterator is not None:
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next

        return res_str

