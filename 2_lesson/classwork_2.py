import numpy as np
import matplotlib.pyplot as plt

# Суммирование значений в массиве, агрегатные функции

rng = np.random.default_rng(1)
s = rng.random(50)

print(s)
print(sum(s))
# numpy считает быстрее на больших объёмах + умеет считать многомерные массивы
print(np.sum(s))

a = np.array([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

print(np.sum(a))
# axis задаёт измерение, которое будет свёрнуто
print(np.sum(a, axis=0))
print(np.sum(a, axis=1))

print(np.min(a))
print(np.min(a, axis=0))
print(np.min(a, axis=1))
# или так
print(a.min())
print(a.min(0))
print(a.min(1))

# безопасная функция (если есть вероятность, что в массиве присутствует Nan)
print(np.nanmin(a))
print(np.nanmin(a, axis=0))
print(np.nanmin(a, axis=1))


# Транслирование (broadcasting)
# набор правил, которые позволяют осуществлять бинарные операции с массивами разных форм и размеров

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])

print(a + b)  # [5, 6, 7]
print(a + 5)  # складывается два массива, "5" транслируется в х5, 5, 5ъ
# подстраивается под размер массива а

a = np.array([0, 1, 2], [3, 4, 5])
print(a + 5)

# может быть ситуация, когда оба массива транслируются
a = np.array([0, 1, 2])
b = np.array([[0], [1], [2]])

# Правила
# 1. Если размерности массива отличаются, то форма массива с меньшей размерностью дополняется 1 с левой стороны
# 2. Если формы массивов не совпадают в каком-то измерении, то если у массива форма равна 1, то он растягивается
#    до соответствия формы второго массива
# 3. Если в каком-либо измерении размеры отличаются и ни один из них не равен 1, то генерируется ошибка

# c = np.array([0, 1, 2], [3, 4, 5])
# d = np.array([5])

# print(c.ndim, a.shape)
# print(d.ndim, b.shape)
# d будет дополнено 1 с левой стороны (1,) -> (1, 1) -> (2, 3)

c = np.ones((2, 3))
d = np.arange(3)

print(c)
print(d)

print(c.ndim, c.shape)
print(d.ndim, d.shape)

# (2, 3)  (2, 3)    (2, 3)
# (3,) -> (1, 3) -> (2, 3)

f = c + d
print(f, f.shape)


a = np.arange(2).reshape((3, 1))
b = np.arange(3)

print(a)
print(b)

print(a.ndim, a.shape)
print(b.ndim, b.shape)

# (3, 1)   (3, 1) -> (3, 3)
# (3, ) -> (1, 3) -> (3, 3)

c = a + b

# [0, 0, 0]    [0, 1, 2]
# [1, 1, 1] +  [0, 1, 2]
# [2, 2, 2]    [0, 1, 2]

# Когда не работает
a = np.ones((3, 2))
b = np.arange(3)

# 2 (3, 2)   (3, 2)    (3, 2)
# 1 (3, ) -> (1, 3) -> (3, 3)
# ошибка
c = a + b


X = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
])
# Мат ожидание
Xmean0 = X.mean(0)
print(Xmean0)
Xcenter0 = X - Xmean0
print(Xcenter0)

Xmean1 = X.mean(1)
print(Xmean1)
# транспонируем
Xmean1 = Xmean1[:, np.newaxis]
Xcenter1 = X - Xmean1
print(Xcenter1)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x)**3 + np.cos(20 + y * x) * np.sin(y)
print(z.shape)  # (50, 50)
# тепловая карта
plt.imshow(z)
plt.colorbar()
plt.show()

# Проверка условия в массиве (получаем массив булевских значений)
x = np.array([1, 2, 3, 4, 5])
y = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(x < 3)
print(np.less(x, 3))

# False = 0
# True = 1

# Число элементов, соответствующих условию
print(np.sum(x < 3))
# Можно выбрать ось для анализа
print(np.sum(y < 4, axis=0))
print(np.sum(y < 4, axis=1))
print(np.sum(y < 4))


# Маски - булевы массивы
x = np.array([1, 2, 3, 4, 5])
print(x[x < 3])

print(bin(42))
print(bin(59))
print(bin(42 & 59))


# Векторизация индекса

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
index = [1, 5, 7]

print(x[index])

# структура в соответствие с индексом, а не изначальным массивом
index = [[1, 5, 7], [2, 4, 8]]
print(x[index])

x = np.arange(12).reshape((3, 4))
print(x)
print(x[2])
print(x[2, [2, 0, 1]])
print(x[1:, [2, 0, 1]])

x = np.arange(10)
i = np.array([2, 1, 8, 4])
print(x)
x[i] = 999
print(x)


# Сортировка
x = [3, 2, 3, 5, 7, 6, 8, 9]
print(sorted(x))
# Работает быстрее на больших объёмах, работает на разных размерностях
print(np.sort(x))


# Структурированные массивы
data = np.zeros(4, dtype={
    'names': (
        'name', 'age'
    ),
    'formats': (
        'U10', 'i4'
    )
})

print(data.dtype)

name = ['name1', 'name2', 'name3', 'name4']
age = [10, 20, 30, 40]

data['name'] = name
data['age'] = age

print(data)
print(data['age'] > 20)
print(data[data['age'] > 20]['name'])


# Массивы записей
data_rec = data.view(np.recarray)
print(data_rec)
# тут можно обращаться по индексам
print(data_rec[0])
print(data_rec[-1].name)
