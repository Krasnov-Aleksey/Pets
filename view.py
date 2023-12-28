import presenter
import text

def main_menu():
    flag = True
    while(flag):
        print(text.main_menu_text)
        choice = input(text.input_menu_item)
        match choice:
            case "1":
                name = input(text.input_name_pet)
                type_animal = text.pet
                command = input(text.input_command_animal)
                presenter.add_animal_pr(name, type_animal, command)
            case "2":
                name = input(text.input_name_animal_pack)
                type_animal = text.animal_pack
                command = input(text.input_command_animal)
                presenter.add_animal_pr(name, type_animal, command)
            case "3":
                presenter.print_animal_pr()
            case "4":
                id_animal = input(text.input_id_animal)
                presenter.print_animal_command_pr(id_animal)
            case "5":
                id_animal = input(text.input_id_animal)
                command = input(text.input_new_command_animal)
                presenter.add_animal_command_pr(id_animal, command)
            case "6":
                flag = False
            case _:
                print(text.invalid_menu_item)
