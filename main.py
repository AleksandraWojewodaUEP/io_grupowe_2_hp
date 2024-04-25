import time
import random

def wyslij_sowe(adresat, tresc):
    print(f"Twój list do {adresat} już leci!")
    time.sleep(1)
    if random.uniform(0,1) <= 0.85:
        return True
    else:
        return False

# print(wyslij_sowe("Hagrid", "Wpadamy na herabtkę"))

def licz_sume(dane):
  
    if 'galeon' not in dane or 'sykl' not in dane or 'knut' not in dane:
        return "Brak wymaganych danych"

    ilosc_galeon = list(dane.get('galeon', 0))
    ilosc_sykl = list(dane.get('sykl', 0))
    ilosc_knut = list(dane.get('knut', 0))
    suma_knut = 0

    max_length = max(len(ilosc_galeon), len(ilosc_sykl), len(ilosc_knut))
    ilosc_galeon.extend([0] * (max_length - len(ilosc_galeon)))
    ilosc_sykl.extend([0] * (max_length - len(ilosc_sykl)))
    ilosc_knut.extend([0] * (max_length - len(ilosc_knut)))

    for i in range(len(ilosc_galeon)):
        suma_knut += (ilosc_galeon[i] * 17 * 21 + ilosc_sykl[i] * 21 + ilosc_knut[i])

    suma_galeon = suma_knut // (17 * 21)
    suma_knut %= (17 * 21)
    suma_sykl = suma_knut // 21
    suma_knut %= 21

    return {'galeon': suma_galeon, 'sykl': suma_sykl, 'knut': suma_knut}

def wybierz_sowe_zwroc_koszt(potwierdzenie: bool, odleglosc: str, typ: str, specjalna: str):
    """
    Obliczanie kosztu wysłania sowy.

    :param potwierdzenie: True/False.
    :param odleglosc: lokalna, krajowa, dalekobiezna.
    :param typ: list, paczka.
    :param specjalna: wyjec, list gończy.
    :return: koszt wysłania wybranej sowy.
    """

    koszty = {
        "list": {
            "lokalna": {"knut": 2},
            "krajowa": {"knut": 12},
            "dalekobiezna": {"knut": 20},
        },
        "paczka": {
            "lokalna": {"knut": 7},
            "krajowa": {"sykl": 1, "knut": 2},
            "dalekobiezna": {"sykl": 2, "knut": 1},
        },
        "specjalna": {
            "wyjec": {"knut": 4},
            "list gończy": {"sykl": 1},
        },
        "potwierdzenie": {
            "knut": 7,
        }
    }

    koszt = {"knut": 0, "sykl": 0, "galeon": 0}
    def dodaj_koszty(cennik):
        for waluta, cena in cennik.items():
            koszt[waluta] += cena
    try:
        if potwierdzenie:
            dodaj_koszty(koszty["potwierdzenie"])
        dodaj_koszty(koszty[typ][odleglosc])
        dodaj_koszty(koszty["specjalna"][specjalna])
    except KeyError:
        raise Exception("Podaj prawidłowe dane.")

    return koszt

def waluta_dict_na_str(waluta_dict):
    wynik = []
    for moneta, ilosc in waluta_dict.items():
        if ilosc != 0:
            wynik.append(f"{ilosc} {moneta}")

    return " ".join(wynik)


przyklad1 = {
    "galeon" : 0,
    "sykl" : 0,
    "knut" : 13
}

przyklad2 = {
    "galeon" : 13,
    "sykl" : 2,
    "knut" : 13
}

