class Voiture:
    local = 0
    def __init__(self, name, color , price,model):
        self.name = name
        self.color = color
        self.price = price
        self.model = model
        Voiture.local += 10
    def desplay(self):
        print(f"the name is {self.name}, the c`olor is {self.color} the price is {self.price} model {self.model}, local {Voiture.local+1}")


def increment(i):
    return i + 1


dacia = Voiture("dacia","black",545,2012)
ferrari = Voiture("ferrari","red",55,2012)
renau = Voiture("decewc","red",55,2012)
print(dacia.desplay())
print(ferrari.desplay())
print(renau.desplay())
print(Voiture.local)
Voiture.local += 10
print(Voiture.local)
nb = increment(10)
print(nb)
