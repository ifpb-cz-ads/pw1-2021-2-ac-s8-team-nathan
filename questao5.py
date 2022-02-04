from collections import namedtuple


def enumerate(lista):
    indice=0
    Lista = namedtuple('Lista', ['indice','valor'])
    for x in lista:
       lista1 = list(Lista(indice,x))
       print(lista1)
       indice+=1
    return lista1

lista=['bataba','Goiaba','Jujuba','Batom','Macaxeira']

enumerate(lista)

