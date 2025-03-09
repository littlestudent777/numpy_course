import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# # Трёхмерные точки и линии
# fig = plt.figure()
# ax = plt.axes(projection='3d')

# z1 = np.linspace(0, 15, 1000)
# y1 = np.cos(z1)
# x1 = np.sin(z1)
#
# #ax.plot3D(x1, y1, z1, 'green')
#
# z2 = 15 * np.random.random(100)
# y2 = np.cos(z2) + 0.1 * np.random.random(100)
# x2 = np.sin(z2) + 0.1 * np.random.random(100)

#ax.scatter3D(x2, y2, z2, c=z2, cmap='Greens')

# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))

# x = np.linspace(-6, 6, 30)
# y = np.linspace(-6, 6, 30)
# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# ax.contour3D(X, Y, Z, 40, cmap='binary')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
#
# # Указываем положение "камеры"
# ax.view_init(60, 45)


# # Каркасные графики
# ax.plot_wireframe(X, Y, Z)

# # Поверхностые графики
# ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
# ax.set_title('Example')


# # Можно построить срез поверхности
# r = np.linspace(0, 6, 20)
# # в полярных координатах - не "довели до конца значения"
# theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
#
# R, Theta = np.meshgrid(r, theta)
#
# X = r * np.sin(Theta)
# Y = r * np.cos(Theta)
# Z = f(X, Y)
#
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')


# # Триангуляция поверхности
# theta = 2 * np.pi + np.random.random(1000)
# r = 6 * np.random.random(1000)
#
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# z = f(x, y)
#
# ax.scatter3D(x, y, z, c=z, cmap='viridis')
#
# ax.plot_trisurf(x, y, z, cmap='viridis')
#


# Seaborn
# - работает с df (mpl - с pd)
# - имеет более высокоуровневый интерфейс

# data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
# data = pd.DataFrame(data, columns=['x', 'y'])
#
# print(data.head())
#
# # На mpl
# fig = plt.figure()
# plt.hist(data['x'], alpha=0.5)
# plt.hist(data['y'], alpha=0.5)
#
# # На sns
# fig = plt.figure()
# sns.kdeplot(data=data, shade=True)


# iris = sns.load_dataset('iris')
# print(iris.head())
#
# sns.pairplot(iris, hue='species', height=2.5)

# # гистограммы
# grid = sns.FacetGrid(tips, row='sex', col='day', hue='time')
# grid.map(plt.hist, "total_bill", bins=np.linspace(0, 40, 15))


#sns.catplot(data='tips', x='day', y='total_bill', kind='box')


# # совместное распределение
# sns.jointplot(data=tips, x='tip', y='total_bill', kind='hex')


## графики временных рядов
# planets = sns.load_dataset('planets')
# print(planets.head())
#
# sns.catplot(data=planets, x='year', kind='count', hue='method', order=range(2005, 2015))


# Категориальные данные
tips = sns.load_dataset('tips')
print(tips.head())

# # Сравнение числовых данных
# # Числовые пары
# sns.pairplot(tips)

# # Тепловая карта
# tips_corr = tips[['total_bill', 'tip', 'size']]
# sns.heatmap(tips_corr.corr(), cmap='RdBu_r', annot=True, vmin=-1, vmax=1)
# # 0 - независимы
# # 1 - положительная
# # -1 - отрицательная
#
# # Диаграмма рассеяния
# sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex')
#
# # Линейная регрессия
# sns.regplot(data=tips, x='total_bill', y='tip')
#
# sns.relplot(data=tips, x='total_bill', y='tip', hue='sex')

# # Линейный график
# sns.lineplot(data=tips, x='total_bill', y='tip')

# # Сводная диаграмма
# sns.jointplot(data=tips, x='total_bill', y='tip')


# # Сравнение числовых и категориальных данных
# # Гистограмма
# sns.barplot(data=tips, y='total_bill', x='day', hue='sex')

# sns.pointplot(data=tips, y='total_bill', x='day', hue='sex')


# # Ящик с усами
# sns.boxplot(data=tips, y='total_bill', x='day')


# # Скрипичная диаграмма
# sns.violinplot(data=tips, y='total_bill', x='day')


# Одномерная диаграмма рассеяния
sns.stripplot(data=tips, y='total_bill', x='day')

plt.show()
