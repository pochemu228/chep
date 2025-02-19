class Item:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def craft(self, other_item):
        pass  # реализуется в подклассах

class Tool(Item):
    def __init__(self, name, damage=0):
        super().__init__(name)
        self.damage = damage

    def craft(self, material1, material2=None):
        if isinstance(material1, Material) and isinstance(material2, Material):
            if material1.get_name() == 'Stick' and material2.get_name() == 'Stone':
                return StoneSword()
            return None

class StoneSword(Tool):
    def __init__(self):
        super().__init__('Stone Sword', 5)

class Material(Item):
    def __init__(self, name, quantity=1):
        super().__init__(name)
        self.quantity = quantity  # Corrected: Assign value to self.quantity

    def use_material(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        else:
            print(f"Not enough {self.get_name()}!")
            return False

class Stick(Material):
    def __init__(self):
        super().__init__('Stick')

class Stone(Material):
    def __init__(self):
        super().__init__('Stone')



stick = Stick()
stone = Stone()
tool = Tool('Basic Tool')

sword = tool.craft(stick, stone)
if sword is not None:
    print(sword.get_name())
else:
    print("Craft failed")
