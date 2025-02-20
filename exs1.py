class Resource:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name()})"


class Stick(Resource):
    pass


class Stone(Resource):
    pass


class Sword:
    def __init__(self, durability=100):
        self._durability = durability

    def durability(self):
        return self._durability

    def craft(self, stick, stones):
        if isinstance(stick, Stick) and all(isinstance(s, Stone) for s in stones):
            if len(stones) >= 2:
                print(f"Crafted a {self.__class__.__name__}")
                return self
        else:
            raise ValueError("Invalid ingredients")

    def info(self):
        return f"Sword with durability: {self.durability()}"

    def __repr__(self):
        return f"{self.__class__.__name__}(durability={self.durability()})"


stick = Stick('Stick')
stone1 = Stone('Stone')
stone2 = Stone('Stone')
sword = Sword()
crafted_sword = sword.craft(stick, [stone1, stone2])
print(crafted_sword.info())
