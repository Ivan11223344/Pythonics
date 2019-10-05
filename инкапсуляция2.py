class Person:
    def __init__(self, code, prise, name):
        self.__code = code
        self.__pryse = prise
        self.__name = name

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(safe, code):
        if code in range(11111111, 99999999):
            self.__code
        else:
            print("неверный коде")

    @property
    def prise(self):
        return self.__prise

    @code.setter
    def code(safe, prise):
        if code in range(1, 10000):
            self.__code
        else:
            print("неверная цена")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("code" + str(self.__code) + "prise" + str(self.__pryse) + "name" + self.__name)

person1 = Person(12345678, 213, "cola")
person1.display_info()

person2 = Person(123, 111, "pepsi")
person2.display_info()

#price