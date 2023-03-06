Program pro výpočet délky členství ve skautISu. Protože jak jsem zjistil, tak SkautIS měří jen délku aktuální přihlášky, nikoliv délku celkového členství. Tenhle program by měl pomoci tenhle nedostatek vyřešit.

# Jak použít?
- Zkopírovat všechny členy ve tabulce ve "Moje - Moje jednotka - Členové" (nezapomeňte taky dát "Zobrazit i historii")
- Uložit do nějakého text file, třeba poznámkový blok
- Pojmenovat to třeba "clenove.txt"

```py
# Kód bere jakýkoliv text file
list_of_members = UsersList("clenove.txt")

# Jára Cimrman (Jarda)	999999/0000 23.09.2015 23.10.2021 23.10.2024  Hostování Oldskaut

vsichni_clenove = list_of_members.compute_days(everyone=True)

for x, y in vsichni_clenove.items():
    print(f"Jsem {x} a chodil jsem {y} roky!")
    
    # Jsem Jára Cimrman (Jarda) a chodil jsem 3 roky!
```


