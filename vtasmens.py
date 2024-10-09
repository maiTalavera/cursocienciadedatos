import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
ventas = [100, 150, 200, 250, 300]

plt.bar(meses, ventas)
plt.title('Ventas mensuales')
plt.xlabel('Meses')
plt.ylabel('Ventas')
plt.show()
