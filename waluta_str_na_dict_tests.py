import main

assert main.waluta_str_na_dict("13 knut") == {'galeon': 0, 'sykl': 0, 'knut': 13}
assert main.waluta_str_na_dict("5 galeon 13 knut") == {'galeon': 5, 'sykl': 0, 'knut': 13}
assert main.waluta_str_na_dict("5 sykl") == {'galeon': 0, 'sykl': 5, 'knut': 0}