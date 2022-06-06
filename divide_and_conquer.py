import math
from timeit import default_timer as timer

global x, x_oben, mitte, mitte_neu, minimal_intervall, rek_aufrufe, intervall, fnk_aufrufe

nullstellen = []
rek_aufrufe = 0
fnk_aufrufe = 0

x = 0
x_oben = 10

minimal_intervall = 0.0001
intervall = 0.1

def f(x):
    global fnk_aufrufe
    fnk_aufrufe += 1
    return math.sin(x) + 0.3

def IntervallTeilen(x, x_oben):
    mitte = (x + x_oben) / 2
    return mitte

def checkVZW(x, x_oben):
    global rek_aufrufe

    # Abbruchbedingung
    if (f(x_oben) == 0 or f(x) == 0):
        nullstellen.append(x)
        return x

    if ((f(x) > 0 and f(x_oben) > 0) or (f(x) < 0 and f(x_oben) < 0)):
        return None

    if ((x_oben - x) <= minimal_intervall):
        nullstellen.append(x)
        return x

    # rekursive Aufrufe
    mitte_neu = IntervallTeilen(x, x_oben)

    ergebnis_links = checkVZW(x, mitte_neu)
    rek_aufrufe += 1
    ergebnis_rechts = checkVZW(mitte_neu, x_oben)
    rek_aufrufe += 1

    if (ergebnis_links != None):
        return ergebnis_links
    if (ergebnis_rechts != None):
        return ergebnis_rechts

# main
start = timer()
while (x < x_oben):
    if ((f(x) > 0 and f(x + intervall) < 0) or (f(x) < 0 and f(x + intervall) > 0)):
        checkVZW(x, x + intervall)
    x += intervall
end = timer()

#Auswertung
print("""
  _____  _       _     _                        _    _____
 |  __ \(_)     (_)   | |                      | |  / ____|
 | |  | |___   ___  __| | ___    __ _ _ __   __| | | |     ___  _ __   __ _ _   _  ___ _ __
 | |  | | \ \ / / |/ _` |/ _ \  / _` | '_ \ / _` | | |    / _ \| '_ \ / _` | | | |/ _ \ '__|
 | |__| | |\ V /| | (_| |  __/ | (_| | | | | (_| | | |___| (_) | | | | (_| | |_| |  __/ |
 |_____/|_| \_/ |_|\__,_|\___|  \__,_|_| |_|\__,_|  \_____\___/|_| |_|\__, |\__,_|\___|_|
                                                                         | |
                                                                         |_|
""")
print("-"*20)
print("Es wurden ", len(nullstellen), " Nullstellen gefunden.")
print("Nullstellen liegen bei: ", nullstellen)
print(" ")
print("Durchgefuerte rekursive Aufrufe: ", rek_aufrufe)
print(" ")
print("Aufrufe der Funktion: ", fnk_aufrufe)
print(" ")
print("Zeit: ", end - start)
print("-"*20)
