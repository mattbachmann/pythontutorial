from abc import ABC
from abc import abstractmethod

class Papa(ABC):
    cool = "Yea!"

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, input: str) -> str:
        pass

class Bobo(Papa):
     def apply(self, input):
        print(Bobo.cool)
        return self.name + " " + input
   
# test = Xformation()

nouns = ["Winnie", "Dumbo", "Igeli"]

xform = Bobo("super")

for x in nouns:
    print(x + " -> " + xform.apply(x))

result = list(map(xform.apply, nouns))
print(result)

result2 = list(map(Bobo("mega").apply, result))
print(result2)

