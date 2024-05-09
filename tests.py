# Test dla task 4

# Task 4 wymaga obliczenia kosztu sowy, dla podanych parametrów:
# - sowa z potwierdzeniem odbioru/ bez potwierdzenia
# - typ sowy w zależności od odległości (lokalna/krajowa/dalekobieżna)
# - list/paczka
# - opcja specjalna (wyjec/list gończy) lub jej brak

from main import wybierz_sowe_zwroc_koszt

test_1 = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')
assert(test_1 == {'knut': 13, 'sykl': 0, 'galeon': 0})


test_2 = wybierz_sowe_zwroc_koszt(False, 'dalekobiezna', 'paczka', 'list gończy')
assert(test_2 == {'knut': 1, 'sykl': 3, 'galeon': 0})


test_3 = wybierz_sowe_zwroc_koszt(False, 'krajowa', 'list', 'wyjec')
assert(test_3 == {'knut': 16, 'sykl': 0, 'galeon': 0})


#test_4 = wybierz_sowe_zwroc_koszt(True, 'krajowa', 'paczka', )
