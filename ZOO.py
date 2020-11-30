class Milk:
    def __init__(self, name, voice, weight=0, quantity=0):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.quantity = quantity

    def eat(self, grass):
        self.weight += grass

    def milking(self, milk):
        self.quantity += milk


cow = Milk('Манька', 'Му-Му', 350)
goat1 = Milk('Рога', 'Ме-Ме', 20)
goat2 = Milk('Копыта', 'Ме-Ме', 22)

# cow.eat(1)
cow.milking(2)
print(cow.quantity)
# print(goat1.voice)
# print(cow.weight)
# print(cow.quantity)


class Eggs:
    def __init__(self, name, voice, weight=0, quantity=0):
        self.name = name
        self.voice = voice
        self.weight = weight
        self.quantity = quantity

    def eat(self, grass):
        self.weight += grass * 0.2

    def collect(self, eggs):
        self.quantity += eggs


geese1 = Eggs('Grey', 'Шшшш', 13)
geese2 = Eggs('White', 'Шшшш', 15)
chicken1 = Eggs('Ко-Ко', 'Ку-ка-ре-ку', 5)
chicken2 = Eggs('Кукареку', 'Ку-ка-ре-ку', 6)
duck = Eggs('Кряква', 'Кря', 7)

# chicken2.collect(3)
# print(chicken2.quantity)
# print(geese1.weight)


class Cut:
    def __init__(self, name, voice, weight=0, quantity=0):
        self.name = name
        self.voice = voice
        self.weight = weight
        self.quantity = quantity

    def eat(self, grass):
        self.weight += grass

    def cutting(self, wool):
        self.quantity += wool


sheep1 = Cut('Барашек', 'Бее', 20)
sheep2 = Cut('Кудрявый', 'Бее', 22)

# print(sheep2.name)
# sheep2.cutting(2)
# print(sheep2.quantity)
# print(sheep2.weight)

animals = [cow, goat1, goat2, geese1, geese2, chicken2, chicken1, duck, sheep2, sheep1]


sum = 0
for animal in animals:
    sum += animal.weight
print(f'Общий вес животных {sum} кг')

max_weight = 0
for animal in animals:
    if animal.weight > max_weight:
        max_weight = animal.weight
        max_name = animal.name
print(f'Имя животного {max_name} с максимальным весом {max_weight} кг')






    # print(f'Имя животного с максимальным весом {animal.weight}, {animal.name}')



























# гусей "Серый" и
# "Белый"

# корову "Маньку"

# овец "Барашек" и
# "Кудрявый"

# кур "Ко-Ко" и "Кукареку"

# коз "Рога" и "Копыта"

# и утку "Кряква"​Со всеми животными вам необходимо как-то взаимодействовать:

# кормить
# корову и коз доить

# овец стричь

# собирать яйца у кур, утки и гусей

# различать по голосам(коровы мычат, утки крякают и т.д.)​