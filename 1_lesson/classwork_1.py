import numpy as np
import sys
import array

# Динамическая типизация
# тип переменной меняется в runtime

x = 1
print(type(x))
print(sys.getsizeof(x))

x = 'hello'
print(type(x))

x = True
print(type(x))


l1 = list([])
print(sys.getsizeof(l1))

l2 = list([1, 2, 3])
print(sys.getsizeof(l2))

# Список в Питоне позволяет хранить подобное:
l3 = list([1, "2", True])
# Но минус - низкая скорость обработки
print(l3)

# В массиве - только данные одного типа
a1 = array.array('i', [1, 2, 3])
print(sys.getsizeof(a1))
print(type(a1))


# Но в numpy массивы всё-таки лучше
a = np.array([1, 2, 3, 4, 5])
print(type(a), a)

# Повышающее приведение типов (ниже - приведёт к float)
a = np.array([1.23, 2, 3, 4, 5])
print(type(a), a)

# Можно указать желаемый тип
a = np.array([1.23, 2, 3, 4, 5], dtype=int)
print(type(a), a)

# Многомерные массивы
a = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(type(a), a)

# Создание массивов
a = np.zeros(10, dtype=int)
print(a, type(a))

print(np.ones((3, 5), dtype=float))

print(np.full((4, 5), 3.1415))

print(np.arange(0, 20, 2))

# Единичная матрица
print(np.eye(4))


# Установка начального параметра для генерации случайных чисел
np.random.seed(1)

x1 = np.random.randint(10, size=3)
x2 = np.random.randint(10, size=(3, 2))
x3 = np.random.randint(10, size=(3, 2, 1))
print(x1)
print(x2)
print(x3)

# ndim - размерность, shape - размер размерности, size - общее число элементов
print(x1.ndim, x1.shape, x1.size)
print(x2.ndim, x2.shape, x2.size)
print(x3.ndim, x3.shape, x3.size)


# Доступ к элементам массива
a = np.array([1, 2, 3, 4, 5])
print(a[0])
print(a[-2])

a[1] = 20
print(a)

a = np.array([[1, 2], [3, 4]])
print(a)

print(a[0, 0])
print(a[-1, -1])

a[1, 0] = 100
print(a)


# Тип данных фиксирован после создания массива в numpy
a = np.array([1, 2, 3, 4])
b = np.array([1.0, 2, 3, 4])

print(a)
print(b)

a[0] = 10
print(a)

# Приведётся к изначальному типу массива - int
a[0] = 10.123
print(a)


### Срез - подмассив [start:finish:step]
# По умолчанию [0:shape:1]

a = np.array([1, 2, 3, 4, 5, 6])
print(a[:3])
print(a[3:])
print(a[1:5])
print(a[1:-1])
print(a[1::2])
# Массив в обратном порядке
print(a[::-1])

# Срез - это не копия, скорее ссылка
b = a[:3]
print(b)

b[0] = 100
print(a)  # Поменялось а

a = np.arange(1, 13)
print(a)
# Нужно, чтобы размеры соответствовали
print(a.reshape(2, 6))
print(a.reshape(3, 4))


# Объединение

x = np.array([1, 2, 3])
y = np.array([4, 5])
z = np.array([6])

print(np.concatenate([x, y, z]))


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
# Вертикальное склеивание
r1 = np.vstack([x, y])
print(r1)

# Горизонтальное склеивание
print(np.hstack([r1, r1]))


### Вычисления с массивами
# Векторизированная операция (независимо к каждому элементу массива)
x = np.arange(10)
print(x)
print(x * 2 + 1)

# Универсальные функции (+, *, -, отрицание-, /, //, **, %)
print(np.add(np.multiply(x, 2), 1))

# np.abs, sin/cos/tan, exp, log

x = np.arange(5)
y = np.empty(5)
print(np.multiply(x, 10, out=y))
print(y)

x = np.arange(5)
y = np.zeros(10)
print(np.multiply(x, 10, out=y[::2]))
print(y)


# Свёртка массива
x = np.arange(1, 5)
print(x)

print(np.add.reduce(x))
print(np.add.accumulate(x))


# Векторные произведения
x = np.arange(1, 10)
print(np.add.outer(x, x))
print(np.multiply.outer(x, x))
