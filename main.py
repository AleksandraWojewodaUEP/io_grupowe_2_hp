<<<<<<< HEAD
def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna=""):
    koszt = {
        "galeon": 0,
        "sykl": 0,
        "knut": 0
    }

    # Koszty bazowe w zależności od odległości i typu
    if odleglosc == "lokalna":
        if typ == "list":
            koszt["knut"] += 2
        elif typ == "paczka":
            koszt["knut"] += 7
    elif odleglosc == "krajowa":
        if typ == "list":
            koszt["sykl"] += 1
            koszt["knut"] += 2
        elif typ == "paczka":
            koszt["sykl"] += 2
            koszt["knut"] += 1
    elif odleglosc == "dalekobiezna":
        if typ == "list":
            koszt["sykl"] += 2
        elif typ == "paczka":
            koszt["sykl"] += 4

    # Dodatkowe koszty za potwierdzenie odbioru
    if potwierdzenie_odbioru:
        koszt["knut"] += 7

    # Dodatkowe koszty za opcję specjalną, jeśli została wybrana
    if specjalna == "wyjec":
        koszt["knut"] += 4
    elif specjalna == "list gończy":
        koszt["sykl"] += 1

    return koszt


# Przykładowe wywołanie funkcji z opcją specjalną wyjec
koszt = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')
print(koszt)

# Przykładowe wywołanie funkcji bez opcji specjalnej
koszt_bez_specjalnej = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list')
print(koszt_bez_specjalnej)

koszt = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'list gończy')
print(koszt)

=======
def licz_sume(monety):
    # Wartości nominalne
    nom_geleon = 17
    nom_sykl = 21
    nom_knut = 1

    # Obliczanie sumy dla każdego rodzaju monety
    suma_geleon = sum(monety.get("geleon", [])) * nom_geleon
    suma_sykl = sum(monety.get("sykl", [])) * nom_sykl
    suma_knut = sum(monety.get("knut", [])) * nom_knut

    # Zamiana na monety o największym nominale
    while suma_geleon >= nom_sykl:
        suma_geleon -= nom_sykl
        suma_sykl += 1

    while suma_sykl >= nom_knut:
        suma_sykl -= nom_knut
        suma_knut += 1

    return {
        "geleon": suma_geleon,
        "sykl": suma_sykl,
        "knut": suma_knut
    }

# Przykładowe wejście
wejscie = {
    "geleon": [1, 3, 5],
    "sykl": [18, 20, 10],
    "knut": [30, 40, 7]
}

# Wyświetlanie wyniku
print(licz_sume(wejscie))

import math

def waluta_str_na_dict(waluta_str: str) -> dict:
    ciag = waluta_str.split(" ")
    
    galeon = 0
    sykl = 0
    knut = 0

    for element_index in range(len(ciag)):
        # Sprawdź czy element to galeon jesli tak to poprzedni element jest wartością galeonu
        if ciag[element_index].startswith("g"):
            galeon = int(ciag[element_index-1])
            continue
        # Sprawdź czy element to sykl jesli tak to poprzedni element jest wartością sykla
        if ciag[element_index].startswith("s"):
            sykl = int(ciag[element_index-1])
            continue
        # Sprawdź czy element to knut jesli tak to poprzedni element jest wartością knuta
        if ciag[element_index].startswith("k"):
            knut = int(ciag[element_index-1])
            continue

    return {"galeon": galeon, "sykl": sykl, "knut": knut}

# Przykład wywołania z samymi knutami
print(waluta_str_na_dict("13 knut"))

# Przykład wywołania z wszystkimi monetami
print(waluta_str_na_dict("17 galeon 2 sykl 13 knut"))

def waluta_dict_na_str(waluta_dict: dict) -> str:
    # Ilość knutów
    knut_raw = waluta_dict["knut"] 
    # Ilość knutów po odjęciu pełnych sykli
    knut = knut_raw % 21
    # Ilość sykli
    sykl_raw = waluta_dict["sykl"] + math.floor(knut_raw/21)
    # Ilość sykli po odjęciu pełnych galeonów
    sykl = sykl_raw % 17
    # Ilość galeonów
    galeon = waluta_dict["galeon"]+math.floor(sykl_raw/17)
    
    response_list = []
    
    # Wypisz galeony jeśli istnieją
    if galeon != 0:
        response_list.append(f"{galeon} galeon")
    # Wypisz sykle jeśli istnieją
    if sykl !=0:
        response_list.append(f"{sykl} sykl")
    # Wypisz knuty jeśli istnieją
    if knut != 0:
        response_list.append(f"{knut} knut")
    # Zamień listę wiadomości na tekst z spacjami
    response = ' '.join(response_list)

    return response


# Przykład wywołania tylko z knutami
print(waluta_dict_na_str({
    "galeon" : 0,
    "sykl" : 0,
    "knut" : 13
}))
# Przykład wywołania z wszystkimi monetami
print(waluta_dict_na_str({
    "galeon" : 17,
    "sykl" : 2,
    "knut" : 13
}))
# Przykład wywołania z wszystkimi monetami i przekształceniem na wyższą monete
print(waluta_dict_na_str({
    "galeon" : 10,
    "sykl" : 20,
    "knut" : 30
}))
>>>>>>> staging
