from typing import Protocol

class contract(Protocol):
    def voice(self):
        pass


class animal:
    def voice(self):
        print("how how...")


class car:
    def voice(self):
        print("vrom vrom...")


dacia = car()
dog = animal()
classes = [dacia, dog]

for func in classes:
    func.voice()

# Duck typing
