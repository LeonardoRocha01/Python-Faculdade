#Atividade Python

texto = """A inserção de comentários no código do programa é uma prática normal.
Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas.
O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado (BANIN, 2018)."""

caracteres_procurados = {'ó', 'ã'}

for index, char in enumerate(texto):
    if char in caracteres_procurados:
        print(f"Caractere '{char}' encontrado na posição {index}")
