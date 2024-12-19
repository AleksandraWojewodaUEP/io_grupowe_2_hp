def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    ceny = {
        'lokalna' : {'list': (0, 0, 2), 'paczka': (0, 0, 7)},
        'krajowa' : {'list': (0, 0, 12), 'paczka': (0, 1, 2)},
        'dalekobiezna' : {'list': (0, 0, 20), 'paczka': (0, 2, 1)}
    } #g s k

    galeony, sykle, knuty = ceny[odleglosc][typ]

    if potwierdzenie_odbioru == True:
        knuty += 7

    if specjalna == 'wyjec':
        knuty += 4
    elif specjalna == 'list gonczy':
        sykle += 1

    return {'galeony' : galeony, 'sykle' : sykle, 'knuty' : knuty}

print(wybierz_sowe_zwroc_koszt(True, 'dalekobiezna', 'paczka', 'list gonczy'))

#Zadanie 5
def waluta_dict_na_str(fundusz):
    nazwy_monet = {1: 'galeon', 2: 'sykl', 3: 'knut'}

    posortowane_klucze = sorted(fundusz.keys(), reverse=False)
    wynik = []
    for klucz in posortowane_klucze:
        if fundusz[klucz] != 0:  # Pomijamy monety o wartości zerowej
            wynik.append(f"{fundusz[klucz]} {nazwy_monet[klucz]}")
    return ', '.join(wynik)

fundusz = {1: 50, 2: 10, 3: 3}
print(waluta_dict_na_str(fundusz))

# Zadanie 3
def licz_sume(slownik):
    galeon = sum(slownik['galeon'])
    sykl = sum(slownik['sykl'])
    knut = sum(slownik['knut'])

    sykl += knut // 21
    knut = knut % 21

    galeon += sykl // 17
    sykl = sykl % 17

    return {"galeon" : galeon, "sykl" : sykl, "knut" : knut}


slownik = {
    "galeon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
}

print(licz_sume(slownik))