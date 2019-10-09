class Meshnic():
    def __init__(self, mech, go, hp):
        self.__mech = mech
        self.__go = go
        self.__hp = hp

    def display(self):
        print("оружие" + self.__mech + "свойство" + str(self.__go) + "количество жизней" + str(self.__hp))


class Hardmob(Meshnic):
    def __init__(self, mech, go, hp, mana):
        Meshnic.__init__(self, mech, go, hp)
        self.__mana = mana
    #переопределение конструктара (верху)
    def display(self):
        print("оружие" + self.__mech + "свойство" + str(self.__go) +
              "количество жизней" + str(self.__hp) + "мана" + str(self.__mana))

meshnic1 = Meshnic("mech", 100, 100)
meshnic1.display()
hardmob1 = Hardmob("mech", 100, 100, 100)
hardmob1.display()
