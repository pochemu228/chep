class Character:
    def __init__(self, attack_damage, attack_speed, name):
        self._attack_damage = attack_damage
        self._attack_speed = attack_speed
        self._name = name

    def get_name(self):
        return self._name

    def get_attack_damage(self):
        return self._attack_damage

    def get_attack_speed(self):
        return self._attack_speed


class StoneSword:
    def __init__(self, attack_damage, attack_speed, name):
        self._attack_damage = attack_damage
        self._attack_speed = attack_speed
        self._name = name

    def info(self):
        print(f"{self._name}, "
              f"Класс оружия: Каменный меч, "
              f"Физический урон: {self._attack_damage}, "
              f"Быстрая атака: {self._attack_speed}")

    def upgrade(self, new_attack_damage, new_attack_speed):
        old_damage = self._attack_damage
        old_speed = self._attack_speed

        self._attack_damage = new_attack_damage
        self._attack_speed = new_attack_speed

        print(f"Меч был усовершенствован. "
              f"Физический урон увеличился с {old_damage} до {new_attack_damage}, "
              f"Быстрая атака увеличилась с {old_speed} до {new_attack_speed}")


class Axe:
    def __init__(self, damage, cutting_down_trees, name):
        self._damage = damage
        self._cutting_down_trees = cutting_down_trees
        self._name = name

    def get_damage(self):
        return self._damage

    def get_cutting_down_trees(self):
        return self._cutting_down_trees

    def info(self):
        print(f"{self._name}, "
              f"Класс оружия: Топор, "
              f"Физический урон: {self._damage}, "
              f"Вырубка деревьев: {self._cutting_down_trees}")

    def upgrade(self, new_damage, new_cutting_down_trees):
        old_damage = self._damage
        old_cutting = self._cutting_down_trees

        self._damage = new_damage
        self._cutting_down_trees = new_cutting_down_trees

        print(f"Топор был усовершенствован. "
              f"Физический урон увеличился с {old_damage} до {new_damage}, "
              f"Вырубка деревьев увеличилась с {old_cutting} до {new_cutting_down_trees}")


sword = StoneSword(12, 1.2, "Клинок")
sword.info()
sword.upgrade(15, 1.5)
axe = Axe(14, 7, "Лесоруб")
axe.info()
axe.upgrade(21, 9)


