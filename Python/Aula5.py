import random
def busca(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return valor
    return -1

lista = random.sample(range(70), 50)
print(sorted(lista))

print(f"\n{busca(lista,41)}")
print(busca(lista,55))
print(busca(lista,lista,random.randint(1, 70)))
