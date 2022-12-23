from datetime import datetime
import csv
from typing import Any

COLUMN_UNNEEDED = 7
TODAY_DATE_COLUMN = 4
DATE_OF_REGISTRATION = 3
NAME_SURNAME_NICKNAME = 0


def convert_from_txt_to_csv(path_to_txt: str) -> None:
    """Funkce pro příjem txt file ze skautISu a vypláznutí csv file z toho"""

    with open(path_to_txt, "r") as data:
        clean_list_of_members = []
        for line in data:
            x = line.replace("\n", "")
            list_of_lines = x.split("\t")
            list_of_lines[TODAY_DATE_COLUMN] = list_of_lines[TODAY_DATE_COLUMN].replace(" ", "")

            if list_of_lines[TODAY_DATE_COLUMN] == "":
                list_of_lines[TODAY_DATE_COLUMN] = str(datetime.now().strftime("%d.%m.%Y"))

            clean_list_of_members.append(list_of_lines)

    with open("log.csv", "w") as out_file:
        writer = csv.writer(out_file, delimiter=" ")
        for member in clean_list_of_members:
            writer.writerow(member[:COLUMN_UNNEEDED])


def years_actual_members(path_to_csv_file: str) -> dict[str, list[tuple[str, str]]]:
    """Get only new members"""

    all_members = {}

    with open(path_to_csv_file) as cfile:
        csvreader = csv.reader(cfile, delimiter=" ")

        # iterování všech záznamů v csv a seřazení těch záznamů
        for x in csvreader:
            all_members.setdefault(x[NAME_SURNAME_NICKNAME], []).append((x[DATE_OF_REGISTRATION], x[TODAY_DATE_COLUMN]))

        actual_members = {
            x: y
            for x, y in all_members.items()
            for date in y
            if datetime.now().strftime("%d.%m.%Y") in date
        }

    return actual_members


def years_all_members(path_to_csv_file: str) -> dict[str, list[tuple[str, str]]]:
    """Get all members"""

    all_members = {}
    with open(path_to_csv_file) as cfile:
        csvreader = csv.reader(cfile, delimiter=" ")

        for x in csvreader:
            all_members.setdefault(x[NAME_SURNAME_NICKNAME], []).append((x[DATE_OF_REGISTRATION], x[TODAY_DATE_COLUMN]))

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


