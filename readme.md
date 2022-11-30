Program pro výpočet délky členství ve skautISu. Protože jak jsem zjistil, tak SkautIS měří jen délku aktuální přihlášky, nikoliv délku celkového členství. Tenhle program by měl pomoci tenhle nedostatek vyřešit.

# Jak použít?
- Zkopírovat všechny členy ve tabulce ve "Moje - Moje jednotka - Členové" (nezapomeňte taky dát "Zobrazit i historii")
- Uložit do nějakého text file, třeba poznámkový blok
- Pojmenovat to třeba "clenove.txt"

```py
# tohle nám automaticky vytvoří csv file s názvem "log.csv" ve tvaru
# Jméno + příjmení + přezdívka, rodné číslo, datum narození, datum registrace, datum ukončení, typ členství, družina
# CSV file je rozděleno na mezerníky, nevyužívám separátory jako čárky
convert_from_txt_to_csv("clenove.txt")

# Jára Cimrman (Jarda)	999999/0000 23.09.2015 23.10.2021 23.10.2024  Hostování Oldskaut

vsichni_clenove = roky_vsichni_clenove("log.csv")

# {"Jára Cimrman (Jarda)": [(23.10.2021, 23.10.2024)]}

for x, y in pocet_dni_clenove(vsichni_clenove).items():
    print(f"Jsem {x} a chodil jsem {y} roky!")
    
    # Jsem Jára Cimrman (Jarda) a chodil jsem 3 roky!
```


