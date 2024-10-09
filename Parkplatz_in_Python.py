import os
os.system('clear' if os.name == 'posix' else 'cls')

#Array initialisieren
Parkplatz = [0, 1, 2, 2, 1, 0, 0, 0, 1, 1]

def Bereich(eingabe, unten, oben):
    if eingabe >= unten and eingabe <= oben:
        return True
    else:
        return False
    

while True:
    for index, i in enumerate(Parkplatz):
        match i:
            case 0:
                print(f"Parkplatz {index + 1} ist frei")
            case 1:
                print(f"Parkplatz {index + 1} ist belegt")
            case 2:
                print(f"Parkplatz {index + 1} ist reserviert")
            case _:
                print("error")
    
    #Eingabe
    while True:
        istatus = int(input("Geben Sie den Status an (0:löschen 1:belegt 2:reserviert): "))

        valid = Bereich(istatus, 0, 2)

        if valid == True:
            break
        else:
            print("Falsche Eingabe")    
    
    while True:
        ParkplatzNr = int(input("Geben Sie die Parkplatz-Nummer an: "))
        valid = Bereich(ParkplatzNr, 1, 10)
        
        if valid == True:
            break
        else:
            print("Falsche Eingabe")    

    match istatus:
        case 0:
            print(f"Parkplatz {ParkplatzNr} wurde freigegeben \n") 
            Parkplatz[ParkplatzNr - 1] = 0
            break
        case 1:
            print(f"Parkplatz {ParkplatzNr} wurde belegt \n")
            Parkplatz[ParkplatzNr - 1] = 1
            break
        case 2:
            print(f"Parkplatz {ParkplatzNr} wurde reserviert \n")
            Parkplatz[ParkplatzNr - 1] = 2
            break
        case _:
            print("Ungültige Eingabe \n")
            break


