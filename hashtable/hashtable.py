class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"({self.key}, {self.value}, {self.next})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def contains(self, key): 
        current = self.head
        while current is not None: 
            if current.key == key:
                return current
            current = current.next
        return current

    def upsert(self, key, value):
        new_node = HashTableEntry(key,value)
        if self.contains(key) is not None:
            self.contains(key).value = value
        elif self.head: 
            new_node.next = self.head
            self.head = new_node
        elif self.head is self.tail and self.head is None:
            self.tail = new_node
            self.head = new_node

    def __repr__(self):
        return f"{self.head}"

    def delete(self, key):
        if self.contains(key) is not None: 
            if self.head is self.tail:
                self.head = None
                self.tail = None
            elif self.head.key == self.contains(key).key:
                self.head = self.head.next
            elif self.tail is self.contains(key):
                self.tail = self.get_prev_node(self.contains(key))
                self.tail.next = None
            else:
                self.get_prev_node(self.contains(key)).next = self.contains(key).next

    def get_prev_node(self, node):
        current = self.head
        prev_node = None
        while current is not node:
            prev_node = current
            current = self.head.next
        return prev_node  


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
class HashTable:

    def __init__(self, capacity):
        self.capacity = [None] * capacity
        self.filled_slots = 0
        self.new_capacity_length = len(self.capacity) * 2

    def get_num_slots(self):
        return len(self.capacity)

    def get_load_factor(self):
        return self.filled_slots / self.get_num_slots()

    def fnv1(self, key):
        prime_number = 1099511628211
        offset_number = 14695981039346656037
        my_hash = offset_number
        for char in key:
            my_hash = my_hash * prime_number
            my_hash = my_hash ^ ord(char)
        return my_hash

    def djb2(self, key):
        hash_var = 5381
        string_bytes = key.encode()
        for b in string_bytes:
            hash_var = ((hash_var << 5) + hash_var) + b 
        return hash_var

    def hash_index(self, key):
        # return self.fnv1(key) % len(self.capacity)
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        if self.capacity[self.hash_index(key)] is None:
            self.capacity[self.hash_index(key)] = LinkedList()
        self.capacity[self.hash_index(key)].upsert(key,value)
        self.filled_slots += 1
        if self.get_load_factor() >= .70: 
            self.resize(len(self.capacity) * 2)
   
    def delete(self, key):
        self.capacity[self.hash_index(key)].delete(key)
        self.filled_slots -= 1

    def get(self, key):
        node_sent_back = self.capacity[self.hash_index(key)].contains(key)
        if node_sent_back is None:
            return None 
        return node_sent_back.value

    def resize(self, new_capacity):
        temp_capacity = self.capacity
        self.capacity = [None] * new_capacity
        for element in temp_capacity:
            if element is not None:
                self.put(element.head.key, element.head.value)
                current = element.head
                while current.next is not None:
                    self.put(element.head.next.key,element.head.next.value)
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(print(ht.get(f"line_{)i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")