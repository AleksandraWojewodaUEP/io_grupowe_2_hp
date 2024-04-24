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

input_str = "10 galeon 5 sykl 0 knut"
result = waluta_str_na_dict(input_str)
print(result)
