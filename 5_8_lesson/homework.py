import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

fig1, ax1 = plt.subplots()
x1 = [0, 5, 10, 15.5, 20]
# Данные для первой ломаной
y1_1 = [0, 7.5, 3.5, 5, 11]
# Данные для второй ломаной
y1_2 = [4, 3, 0, 8, 12]

plt.plot(x1, y1_1, marker='o', linestyle='-', color='red', label='line 1')
plt.plot(x1, y1_2, marker='o', linestyle='-.', color='green', label='line 2')
plt.legend()


fig2 = plt.figure(figsize=(10, 8))
grid2 = fig2.add_gridspec(2, 2, height_ratios=[2, 1])
x2 = np.linspace(1.0, 5.0, 5)

ax2_1 = fig2.add_subplot(grid2[0, :])
y2_1 = [0, 7, 6, 4, 5]
ax2_1.plot(x2, y2_1, color='blue')

ax2_2 = fig2.add_subplot(grid2[1, 0])
y2_2 = [9, 4, 2, 4, 9]
ax2_2.plot(x2, y2_2, color='blue')

ax2_3 = fig2.add_subplot(grid2[1, 1])
y2_3 = [-7, -4, 2, -4, -7]
ax2_3.plot(x2, y2_3, color='blue')

plt.tight_layout()


fig3, ax3 = plt.subplots()
x3 = np.linspace(-5, 5, 50)
ax3.plot(x3, x3 * x3, color='blue')
ax3.annotate('min', xy=(0, 0), xytext=(-0.3, 10), arrowprops=dict(arrowstyle='->', edgecolor='g'))


fig4, ax4 = plt.subplots()
# Создаем случайные данные для тепловой карты
data4 = np.random.rand(7, 7) * 10

plt.imshow(data4, cmap='viridis', origin='lower', extent=[0, 7, 0, 7])
plt.colorbar()


fig5, ax5 = plt.subplots()
x5 = np.linspace(0, 5, 1000)
y5 = np.cos(np.pi * x5)  # Период равен 2

# Закрашиваем область под кривой
plt.fill_between(x5, y5, color='blue', alpha=0.6)

# Отрисовываем контур
plt.plot(x5, y5, color='red')


fig6, ax6 = plt.subplots()
x6 = np.linspace(0, 5, 1000)
y6 = np.cos(np.pi * x6)
y_limit = -0.5

# Маскируем значения, которые ниже порога
y_masked = np.where(y6 >= y_limit, y6, np.nan)  # Заменяем значения ниже порога на Nan

plt.plot(x6, y_masked, color='blue', alpha=0.6, linewidth=3)
plt.ylim(-1, 1)


fig7, axes7 = plt.subplots(1, 3, figsize=(12, 4))
x7 = np.arange(7)
y7 = np.arange(7)

styles = ['pre', 'mid', 'post']

for ax, style in zip(axes7, styles):
    ax.step(x7, y7, where=style, color='green', marker='o')
    ax.grid(True)


fig8, ax8 = plt.subplots()
x8 = np.linspace(0, 10, 500)

y8_1 = -0.4 * (x8 - 5)**2 + 10
y8_2 = -0.2 * (x8 - 5)**2 + 5
y8_3 = -(x8 - 5)**2 + 25

plt.fill_between(x8, y8_3, color='lightgreen', label='y3', zorder=1)
plt.plot(x8, y8_3, color='green', linewidth=2, zorder=2)

plt.fill_between(x8, y8_1, color='lightblue', label='y1', zorder=3)
plt.plot(x8, y8_1, color='blue', linewidth=2, zorder=4)

plt.fill_between(x8, y8_2, color='lightcoral', label='y2', zorder=5)
plt.plot(x8, y8_2, color='red', linewidth=2, zorder=6)

plt.legend()


fig9, ax9 = plt.subplots()
car_brands = ['Toyota', 'Ford', 'Jaguar', 'AUDI', 'BMW']
counts = [10, 15, 22.5, 12.5, 40]
# Параметр explode: задаем смещение
explode = [0, 0, 0, 0, 0.1]

plt.pie(counts, labels=car_brands, explode=explode)


fig10, ax10 = plt.subplots()
plt.pie(counts, labels=car_brands, pctdistance=0.85)
centre_circle = plt.Circle((0, 0), 0.5, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)


plt.show()
