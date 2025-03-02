import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)
data = rng.normal(size=1000)

# Гистограмма
plt.hist(data,
         bins=30,  # количество "корзин"
         density=True,  # draw and return a probability density: each bin will display
         # the bin's raw count divided by the total number of counts and the bin width
         alpha=0.5,
         histtype='step',
         edgecolor='red'
         )

# Несколько гистограмм на одной фигуре
x1 = rng.normal(0, 0.8, 1000)
x2 = rng.normal(-2, 1, 1000)
x3 = rng.normal(3, 2, 1000)

# Общие настройки
args = dict(
    alpha=0.3,
    bin=40
)

plt.hist(x1, **args)
plt.hist(x2, **args)
plt.hist(x3, **args)


# Вывод числовых значений
print(np.histogram(x1, bins=1))
print(np.histogram(x2, bins=2))
print(np.histogram(x3, bins=40))


# Двумерные гистограммы
mean = [0, 0]
cov = [[1, 1], [1, 2]]

x, y = rng.multivariate_normal(mean, cov, 10000).T

plt.hist2d(x, y, bins=30)
plt.hexbin(x, y, gridsize=30)
cb = plt.colorbar()
cb.set_label('Point in interval')

print(np.histogram2d(x, y, bins=1))
print(np.histogram2d(x, y, bins=10))


# Легенды
x = np.linspace(1, 10, 1000)

fig, ax = plt.subplots()
# Синусоиды с шагом
y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))

lines = plt.plot(x, y)  # plt.Line2d
plt.legend(lines, ['1', 'второй', 'third', '4-ый'], loc='upper left')
Можно именовать не все линии
plt.legend(lines[:2], ['1', '2'])

ax.plot(x, np.sin(x), label='Синус')
ax.plot(x, np.cos(x), label='Косинус')
ax.plot(x, np.cos(x) + 2)
ax.axis('equal')

# По умолчанию включаются все элементы с лейблом
ax.legend(
    frameon=False,
    fancybox=True,
    shadow=True
)

cities = pd.read_csv('./data/california_cities.csv')

lat, lon, pop, area = cities['latd'], cities['longd'], \
    cities['population_total'], cities['area_total_km2']

plt.scatter(lon, lat, c=np.log10(pop), s=area)  # s - size, c - color (зависимость от указанной величины)
plt.xlabel('Широта')
plt.ylabel('Долгота')
plt.colorbar()
plt.clim(3, 7)  # отображение определенной части colorbar

# Чтобы показать размер в легенде, можно сделать "пустые" графики
plt.scatter([], [], c='k', alpha=0.5, s=100, label='100 $km^2$')
plt.scatter([], [], c='k', alpha=0.5, s=300, label='300 $km^2$')
plt.scatter([], [], c='k', alpha=0.5, s=500, label='500 $km^2$')

plt.legend(labelspacing=3, frameon=False)


# На одном графике несколько легенд
fig, ax = plt.subplots()
lines = []
styles = ['-', '--', '-,', ':']
x = np.linspace(0, 10, 1000)
for i in range(4):
    lines += ax.plot(
        x,
        np.sin(x - i + np.pi / 2),
        styles[i]
    )

ax.axis('equal')
ax.legend(lines[:2], ['line 1', 'line 2'], loc='upper right')

# Для создания новой легенды нужно сделать новый слой
leg = mpl.legend.Legend(ax, lines[1:], ['line 2', 'line 3', 'line 4'], loc='lower left')
ax.add_artist(leg)


# Шкалы

x = np.linspace(0, 10, 1000)
y = np.sin(x) * np.cos(x[:, np.newaxis])

# Карты цветов
# 1 - последовательные
# 2 - дивергентные (два цвета)
# 3 - качественные (смешиваются без чёткого порядка)

# 1
plt.imshow(y, cmap='binary')
plt.imshow(y, cmap='viridis')
plt.colorbar()

# 2
plt.imshow(y, cmap='RdBu')
plt.imshow(y, cmap='PuOr')
plt.colorbar()

# 3
plt.imshow(y, cmap='rainbow')
plt.imshow(y, cmap='jet')

plt.colorbar()


plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(y, cmap='viridis')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(y, cmap=plt.cm.get_cmap('viridis', 6))  # Дискретизация шкалы
plt.colorbar()
plt.clim(-0.25, 0.25)


ax1 = plt.axes()
# Система координат внутри другой
# [нижний угол, левый угол, ширина, высота]
ax2 = plt.axes([0.4, 0.3, 0.2, 0.1])  # соотношение к параметрам всего холста


fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.6, 0.8, 0.4])
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.4])
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))

# Простые сетки
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.plot(np.sin(x + np.pi / 4 * i))

plt.show()
