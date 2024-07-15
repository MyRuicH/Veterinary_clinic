from datetime import datetime


def add_employee(employees: dict) -> dict:
    username = input("Введіть логін працівника: ")
    position = input("Вкажіть посаду працівника: ")
    salary = input("Вкажіть ЗП працівника: ")
    name = input("Вкажіть ім'я працівника: ")
    password = input("Введіть пароль для працівника: ")

    if username not in employees:
        employees[username] = {
            "position": position,
            "salary": salary,
            "start_date": datetime.now().strftime("%d.%m.%Y"),
            "name": name,
            "password": password
        }
        print("Працівника успішно зареєстровано в системі.")
    else:
        print("Такий логін вже зареєстрований в системі.")

    return employees


def remove_employee(employees: dict) -> dict:
    username = input("Вкажіть логін працівника, якого хочете видалити: ")
    if username in employees:
        del employees[username]
        print("Працівника успішно видалено.")
    else:
        print("Такого працівника немає у списку.")

    return employees


def show_all_employees(employees: dict) -> None:
    print("Список працівників:\n")
    for i, employee in employees.items():
        print(f"{i}:\n{employee}")


def change_employee_salary(employees: dict) -> dict:
    username = input("Вкажіть логін працівника: ")
    salary = input("Вкажіть нову зарплату працівника: ")

    if username in employees:
        employees[username]["salary"] = salary
        print("Зарплата працівника змінена.")
    else:
        print("Такого працівника немає у списку.")

    return employees


def change_employee_position(employees: dict) -> dict:
    username = input("Вкажіть логін працівника: ")
    position = input("Вкажіть нову посаду працівника: ")

    if username in employees:
        employees[username]["position"] = position
        print("Посада працівника змінена.")
    else:
        print("Такого працівника немає у списку.")

    return employees
