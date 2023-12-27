from animal import Animal


class AnimalList:
    def __init__(self):
        self.animal_list = []

    def add_animal(self, name, type_animal, birthday, command):
        animal = Animal(name, type_animal, birthday, command)
        self.animal_list.append(animal)
        print(animal.get_name())

    def print_animal(self):
        for item in self.animal_list:
            print(item)

    def get_animal_list(self):
        return self.animal_list



