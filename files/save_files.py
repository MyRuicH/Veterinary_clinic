import json

from files import list_files


def save_animals(animals: list) -> None:
    animals = [animal + "\n" for animal in animals]
    with open(list_files.animals, "w", encoding="utf-8") as fh:
        fh.writelines(animals)


def save_reviews(reviews: list) -> None:
    reviews = [review + "\n" for review in reviews]
    with open(list_files.reviews, "w", encoding="utf-8") as fh:
        fh.writelines(reviews)


def save_animals_cured(animals_cured: list) -> None:
    with open(list_files.animals_cured, "w", encoding="utf-8") as fh:
        json.dump(animals_cured, fh, indent=4)


def save_employees(employees: dict) -> None:
    with open(list_files.employees, "w", encoding="utf-8") as fh:
        json.dump(employees, fh, indent=4)


def save_log(log: list) -> None:
    with open(list_files.log, "w", encoding="utf-8")as fh:
        json.dump(log, fh, indent=4)


def save_most_using_command(most_using_command: dict) -> None:
    with open(list_files.most_using_command, "w", encoding="utf-8") as fh:
        json.dump(most_using_command, fh, indent=4)

