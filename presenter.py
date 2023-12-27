from animal_dict import Animal_dict

animal_dict = Animal_dict()


def add_animal_pr(name, type_animal, birthday, command):
    animal_dict.add_animal(name, type_animal, birthday, command)


def print_animal_pr():
    animal_dict.print_animal()

