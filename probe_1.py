class House:

    houses_history = []


    def __new__(cls, *args, **kwargs):

        return object.__new__(cls)

        cls.houses_history.append(cls.args)


    print(houses_history)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # self.same_metod()





    def go_to(self, new_floor):

        if new_floor < 1 or new_floor > self.number_of_floors:

            print("Такого этажа не существует")
        else:
            print(new_floor)

    # def same_metod(self):
    #     historu = []
    #     historu. append(self)
    #     print(historu, 'теперь в истории')

    # def __add__(self, value):
    #     return self.number_of_floors + value


    def __len__(self):
        return self.number_of_floors


    def __str__(self):
        return f'Название: {self.name}, кол-во этажей {self.number_of_floors}.'


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors


    def __eq__(self, other):
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False


    def __lt__(self, other):
        if self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False



    def __le__(self, other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False


    def __gt__(self, other):
        if self.number_of_floors > other.number_of_floors:
            return True
        else:
            return False


    def __ge__(self, other):
        if self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False


    def __ne__(self, other):
        if self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False


    def __add__(self, other):
        if isinstance(self.number_of_floors, int):
            self.number_of_floors += int(other)
            return self



    def __radd__(self, other):
        self.number_of_floors += int(other)
        return self


    def __iadd__(self, other):
        self.number_of_floors += int(other)
        return self


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)




















# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)

# print(h1)
# print(id(h1))
# print(h2)
# print(id(h2))
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__



