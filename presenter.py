from animal_list import AnimalList

animal_list = AnimalList()


def add_animal_p(name, type_animal, birthday, command):
    animal_list.add_animal(name, type_animal, birthday, command)


def print_animal_p():
     animal_list.print_animal()
