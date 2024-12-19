from main import waluta_dict_na_str


# test 1 
assert waluta_dict_na_str({'galeon':1, 'sykl': 2, 'knut': 3}) == '1 galeon 2 sykl 3 knut' 
# test 2
assert waluta_dict_na_str({'galeon':4, 'sykl': 8, 'knut': 1}) == '4 galeon 8 sykl 1 knut'
# test 3 
assert waluta_dict_na_str({'galeon':2, 'sykl': 6, 'knut': 9}) == '2 galeon 6 sykl 9 knut'
# test 4 
assert waluta_dict_na_str({'galeon':8, 'sykl': 1, 'knut': 8}) == '8 galeon 1 sykl 8 knut'

