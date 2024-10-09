import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [1, 4, 9, 16, 25]

# Crear dos subgráficos
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Gráfico 1')

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Gráfico 2')

# Mostrar gráficos
plt.show()
