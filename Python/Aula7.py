import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2.33, 4.1, 1.5, 3.4, 4.5]

#Criar um gráfico de linha
plt.plot(x, y)

#Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

#Adicionar um título ao gráfico
plt.title('Exemplo de Gráfico de Linha')

#Mostrar o gráfico
plt.show()
