import random

def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1
    while minimo <= maximo:
         meio = (minimo + maximo) // 2 
         if valor < lista[meio]:
              maximo = meio - 1 
         elif valor > lista[meio]:
              minimo = meio + 1
         else:
              return True
    return False

lista = random.sample(range(999), 250)
lista = (sorted(lista))
print(lista,'\n')

print (f"\n{executar_busca_binaria(lista,501)}")
print(executar_busca_binaria(lista,637))
p=random.randint(1, 999)
print(executar_busca_binaria(lista,p),'\n',p)
