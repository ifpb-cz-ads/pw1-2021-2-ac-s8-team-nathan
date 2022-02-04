def compara_string(lista,string):
    for x in lista:
        if x == string:
            print('Elemento Achado')
            return True
    print('Elemento nao encontrado')
    return False
lista=['a','b','c','d']
string='d'
compara_string(lista,string)