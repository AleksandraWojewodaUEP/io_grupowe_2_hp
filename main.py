import time
import random

def wyslij_sowe (adresat, tresc):

    print(f"Wysyłanie sowy do: {adresat}, o treści: {tresc}")
    time.sleep(1)

    if random.random()<0.85:
        print("Sowa została wysłana pomyślnie!")
        return True
    else:
        print("Niestety wystąpił błąd podczas wysyłania sowy")
        return False
    

def licz_sume(fundusz):
    # Przeliczenie knutów na sykle
    knuty = sum(fundusz.get("knut"))
    knut_sykl = knuty // 21
    knuty = knuty % 21

    # Dodanie knutów do sykli i przeliczenie sykli na galeony 
    sykle = sum(fundusz.get("sykl")) + knut_sykl
    sykl_galeon = sykle // 17
    sykle = sykle % 17

    # Dodanie sykli do galeonów
    galeony = sum(fundusz.get("galeon")) + sykl_galeon

    return {
        "galeon": galeony,
        "sykl": sykle,
        "knut": knuty
    }


def wybierz_sowe_zwroc_koszt(potw_odbioru, odleglosc, typ, specjalna):

    koszt_dict = {'galeon': 0, 'sykl': 0, 'knut': 0}

    if typ == 'list':
        if odleglosc == 'lokalna':
            koszt_dict['knut'] = 2
        elif odleglosc == 'krajowa':
            koszt_dict['knut'] = 12
        elif odleglosc == 'dalekobieżna':
            koszt_dict['knut'] = 20

    elif typ == 'paczka':
        if odleglosc == 'lokalna':
            koszt_dict['knut'] = 7
        elif odleglosc == 'krajowa':
            koszt_dict['knut'] = 2
            koszt_dict['sykl'] = 1
        elif odleglosc == 'dalekobieżna':
            koszt_dict['knut'] = 1
            koszt_dict['sykl'] = 2

    if potw_odbioru:
        koszt_dict['knut'] = koszt_dict.get('knut') + 7

    if specjalna == 'wyjec':
        koszt_dict['knut'] = koszt_dict.get('knut') + 4
    elif specjalna == 'list gończy':
        koszt_dict['sykl'] = koszt_dict.get('sykl') + 1

    return koszt_dict


def waluta_dict_na_str(fundusz):
    for k, v in fundusz.items():
        if k in fundusz and v != 0:
            fundusz[k] = v
    cena = ""

    if fundusz['galeon'] != 0:
        cena += str(fundusz['galeon']) + ' galeon '
    if fundusz['sykl'] != 0:
        cena += str(fundusz['sykl']) + ' sykl '
    if fundusz['knut'] != 0:
        cena += str(fundusz['knut']) + ' knut'

    return cena


def waluta_str_na_dict(waluta_str):
    
    elements = waluta_str.split()
    
   
    currency_dict = {'galeony': 0, 'sykle': 0, 'knuty': 0}
    
    
    for i in range(0, len(elements), 2):
        value = int(elements[i])  
        unit = elements[i + 1]    
        
        if unit.startswith('g'):
            currency_dict['galeony'] = value
        elif unit.startswith('s'):
            currency_dict['sykle'] = value
        elif unit.startswith('k'):
            currency_dict['knuty'] = value
    
    return currency_dict






