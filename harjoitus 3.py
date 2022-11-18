# Auto1 = Auto()
# Autot = [merkki, väri, paino,vuosimali,kilometri]
# Autot.append(Auto1)
# 
# merkki = ["merssu", "cadillac","volvo"]
# väri = [" tummansininen,"," punainen,","vihreä"]
# paino = ["1200", "1000", "2500"]
# vuosimali = ["1994","1999","1985"]
# kilometri = ["200000","350000","150000"]
# print(Autot)

class Auto:
    merkki = ""
    vuosi = 0
    väri = ""
    kilometri = 0
    paino = 0
    hinta = 0
    
Autot = []
    
uusiAuto = Auto()
uusiAuto.merkki = "Mersu"
uusiAuto.väri = "Tummapunainen"
uusiAuto.vuosi = 1994
uusiAuto.kilometri = 200000
uusiAuto.paino  = 1500
uusiAuto.hinta = 15000
Autot.append(uusiAuto)
print("Autot =", Autot)
Auto()
# uusiAuto = Auto()
# 
# Autot.append(uusiAuto.väri)
# 
# uusiAuto = Auto()
# uusiAuto.vuosi = 1994
# Autot.append(uusiAuto.vuosi)
# 
# uusiAuto = Auto()
# uusiAuto.kilometri = 200000
# Autot.append(uusiAuto.kilometri)
# 
# uusiAuto = Auto()
# uusiAuto.paino  = 1500
# Autot.append(uusiAuto.paino)
# 
# uusiAuto = Auto()
# uusiAuto.hinta = 15000
# Autot.append(uusiAuto.hinta)
# 
# print("Autot =", Autot)
# Auto()
