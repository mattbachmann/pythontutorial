from abc import ABCMeta
from abc import abstractmethod

class Xformation(metaclass=ABCMeta):
    @abstractmethod
    def apply(self, input: str) -> str:
        pass

class AdjectiveX(Xformation):
    def __init__(self, adjective: str):
        self.adjective = adjective

    def apply(self, input: str) -> str:
        return f"{self.adjective} {input}"

nouns = ["Winnie", "Dumbo", "Igeli"]
xform = AdjectiveX("super");
result = list(map(xform.apply, nouns))
print(result)

result2 = list(map(AdjectiveX("mega").apply, result))
print(result2)

