from datetime import datetime

with open("delka_clenstvi.txt") as text_file:
    clen_roky = {}
    clen_pocet_dni = {}

    for line in text_file:
        x = line.replace("\n", "")
        list_of_lines = x.split("\t")
        list_of_lines[4] = list_of_lines[4].replace(" ", "")

        if list_of_lines[4] == "":
            list_of_lines[4] = str(datetime.now().strftime("%d.%m.%Y"))

        d1 = datetime.strptime(list_of_lines[4], "%d.%m.%Y")
        d2 = datetime.strptime(list_of_lines[3], "%d.%m.%Y")

        difference = d1 - d2

        if list_of_lines[0] not in clen_roky.keys():

            clen_roky[list_of_lines[0]] = [(list_of_lines[3], list_of_lines[4])]
            clen_pocet_dni[list_of_lines[0]] = difference.days

        else:
            clen_roky[list_of_lines[0]].append((list_of_lines[3], list_of_lines[4]))
            clen_pocet_dni[list_of_lines[0]] += difference.days

    for x, y in clen_pocet_dni.items():
        print(f"{round(y / 365.25, 1)}")
