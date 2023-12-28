from animal import Animal
import text


class AnimalDict:
    def __init__(self):
        self.animal_dict = {}

    def add_animal(self, name, type_animal, command):
        animal = Animal(name=name, type_animal=type_animal, command=command)
        key_animal = 0
        for key in self.animal_dict.keys():
            key_animal = int(key) + 1
        animal.id_entry = str(key_animal)
        self.animal_dict[animal.id_entry] = [animal.name, animal.type_animal, animal.command]

    def print_animal(self):
        for key, value in self.animal_dict.items():
            print(key, value)

    def print_animal_command(self, id_animal):
        for key, value in self.animal_dict.items():
            if id_animal in key:
                print(f"{key} {value[2]}")
                return
        print(text.id_not_found)

    def add_animal_command(self, id_animal, command):
        for key, value in self.animal_dict.items():
            if id_animal in key:
                value[2] = f"{value[2]}, {command}"
                return
        print(text.id_not_found)
