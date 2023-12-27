import presenter

def main_menu():
    # TODO текст в отдельный файл
    flag = True
    while(flag):
        print("""Меню
1 Добавить домашнее животное
2 Добавить вьючное животное
3 Показать список команд животного
4 Показать список животных
5 Выход""")
        choice = input("Введите пункт меню ")
        match choice:
            case "1":
                name = input("Введите имя животного ")
                type_animal = input("Введите тип животного ")
                birthday = input("Введите день рождение животного ")
                command = input("Введите команды животного ")
                presenter.add_animal_p(name, type_animal, birthday, command)
            case "2":
                print("Выбран 2 пункт меню")
            case "3":
                presenter.print_animal_p()
            case "4":
                presenter.print_animal_p()
            case "5":
                print("Выбран 9 пункт меню")
                flag = False
            case _:
                print("Неверный пункт меню")
