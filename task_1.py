class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def tolist(self) -> list:
        return [i for i in self.table]

    def hash_function(self, key):
        hash_key = hash(key) % self.size
        return hash_key

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        deleted = False
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for entry in self.table[key_hash]:
                if entry[0] == key:
                    sub_item_index = self.table[key_hash].index(entry)
                    self.table[key_hash].pop(sub_item_index)
                    deleted = True
                    break
            if not deleted:
                print("No corresponding item found.")
        else:
            print("No corresponding item found.")


H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.tolist())

H.delete("apple")  # deletion happens
print(H.tolist())  # check the above
H.delete("bananas")  # no deletion happens
print(H.tolist())  # the hash table stays the same
