from main import waluta_dict_na_str, waluta_str_na_dict

# Task 5

currencies1 = {
    "knut": 13,
    "galeon": 0,
    "sykl": 0,
}

currencies2 = {
    "sykl": 2,
    "galeon": 13,
    "knut": 13
}

assert (waluta_dict_na_str(currencies1) == "13 knut")
assert (waluta_dict_na_str(currencies2) == "13 galeon 2 sykl 13 knut")

# Task 6
assert (waluta_str_na_dict("13 knut") == {'knut': '13'})
assert (waluta_str_na_dict("22 galeon 15 sykl 4 knut") == {'galeon': '22', 'sykl': '15', 'knut': '4'})
