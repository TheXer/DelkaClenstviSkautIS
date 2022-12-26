import dataclasses
from datetime import datetime
import csv
from typing import Any

COLUMN_UNNEEDED = 7
TODAY_DATE_COLUMN = 4
DATE_OF_REGISTRATION = 3

@dataclasses.dataclass()
class Person:
    name: str
    ID: str
    date_of_birth: str
    registration_date: str
    registration_expiry: str
    membership_type: str
    group_type: str


def txt_to_person(path_to_txt: str) -> list[Person]:
    with open(path_to_txt, "r") as data:
        clean_list_of_members = []
        for line in data:
            x = line.replace("\n", "")
            list_of_lines = x.split("\t")
            list_of_lines[TODAY_DATE_COLUMN] = list_of_lines[TODAY_DATE_COLUMN].replace(" ", "")

            if list_of_lines[TODAY_DATE_COLUMN] == "":
                list_of_lines[TODAY_DATE_COLUMN] = str(datetime.now().strftime("%d.%m.%Y"))

            person = Person(*list_of_lines[:COLUMN_UNNEEDED])
            clean_list_of_members.append(person)

    return clean_list_of_members


def make_csv_file(person_list: list[Person]) -> None:
    with open("log.csv", "w") as out_file:
        writer = csv.writer(out_file, delimiter=" ")

        for member in person_list:
            writer.writerow([
                member.name,
                member.ID,
                member.date_of_birth,
                member.registration_date,
                member.registration_expiry,
                member.membership_type,
                member.group_type])


def years_actual_members(member_list: list[Person]) -> dict[str, list[tuple[str, str]]]:
    """Get only new members"""

    all_members = {}

    for person in member_list:
        all_members.setdefault(person.name, []).append((person.registration_date, person.registration_expiry))

    actual_members = {
        x: y
        for x, y in all_members.items()
        for date in y
        if datetime.now().strftime("%d.%m.%Y") in date
    }

    return actual_members


def years_all_members(member_list: list[Person]) -> dict[Person, list[tuple[str, str]]]:
    """Get all members"""

    all_members = {}
    for person in member_list:
        all_members.setdefault(person.name, []).append((person.registration_date, person.registration_expiry))

    return all_members


def count_days(members: dict) -> dict[Any, float]:
    """Funkce pro výpočet členství zaokrouhlené na roky"""

    days = {}
    for name, dates in members.items():
        for date in dates:
            d1 = datetime.strptime(date[0], "%d.%m.%Y")
            d2 = datetime.strptime(date[1], "%d.%m.%Y")

            diff = d2 - d1
            years = round(diff.days / 365.25, 1)

            if name not in days.keys():
                days[name] = years
            else:
                days[name] += years

    return days


if __name__ == '__main__':

    persons = txt_to_person("delka_clenstvi.txt")
    make_csv_file(persons)
