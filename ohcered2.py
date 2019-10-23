class Credit:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def info_of_item(self, iteam):
        print("индекс" + str(self.items.index(iteam)))

        if self.items == 0:
            print("wno")
        if self.items == 1:
            print("two")
        if self.items == 2:
            print("free")
        if self.items == 3:
            print("fore")
        if self.items == 4:
            print("fife")
        if self.items == 5:
            print("six")
        if self.items == 6:
            print("seven")
        if self.items == 7:
            print("eght")
        if self.items == 8:
            print("nite")
        if self.items == 9:
            


    def info_of_queue(self):
        print(self.items)

    def size(self):
        return len(self.items)


abc = Credit()

print(abc.is_empty())

print(abc.size())
print("===================")

# abc.enqueue("p02")
# abc.enqueue("p03")
# abc.enqueue("p04")
# abc.enqueue("p05")
# abc.enqueue("p06")
# abc.enqueue("p07")
# abc.enqueue("p08")

for i in range(1, 11):
    abc.enqueue("p-{}".format(i))

print(abc.info_of_queue())
print(abc.size())
print("===================")

#print(abc.info_of_item())

abc.info_of_item("p-6")