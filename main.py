from pprint import pprint
from datetime import datetime


from function.password import is_verify_password, generate_password
from function.animals import (
    show_all_sick_animals,
    add_animal,
    remove_animal,
    show_all_cured_animals,
    find_number_by_name,
    remove_an_incorrectly_added_animal_by_name,
    remove_an_incorrectly_added_animal_by_number,
    sort_by_alphabet,
    change_name,
    are_names_palindromes
)
from function.reviews import add_review, find_repeated_chars
from function.employees import (
    add_employee,
    remove_employee,
    show_all_employees,
    change_employee_salary,
    change_employee_position
)
from files import list_files, open_files, save_files


def help():
    print("Список команд:\n")
    with open(list_files.help, "r", encoding="utf-8") as fh:
        print(fh.read())


def show_log(log: list) -> None:
    print("ЛОГ:")
    pprint(log)


def show_the_most_repeated_commands(most_using_command: dict) -> None:
    print("Список команд та їх частота використання:")
    pprint(most_using_command)


def exit_the_program():
    print("Дякуємо що звернулися до нашої клініки!")
    quit()


def main():
    animals = open_files.animals
    employees = open_files.employees
    animals_cured = open_files.animals_cured
    reviews = open_files.reviews
    log = open_files.log
    most_using_command = open_files.most_using_command

    user_name = input("Введіть свій логін: ")
    pass_word = employees.get(user_name, {}).get("password", "")

    while not pass_word:
        position = input("Вкажіть вашу посаду: ")
        salary = input("Вкажіть свою ЗП: ")
        name = input("Вкажіть ваше ім'я: ")
        start_date = input("Введіть дату початку роботи у такому форматі(01.01.2024): ")
        employees[user_name] = {
            "position": position,
            "salary": salary,
            "start_date": start_date,
            "name": name,
        }

        print("\nДоброго дня! Вас вітає Veterinary_clinic 'ОЛВЕТ'."
              "\nДля використання наших послуг створіть пароль для входу у систему\n")
        command = input("Введіть 'create' для введення свого паролю,"
                        " або 'generate' для автоматичної генерації паролю\n-> ")

        if command == "create":
            password = input("Введіть свій пароль:\nПароль повинен бути не менше 8 символів,"
                             "та має містити хоча б 1 букву та 1 цифру\n-> ")

            if is_verify_password(password):
                pass_word = password
            else:
                print("Пароль не пройшов перевірку")

        elif command == "generate":
            len_pass = input("Вкажіть довжину паролю, або залиште за замовчуванням(8 символів)\n-> ")
            if len_pass.isdigit() and int(len_pass) > 7:
                len_pass = int(len_pass)
            else:
                len_pass = 8

            is_upper = input("Чи використовувати великі літери: 1 - так, Enter - ні\n-> ")
            is_upper = True if is_upper == "1" else False
            is_punctuation = input("Чи використовувати спецсимволи: 1 - так, Enter - ні\n-> ")
            is_punctuation = True if is_punctuation == "1" else False
            is_repeat = input("Чи можуть символи повторюватися: 1 - так, Enter - ні\n-> ")
            is_repeat = True if is_repeat == "1" else False

            password = generate_password(len_password=len_pass, is_upper=is_upper,
                                         is_punctuation=is_punctuation, is_repeat=is_repeat)

            if is_verify_password(password):
                pass_word = password
            else:
                print("Пароль не пройшов перевірку")

    else:
        print(f"Ваш пароль {pass_word} успішно створено. Запам'ятайте його!")
        input("Натисніть 'Enter' для продовження")

    password = input("\nВведіть пароль для входу в систему\n-> ")

    command = None
    while pass_word == password:
        if not command:
            log.append(f"Користувач під логіном '{user_name}' увійшов в систему: {datetime.now()}")
            print("Доброго дня. Вітаємо в нашій інформаційній системі")

        command = input("\nВведіть команду(help для допомоги)-> ")
        log.append(f"Користувач під логіном '{user_name}' ввів команду {command}: {datetime.now()}")

        if command in most_using_command:
            most_using_command[command] += 1
        else:
            most_using_command[command] = 1

        match command:
            case "show all sick animals":
                show_all_sick_animals(animals)
            case "add animal":
                animals = add_animal(animals)
            case "remove animal":
                animals, animals_cured = remove_animal(animals, animals_cured)
            case "show all cured animals":
                show_all_cured_animals(animals_cured)
            case "find number by name":
                animals = find_number_by_name(animals)
            case "remove an incorrectly added animal by name":
                animals = remove_an_incorrectly_added_animal_by_name(animals)
            case "remove an incorrectly added animal by number":
                animals = remove_an_incorrectly_added_animal_by_number(animals)
            case "sort by alphabet":
                animals = sort_by_alphabet(animals)
            case "change name":
                animals = change_name(animals)
            case "are names palindromes":
                animals = are_names_palindromes(animals)
            case "add review":
                reviews = add_review(reviews)
            case "find repeated chars":
                find_repeated_chars(reviews)
            case "add employee":
                employees = add_employee(employees)
            case "remove employee":
                employees = remove_employee(employees)
            case "show all employees":
                show_all_employees(employees)
            case "change employee salary":
                employees = change_employee_salary(employees)
            case "change employee position":
                employees = change_employee_position(employees)
            case "show Log":
                show_log(log)
            case "show the most repeated commands":
                show_the_most_repeated_commands(most_using_command)
            case "exit":
                save_files.save_animals(animals)
                save_files.save_reviews(reviews)
                save_files.save_animals_cured(animals_cured)
                save_files.save_employees(employees)
                save_files.save_log(log)
                save_files.save_most_using_command(most_using_command)
                exit_the_program()
            case "help":
                help()
        input("\nНатисніть 'Enter' для продовження")

    else:
        print("Пароль введено неправильно. Доступ заблоковано")


if __name__ == "__main__":
    main()
