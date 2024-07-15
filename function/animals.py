template = "|{:^5}|{:<40}|"
delimiter = "—" * 48
head = template.format("№", "Назва тварини")


def show_all_sick_animals(animals: list) -> None:
    print("Список тварин на лікуванні:")
    print(delimiter)
    print(head)
    print(delimiter)

    for i, animal in enumerate(animals):
        print(template.format(i + 1, animal))
    print(delimiter)


def add_animal(animals: list) -> list:
    animals.append(input("Вкажіть ім'я тварини для прийняття на лікування-> "))

    print("Ваша тваринка успішно записана на лікування!")

    return animals


def remove_animal(animals: list, animals_cured: list) -> tuple[list, list]:
    animal_cured = input("Вкажіть кличку тварини щоб забрати її з лікування-> ")

    if animal_cured not in animals:
        print(f"Тварини {animal_cured} немає в списку тварин.")

    else:
        animals.remove(animal_cured)
        animals_cured.append(animal_cured)
        print("Ваша тваринка вилікувана та очікує вас!")

        return animals, animals_cured


def show_all_cured_animals(animals_cured: list) -> None:
    if len(animals_cured) == 0:
        print("Список вилікуваних тварин наразі пустий")

    else:
        print("Список усіх вилікуваних тварин:")
        for animal_cured in animals_cured:
            print(animal_cured)


def find_number_by_name(animals: list) -> list:
    animal_indx = input("Введіть тваринку, номер якої хочете знайти: ")

    if animal_indx not in animals:
        print(f"Тварини {animal_indx} немає в списку тварин.")

    else:
        animal_index = animals.index(animal_indx)
        print(f"Тварина {animal_indx} має номер {animal_index + 1}")

    return animals


def remove_an_incorrectly_added_animal_by_name(animals: list) -> list:
    animals.remove(input("Введіть ім'я тварини щоб відмінити запис на лікування-> "))

    print("Помилковий запис на лікування відмінено!")

    return animals


def remove_an_incorrectly_added_animal_by_number(animals: list) -> list:
    animals.pop(int(input("Введіть номер тварини щоб відмінити запис на лікування-> ")) - 1)

    print("Помилковий запис тварини на лікування відмінено!")

    return animals


def sort_by_alphabet(animals: list) -> list:
    animals_copy = animals.copy()
    animals_copy.sort()

    print("Список тварин на лікування за алфавітом:")
    for animal in animals_copy:
        print(animal)

    return animals


def change_name(animals: list) -> list:
    animal = input("Вкажіть ім'я тваринки яке хочете замінити-> ")
    new_animal_name = input("Введіть нове ім'я тварини-> ")

    animal_indx = animals.index(animal)

    animals.remove(animal)

    animals.insert(animal_indx, new_animal_name)
    print(f"Ім'я вказаної тварини змінилося на {new_animal_name}!")

    return animals


def are_names_palindromes(animals: list) -> list:
    for animal in animals:
        palindrome = animal[::-1].lower()
        if animal.lower() == palindrome:
            print(f"Ім'я '{animal}' є паліндромом")
        else:
            print(f"Ім'я '{animal}' не є паліндромом")

    return animals
