from animal import Animal


class Animal_dict:
    def __init__(self):
        self.animal_dict = {}


    def add_animal(self, name, type_animal, birthday, command):
        animal = Animal(name=name, type_animal=type_animal, birthday=birthday, command=command)
        key_animal = 0
        for key in self.animal_dict.keys():
            key_animal = int(key) + 1
        animal.id_entry = str(key_animal)
        self.animal_dict[animal.id_entry] = [animal.name, animal.type_animal, animal.birthday, animal.command]

    def print_animal(self):
        for key, value in self.animal_dict.items():
            print(key, value)

    def print_animal_command(self):
        for value in self.animal_dict.values():
            print(value[3])



