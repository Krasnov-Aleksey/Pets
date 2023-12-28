from animaldict import AnimalDict

animal_dict = AnimalDict()


def add_animal_pr(name, type_animal, command):
    animal_dict.add_animal(name, type_animal, command)


def print_animal_pr():
    animal_dict.print_animal()


def print_animal_command_pr(id_animal):
    animal_dict.print_animal_command(id_animal)


def add_animal_command_pr(id_animal, command):
    animal_dict.add_animal_command(id_animal, command)

