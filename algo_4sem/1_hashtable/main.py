import random
# для воспроизводимости результатов
random.seed(17)

class HashTable:
    def __init__(self, size):
        self.size = size
        # количество свободных мест
        self.capacity = self.size
        self.slots = [None] * self.size
        # key, value пары
        self.data =  [None] * self.size

    def hashfunction(self, key):
        return ord(key[0]) + ord(key[1]) + ord(key[2])

    def rehash(self, oldhash, size):
        return (oldhash + random.randint(1, size)) % size

    def put(self, key, value):
        # если так получилось, что не осталось свободных мест
        if self.capacity < 1:
            self.slots += [None]
            self.data += [None]
            self.capacity += 1

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
            self.capacity -= 1
        else:
        	# проверяем, нет ли коллизии по ключу
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                rehashed = self.rehash(hashvalue, len(self.slots))
                while self.slots[rehashed] != None and self.slots[rehashed] != key:
                    rehashed = self.rehash(rehashed, len(self.slots))
                if self.slots[rehashed] == None:
                    self.slots[rehashed] = key
                    self.data[rehashed] = value
                    self.capacity -= 1
                else:
                    self.data[rehashed] = value

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        found = False
        stop = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                data = self.data[key]
                found = True
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __delitem__(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == key:
            self.slots[hashvalue] = None
            self.data[hashvalue] = None
        else:
            rehashed = self.hashfunction(hashvalue, len(self.slots))
            while self.slots[rehashed] != key:
                rehashed = self.hashfunction(rehashed, len(self.slots))
            if self.slots[rehashed] == key:
                self.slots[rehashed] == None
                self.data[rehashed] == None

    def __contains__(self, key):
        return key in self.slots

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)