import time
import random
from datetime import datetime
import csv


def wyslij_sowe(adresat, tresc):
    print(f"Twój list do {adresat} już leci!")
    time.sleep(1)
    if random.uniform(0, 1) <= 0.85:
        return True
    else:
        return False


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
    sorted_dict = {"galeon": waluta_dict["galeon"],
                   "sykl": waluta_dict["sykl"],
                   "knut": waluta_dict["knut"]}

    wynik = []
    for moneta, ilosc in sorted_dict.items():
        if ilosc != 0:
            wynik.append(f"{ilosc} {moneta}")

    return " ".join(wynik)


def waluta_str_na_dict(currency_text: str) -> dict:
    """
    Convert string with currencies to a dictionary.

    :param currency_text: text that contains currency values in format '12 galeon 5 sykl'.
    :return: dict with currencies.
    """
    currency_dict = {}
    texts = currency_text.split(" ")
    for i in range(1, len(texts), 2):
        currency_dict[texts[i]] = texts[i - 1]

    return currency_dict


def nadaj_sowe(adresat: str, tresc: str, potwierdzenie: bool, odleglosc: str, typ: str, specjalna: str):
    """
    Save letter data into csv file.

    :param adresat: receipent.
    :param tresc: content.
    :param potwierdzenie: is confirmation.
    :param odleglosc: distance.
    :param typ: type.
    :param specjalna: special.
    """
    cost = wybierz_sowe_zwroc_koszt(potwierdzenie=potwierdzenie, odleglosc=odleglosc, typ=typ, specjalna=specjalna)
    cost = waluta_dict_na_str(cost)
    confirmation = "TAK" if potwierdzenie else "NIE"
    with open("poczta_nadania_lista.csv", 'a') as file:
        file.write(f"{adresat},{tresc},{cost},{confirmation}\n")


def poczta_wyslij_sowy(csv_path: str):
    """
    Sent letters, recompute the costs. Save results to csv file.

    :param csv_path: path to csv file with letters that should be sent.
    """
    letters = []
    with open(csv_path, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            letters.append(row)

    costs = []
    confirmations = []
    for letter in letters:
        is_delivered = wyslij_sowe(letter[0], letter[1])
        if is_delivered:
            costs.append(letter[2])
            confirmations.append("TAK")
        else:
            # is confirmation
            confirmations.append("NIE")
            if letter[3]:
                costs.append("")
            else:
                costs.append(letter[2])

    today = datetime.today()
    with open(f"output_sowy_z_poczty_{today.month}_{today.year}.csv", "a") as file:
        for i in range(len(letters)):
            file.write(f"{letters[i][0]},{letters[i][1]},{letters[i][2]},{confirmations[i]},{costs[i]}\n")
