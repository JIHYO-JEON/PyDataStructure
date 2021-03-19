class Node:
    """node class for linked list"""
    def __init__(self, data):
        self.data = data  # Node data
        self.next = None  # Reference for next node


class LinkedList:
    """Linked List Class"""

    def __init__(self):
        self.head = None  # the first node(head node)
        self.tail = None  # the last node(tail node)

    def append(self, data):
        """Append new node to linked list"""
        new_node = Node(data)

        # when linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # when linked list is not empty
        else:
            self.tail.next = new_node  # add new node after the last node
            self.tail = new_node  # let new node as tail node

    def prepend(self, data):
        """Append new node before head"""
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def pop_left(self):
        """Delete head node"""
        data = self.head.data
        self.head = self.head.next
        if self.head == self.tail:
            self.tail = None
        return data

    def __str__(self):
        """print linked list"""
        res_str = "|"

        iterator = self.head

        # for all node
        while iterator is not None:
            # str +
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # next node

        return res_str

    def find_node_with_data(self, data):
        """Find node with data(input), if there is no"""
        iterator = self.head
        while True:
            if iterator.data == data:
                return iterator
            elif iterator.next is None:
                return None
            else:
                iterator = iterator.next

    def find_node_at(self, index):
        """fidn node with index"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator


class DoublyLinkedList:
    """ Linked List with data, prev, next"""

    def __init__(self):
        self.head = None  # the first node(head node)
        self.tail = None  # the last node(tail node)

    def insert_after(self, previous_node, data):
        """Append new node to linked list"""
        new_node = Node(data)
        if previous_node != self.tail:
            previous_node.next.prev = new_node
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next = new_node
        else:
            new_node.prev = previous_node
            previous_node.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Append new node before head"""
        new_node = Node(data)
        if self.tail == None and self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, node_to_delete):
        if node_to_delete == self.head and node_to_delete == self.tail:
            self.head = None
            self.tail = None
        elif node_to_delete == self.head:
            self.head = node_to_delete.next
            self.head.prev = None
        elif node_to_delete == self.tail:
            self.tail = node_to_delete.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        return node_to_delete.data

    def __str__(self):
        """print linked list"""
        res_str = "|"

        iterator = self.head

        # for all node
        while iterator is not None:
            # str +
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # next node

    def find_node_with_data(self, data):
        """Find node with data(input), if there is no"""
        iterator = self.head
        while True:
            if iterator.data == data:
                return iterator
            elif iterator.next is None:
                return None
            else:
                iterator = iterator.next

    def find_node_at(self, index):
        """fidn node with index"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator
