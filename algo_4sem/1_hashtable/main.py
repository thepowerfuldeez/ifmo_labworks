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
        self.n_collisions = 0
        self.n_comparisons = 0

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

        hashvalue = self.hashfunction(key)
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = value
            self.capacity -= 1
        else:
        	# проверяем, нет ли коллизии по ключу
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = value
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
        startslot = self.hashfunction(key)
        data = None
        found = False
        stop = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            self.n_comparisons += 1
            if self.slots[position] == key:
                data = self.data[position]
                found = True
            else:
            	# случилась коллизия
                self.n_collisions += 1
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __contains__(self, key):
        return key in self.slots

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == '__main__':
    table = HashTable(3500)
    with open("sample_text.txt", encoding="windows-1251") as f:
        for line in f:
            if line.strip():
                key, *value = line.split()
                if len(key) >= 3:
                    table[key] = " ".join(value)

    with open("sample_text.txt", encoding="windows-1251") as g:
        i = 1
        j = 1
        for line in g:
            if line.strip():
                key, *value = line.split()
                if len(key) >= 3:
                    v = table[key]
                    if v == " ".join(value):
                        i += 1
                        # print(key, v)
                    if j % 100 == 0:
                        print(j, table.n_comparisons, table.n_collisions)
                    j += 1
    print(i / j)



