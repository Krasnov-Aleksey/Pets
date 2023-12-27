import presenter
def main_menu():
    # TODO текст в отдельный файл
    flag = True
    while(flag):
        print("""Меню
1 Добавить домашнее животное
2 Добавить вьючное животное
3 Показать список животных
4 Показать список команд животного
5 Добавить команду животному
6 Выход""")
        choice = input("Введите пункт меню ")
        match choice:
            case "1":
                name = "R" #input("Введите имя домашнего животного ")
                type_animal = "Домашнее животное"
                birthday = 1 #input("Введите день рождение животного ")
                command = "stop" #input("Введите команды животного ")
                presenter.add_animal_pr(name, type_animal, birthday, command)
            case "2":
                name = "T"# input("Введите имя вьючного животного ")
                type_animal = "Вьючное животное"
                birthday = 2 #input("Введите день рождение животного ")
                command = "go" #input("Введите команды животного ")
                presenter.add_animal_pr(name, type_animal, birthday, command)
            case "3":
                presenter.print_animal_pr()
            case "4":
                presenter.print_animal_command_pr()
            case "5":
                pass
            case "6":
                flag = False
            case _:
                print("Неверный пункт меню")
