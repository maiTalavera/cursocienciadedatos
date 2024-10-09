import matplotlib.pyplot as plt

# Datos
alturas = [1.60, 1.65, 1.70, 1.75, 1.80]
pesos = [60, 65, 70, 75, 80]

plt.scatter(alturas, pesos)
plt.title('Relación Altura vs Peso')
plt.xlabel('Altura (m)')
plt.ylabel('Peso (kg)')
plt.show()
