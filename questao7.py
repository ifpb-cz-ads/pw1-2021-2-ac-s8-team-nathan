def valida_string(max,min,string):
    x=len(string)
    if x <= max and x >= min:
        print('string valida')
    else:
        print('String invalida')
string='batata'
valida_string(6,2,string)