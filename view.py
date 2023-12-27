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
                name = input("Введите имя домашнего животного ")
                type_animal = "Домашнее животное"
                birthday = 1 #input("Введите день рождение животного ")
                command = 1 #input("Введите команды животного ")
                presenter.add_animal_pr(name, type_animal, birthday, command)
            case "2":
                name = input("Введите имя вьючного животного ")
                type_animal = "Вьючное животное"
                birthday = 2 #input("Введите день рождение животного ")
                command = 2 #input("Введите команды животного ")
                presenter.add_animal_pr(name, type_animal, birthday, command)

            case "3":
                pass
            case "4":
                presenter.print_animal_pr()
            case "5":
                print("Выбран 5 пункт меню")
                flag = False
            case _:
                print("Неверный пункт меню")
