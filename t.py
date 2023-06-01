def tarkista_tilinumero(tilinumero):
    
    tilinumero = tilinumero.replace(" ", "")
    if len(tilinumero) != 18:
        return False

    
    tilinumero = tilinumero[4:] + tilinumero[:4]

    
    tilinumero = "".join(str(ord(c) - 55) if c.isalpha() else c for c in tilinumero)

    
    jakojäännös = int(tilinumero) % 97
    return jakojäännös == 1



tilinumero = input("Anna tilinumerosi")
print(tilinumero)
if tarkista_tilinumero(tilinumero):
    print("Tilinumerosi on aito.")
else:
    print("Tilinumerosi ei ole aito.")

