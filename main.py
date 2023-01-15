import dataclasses
import pathlib
from datetime import datetime
import csv

INPUT_DIRECTORY = pathlib.Path(__file__).parent


@dataclasses.dataclass()
class User:
    name: str
    ID: str
    date_of_birth: str
    registration_date: str
    registration_expiry: str
    membership_type: str
    group_type: str


class UsersList:
    def __init__(self, txt_name: str) -> None:
        self.COLUMN_UNNEEDED = 7
        self.TODAY_DATE_COLUMN = 4
        self.DATE_OF_REGISTRATION = 3

        self.user_list = self._user_list_init(txt_name)

    def _user_list_init(self, txt_path: str) -> list[User]:
        with open(INPUT_DIRECTORY / txt_path, "r") as data:
            clean_list_of_members = []

            for line in data:
                x = line.replace("\n", "")
                list_of_lines = x.split("\t")
                list_of_lines[self.TODAY_DATE_COLUMN] = list_of_lines[self.TODAY_DATE_COLUMN].replace(" ", "")

                if list_of_lines[self.TODAY_DATE_COLUMN] == "":
                    list_of_lines[self.TODAY_DATE_COLUMN] = str(datetime.now().strftime("%d.%m.%Y"))

                user = User(*list_of_lines[:self.COLUMN_UNNEEDED])
                clean_list_of_members.append(user)

        return clean_list_of_members

    def _compute_membership_years_all(self) -> dict[User, list[tuple[str, str]]]:

        all_users = {}
        for user in self.user_list:
            all_users.setdefault(user.name, []).append((user.registration_date, user.registration_expiry))

        return all_users

    def membership_years(self) -> dict[User, list[tuple[str, str]]]:
        return {user: years
                for user, years in self._compute_membership_years_all().items()
                for year in years
                if datetime.now().strftime("%d.%m.%Y") in year}

    def compute_days(self, everyone: bool = False) -> dict[User, float]:
        if everyone:
            users = self._compute_membership_years_all()
        else:
            users = self.membership_years()
        days = {}
        for name, years in users.items():
            for date in years:
                date1 = datetime.strptime(date[0], "%d.%m.%Y")
                date2 = datetime.strptime(date[1], "%d.%m.%Y")

                diff = date2 - date1
                years = round(diff.days / 365.25, 1)

                if name not in days.keys():
                    days[name] = years
                else:
                    days[name] += years

        return days


def make_csv_file(person_list: list[User]) -> None:
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


if __name__ == "__main__":
    lol = UsersList("delka_clenstvi.txt")
    print(lol.compute_days(everyone=True))
