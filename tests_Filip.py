from main import waluta_str_na_dict
from main import wyslij_sowe

#Test 1 simple
assert waluta_str_na_dict('1 galeon 2 sykl 3 knut') == {'galeony': 1, 'sykle': 2, 'knuty': 3}
#Test 2 without knut
assert waluta_str_na_dict('1 galeon 2 sykl') == {'galeony': 1, 'sykle': 2, 'knuty': 0}
#Test 3 without sykl
assert waluta_str_na_dict('1 galeon 3 knut') == {'galeony': 1, 'sykle': 0, 'knuty': 3}
#Test 4 without galeon
assert waluta_str_na_dict('2 sykl 3 knut') == {'galeony': 0, 'sykle': 2, 'knuty': 3}
#Test 5 without galeon and sykl
assert waluta_str_na_dict('3 knut') == {'galeony': 0, 'sykle': 0, 'knuty': 3}
#Test 6 without galeon and knut
assert waluta_str_na_dict('2 sykl') == {'galeony': 0, 'sykle': 2, 'knuty': 0}
#Test 7 without sykl and knut
assert waluta_str_na_dict('1 galeon') == {'galeony': 1, 'sykle': 0, 'knuty': 0}
#Test 8 empty
assert waluta_str_na_dict('') == {'galeony': 0, 'sykle': 0, 'knuty': 0}

