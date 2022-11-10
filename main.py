from datetime import datetime
import csv


def convert_from_txt_to_csv(txt):
    """Funkce pro příjem txt file ze skautISu a vypláznutí csv file z toho"""

    with open(txt, "r") as data:
        lst = []
        for line in data:
            x = line.replace("\n", "")
            list_of_lines = x.split("\t")
            list_of_lines[4] = list_of_lines[4].replace(" ", "")

            if list_of_lines[4] == "":
                list_of_lines[4] = str(datetime.now().strftime("%d.%m.%Y"))

            lst.append(list_of_lines)

    with open("log.csv", "w") as out_file:
        writer = csv.writer(out_file, delimiter=" ")
        for x in lst:
            try:
                x.pop(7)
            except IndexError:
                pass
            finally:
                writer.writerow(x)


def roky_dnesni_clenove(csv_file):
    """Získat dnešní členy"""

    clen_roky_vsichni = {}
    with open(csv_file) as cfile:
        csvreader = csv.reader(cfile, delimiter=" ")

        # iterování všech záznamů v csv a seřazení těch záznamů
        for x in csvreader:
            if x[0] not in clen_roky_vsichni.keys():
                clen_roky_vsichni[x[0]] = [(x[3], x[4])]
            else:
                clen_roky_vsichni[x[0]].append((x[3], x[4]))

        aktualni_clenove = {
            x: y
            for x, y in clen_roky_vsichni.items()
            for date in y
            if datetime.now().strftime("%d.%m.%Y") in date
        }
    return aktualni_clenove


def roky_vsichni_clenove(csv_file):
    """Získat všechny členy"""

    clen_roky_vsichni = {}
    with open(csv_file) as cfile:
        csvreader = csv.reader(cfile, delimiter=" ")

        # iterování všech záznamů v csv a seřazení těch záznamů
        for x in csvreader:
            if x[0] not in clen_roky_vsichni.keys():
                clen_roky_vsichni[x[0]] = [(x[3], x[4])]
            else:
                clen_roky_vsichni[x[0]].append((x[3], x[4]))

    return clen_roky_vsichni


def pocet_dni_clenove(dct):
    """Funkce pro výpočet členství zaokrouhlené na roky"""

    pocet_dni = {}
    for x, y in dct.items():
        for date in y:
            d1 = datetime.strptime(date[0], "%d.%m.%Y")
            d2 = datetime.strptime(date[1], "%d.%m.%Y")

            diff = d2 - d1
            years = round(diff.days / 365.25, 1)

            if x not in pocet_dni.keys():
                pocet_dni[x] = years
            else:
                pocet_dni[x] += years

    return pocet_dni

if __name__ == "__main__":
    convert_from_txt_to_csv("delka_clenstvi.txt")
    rslt = roky_vsichni_clenove("log.csv")

    for x, y in pocet_dni_clenove(rslt).items():
        print(x, y)