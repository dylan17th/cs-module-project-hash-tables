class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:

    def __init__(self, capacity):
        self.capacity = [None] * capacity
        self.filled_slots = 0

    def get_num_slots(self):
        return len(self.capacity)


    def get_load_factor(self):
        return self.filled_slots / self.get_num_slots()


    def fnv1(self, key):
        prime_number = 1099511628211
        offset_number = 14695981039346656037
        my_hash = offset_number + 2
        for char in key:
            my_hash = my_hash * prime_number
            my_hash = my_hash ^ ord(char)
        return my_hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        pass


    def hash_index(self, key):
        return self.fnv1(key) % len(self.capacity)
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        key = self.hash_index(key)
        self.capacity[key] = value
        self.filled_slots += 1



    def delete(self, key):
        key = self.hash_index(key)
        self.capacity[key] = None

    def get(self, key):
        key = self.hash_index(key)
        return self.capacity[key]


    def resize(self, new_capacity):
        self.capacity = new_capacity
        return self.capacity


if __name__ == "__main__":
    ht = HashTable(8)
    my_item = HashTableEntry("dyl", "dylan collins")
    my_item2 = HashTableEntry("dustyn", "dustyn collins")
    ht.put(my_item.key, my_item.value)
    ht.put(my_item2.key, my_item2.value)
    # print(ht.resize(16))
    print(ht.capacity)

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
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
