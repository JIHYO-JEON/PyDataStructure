from Basic.LLforHT import LinkedList

class HashTable:
    """Hash Table class with Chaining"""

    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [LinkedList() for _ in range(self._capacity)]

    def _hash_function(self, key):
        """
        Return hash value of key
        :param key: invariant value
        :return: hash vaule
        """
        return hash(key) % self._capacity

    def look_up_value(self, key):
        """
        Return data with key
        :param key: key
        """
        hash_value = self._hash_function(key)
        node = self._table[hash_value].find_node_with_key(key)
        return node.value

    def _look_up_node(self, key):
        """Return node with key"""
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)

    def insert(self, key, value):
        """
        Insert new key-value set
        """
        hash_value = self._hash_function(key)
        ll = self._table[hash_value]
        node = ll.find_node_with_key(key)
        if node is None:
            ll.append(key, value)
        else:
            node.value = value

    def _get_linked_list_for_key(self, key):
        """Return linked list of input key"""
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]

    def delete_by_key(self, key):
        """Delete key-value set of input key"""
        ll = self._get_linked_list_for_key(key)
        node = ll.find_node_with_key(key)
        ll.delete(node)

    def __str__(self):
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

