class Model():
    
    def __init__(self, shk, price, valut, tetle, partiya):
        self.shk = shk      #публичный, общественный атрибут
        self.price = price
        self.valut = valut
        self.tetle = tetle
        self.partiya = partiya

    def info (self):
        if self.valut is True:
            self.valut = "$"
        else:
            self.valute = "RUB"

        if self.partiya is True:
            self.partiya = "GOOD!"
        else:
            self.partiya = "Big downe!"
        print("Напиток " + self.shk + str(self.price) + self.valut + self.tetle + self.partiya)

model1 = Model("не известен ", 150, True, "Cola ", False)
model1.info()