class Person():
    def __init__(self, name, sername, money, hp, skorost):
        self.name = name
        self.sername = sername
        self.money = money
        self.hp = hp
        self.skorost = skorost
        self.atack = atack
        self.proviziya = proviziya

    def wazzep(self):
        print("Меня зовут " + self.name + self.sername + "имею" + self.money + self.hp + self.skorost + self.atack + self.provizia)

    if self.money == 1000:
        print(Вы очень богаты!)

    if self.hp == 1000:
        print(Вы почти безсмертны)

    if self.skorost == 1000:
        print(Вы очень бысры)

person1 = Person("Tom", "Redle", "1000", "1000", "1000")
person1.wazzep()

