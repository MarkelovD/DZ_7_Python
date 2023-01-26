from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
from view import show_menu




def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Коментарий: ")
    return [last_name, first_name, phone_number, note]


def choice_sep():
    while True:
        sep = input("Введите разделитель: ")
        collection = [";",":",",",""]
        if sep in collection:
            return sep
        else:
            print("повторите попытку")


def choice_todo():
    while True:
        show_menu()
        ch = input("Введите операцию: ")
        if ch == '1':
            sep = choice_sep()
            import_data(input_data(), sep)
        elif ch == '2':
            data = export_data()
            print_data(data)
        elif ch =="3":
            word = input("Введите данные для поиска: ")
            data = export_data()
            item = search_data(word, data)
            if item != None:
                print("Фамилия".center(20), "Имя".center(20),
                    "Номер телефона".center(15), "Примечание".center(30))
                print("-"*85)
                print(item[0].center(20), item[1].center(20),
                    item[2].center(15), item[3].center(30))
            else:
                print("Справочник пуст")     
        else:
            break
        