import numpy as np
import sys
import array

## 1. Какие еще существуют коды типов?

#         'b': signed char
#         'B': unsigned char
#         'u': Py_UNICODE
#         'h': signed short
#         'H': unsigned short
#         'i': signed int
#         'I': unsigned int
#         'l': signed long
#         'L': unsigned long
#         'q': signed long long
#         'Q': unsigned long long
#         'f': float
#         'd': double

## 2. Напишите код, подобный приведенному выше, но с другим типом

arr = array.array('f', [1.1, 2.2, 3.3])
print(sys.getsizeof(arr))
print(type(arr))

## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1

lin_arr = np.linspace(0, 1, 5)
print(lin_arr)

## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

np.random.seed(3)
rand_arr = np.random.rand(5)
print(rand_arr)

## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и
#    дисперсией 1

norm_arr = np.random.normal(0, 1, 5)
print(norm_arr)

## 6. Напишите код для создания массива с 5 случайными целыми числами в от [0, 10)

randint_arr = np.random.randint(0, 10, size=5)
print(randint_arr)

## 7. Написать код для создания срезов массива 3 на 4

matrix = np.random.randint(10, size=(3, 4))
print(matrix)

# - первые две строки и три столбца
print(matrix[:2, :3])

# - первые три строки и второй столбец
print(matrix[:, 1:2])

# - все строки и столбцы в обратном порядке
print(matrix[::-1, ::-1])

# - второй столбец
print(matrix[:, 1])

# - третья строка
print(matrix[2])


## 8. Продемонстрируйте, как сделать срез-копию

slice_arr = matrix[:, 2]
slice_copy = slice_arr.copy()

print(matrix[:, 2])  # одинаковые
print(slice_copy)

# Изменим значение в копии для демонстрации
slice_copy[0] = 100

print(matrix[:, 2])  # не изменилось
print(slice_copy)  # изменилось


## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

array = np.array([1, 2, 3, 4, 5])

# Преобразование в вектор-строку
vector_row = array[np.newaxis, :]

# Преобразование в вектор-столбец
vector_column = array[:, np.newaxis]

print(array, array.shape)
print(vector_row, vector_row.shape)
print(vector_column, vector_column.shape)


## 10. Разберитесь, как работает метод dstack
#       Метод dstack используется для объединения массивов вдоль третьей оси

# Создаем два двумерных массива одинаковой формы
array1 = np.array([[1, 2],
                   [3, 4]])

array2 = np.array([[5, 6],
                   [7, 8]])

# Объединяем
result = np.dstack((array1, array2))
print(result)


## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

# Функция np.split используется для разбиения массива вдоль заданной оси на подмассивы одинакового размера.
x = np.arange(9.0)
print(np.array_split(x, 3))  # по умолчанию axis = 0

# Функция np.vsplit предназначена для разбивания двумерных массивов вдоль вертикальной оси.
arr11 = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(np.vsplit(arr11, 2))  # второй параметр - количество секций среза

# Функция np.hsplit используется для разбиения массивов вдоль горизонтальной оси
print(np.hsplit(arr11, 2))

# Функция np.dsplit применяется для разбиения трехмерных массивов по третьему измерению.
# Работает только на трёх- и более мерных массивах
arr_11 = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print(np.dsplit(arr_11, 2))


## 12. Привести пример использования всех универсальных функций, которые я привел

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
# -
print(np.subtract(a, b))
# /
print(np.divide(a, b))
# //
print(np.floor_divide(a, b))
# **
print(np.power(a, b))
# %
print(np.mod(a, b))
# -
print(np.negative(a))