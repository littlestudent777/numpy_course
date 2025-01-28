import numpy as np
import pandas as pd

# Pandas - расширение NumPy (структурированные массивы).
# Строки и столбцы индексируются метками (разных типов), а не только числовыми значениями

# Основные структуры: Series, DataFrame, Index

## Series

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print(type(data))

print(data.values)
print(type(data.values))
print(data.index)
print(type(data.index))

print(data[0])
print(data[1:3])

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)
print(data['a'])
print(data['b':'d'])

print(type(data.index))

# Можно и так - индексы разного типа
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 10, 7, 'd'])
print(data)
print(data[1])
print(data[10:'d'])

population_dict = {
    'city_1': 1001,
    'city_2': 1002,
    'city_3': 1003,
    'city_4': 1004,
    'city_5': 1005
}

# Индексы берутся из ключей, значения - из значений словаря
population = pd.Series(population_dict)
print(population)
print(population['city_4'])
print(population['city_4':'city_5'])

# Для создания Series можно использовать
# - списки python или массивы numpy
# - скалярные значения
# - словари

## DataFrame - двумерный массив с явно определёнными индексами
# или последовательность согласованных (по индексам) Series

population_dict = {
    'city_1': 1001,
    'city_2': 1002,
    'city_3': 1003,
    'city_4': 1004,
    'city_5': 1005
}

area_dict = {
    'city_1': 9991,
    'city_2': 9992,
    'city_3': 9993,
    'city_4': 9994,
    'city_5': 9995
}

population = pd.Series(population_dict)
area = pd.Series(area_dict)

print(population)
print(area)

states = pd.DataFrame({
    'population': population,
    'area': area
})

print(states)

print(states.values)
print(states.index)
print(states.columns)

print(type(states.values))
print(type(states.index))
print(type(states.columns))

print(states['area1'])

# DataFrame. Способы создания
# - через объекты Series
# - списки словарей
# - словари объектов Series
# - двумерный массив NumPy
# - структурированный массив NumPy


# Index - способ организации ссылки на данные объектов Series, DataFrame
# Index - неизменяем (кортеж), упорядочен (не лексикографически), является мультимножеством
# (в нём могут быть повторяющиеся значения)

ind = pd.Index([2, 3, 5, 7, 11])
print(ind[1])
print(ind[::2])

# ind[1] = 5 - нельзя!

# Index - следует соглашениям объекта set (python)

indA = pd.Index([1, 2, 3, 4, 5])
indB = pd.Index([2, 3, 4, 5, 6])
# возвращается новый индекс
print(indA.intersection(indB))


# Выборка данных из Series
# как словарь
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

# проверка наличия индекса
print('a' in data)
print('z' in data)

# получить индекс
print(data.keys())

# получить список
print(list(data.items()))

data['a'] = 100
data['z'] = 1000  # добавляется значение
print(data)

# как одномерный массив

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

print(data['a':'c'])
print(data[0:2])  # это также работает
print(data[(data > 0.5) & (data < 1)])
print(data[['a', 'd']])

# атрибуты - индексаторы
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 'b', 'c', 'd'])

print(data[1])  # путаница в индексах

print(data.loc[1])  # обращение к значению индекса
print(data.iloc[1])  # обращение к номеру


# Выборка данных из DataFrame
# как словарь
pop = pd.Series(
    {
        'city_1': 1001,
        'city_2': 1002,
        'city_3': 1003,
        'city_4': 1004,
        'city_5': 1005
    }
)

area = pd.Series(
    {
        'city_1': 9991,
        'city_2': 9992,
        'city_3': 9993,
        'city_4': 9994,
        'city_5': 9995
    }
)

data = pd.DataFrame({'area1': area, 'pop1': pop, 'pop': pop})
print(data)
print(data['area1'])
print(data.area1)

print(data.pop1 is data['pop1'])
print(data.pop is data['pop'])  # conflict

# увеличиваем размерность
data['new'] = data['area1']
print(data)

data['new1'] = data['area1'] / data['pop1']

# также может вести себя как двумерный массив numpy
data = pd.DataFrame({'area1': area, 'pop1': pop})
print(data)
print(data.values)

print(data.T)
# работа со столбцами
print(data['area1'])
# чтобы получить строку, переходим в numpy
print(data.values[0])

# атрибуты-индексаторы
data = pd.DataFrame({'area1': area, 'pop1': pop, 'pop': pop})
print(data)
print(data.iloc[:3, 1:2])
print(data.loc[:'city_3', 'pop1': 'pop'])
print(data.loc[data['pop'] > 1002, ['area1', 'pop']])

# присваивание значения
data.iloc[0, 2] = 99999
print(data)

# универсальные функции
rng = np.random.default_rng()
s = pd.Series(rng.integers(0, 10, 4))
print(s)
print(np.exp(s))

# не все элементы совпадают
pop = pd.Series(
    {
        'city_1': 1001,
        'city_2': 1002,
        'city_3': 1003,
        'city_41': 1004,
        'city_51': 1005
    }
)

area = pd.Series(
    {
        'city_1': 9991,
        'city_2': 9992,
        'city_3': 9993,
        'city_42': 9994,
        'city_52': 9995
    }
)

# происходит объединение индексов (недостающее заполняется Nan)
data = pd.DataFrame({'area1': area, 'pop1': pop})

dfA = pd.DataFrame(rng.integers(0, 10, (2, 2)), columns=['a', 'b'])
dfB = pd.DataFrame(rng.integers(0, 10, (3, 3)), columns=['a', 'b', 'c'])

print(dfA)
print(dfB)
print(dfA + dfB)

rng = np.random.default_rng(1)

A = rng.integers(0, 10, (3, 4))
print(A)
print(A[0])
print(A - A[0])  # транслирование

df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print(df)
print(df.iloc[0])
print(df - df.iloc[0])
print(df.iloc[0, ::2])

print(df - df.iloc[0, ::2])  # согласование индексов


# NA - значения: NaN, null, -99999

# Pandas. Два способа хранения отсутствующих значений
# - индикаторы NaN, None
# - null

# None - объект (накладные расходы). Не работает с sum, min и проч

# val1 = np.array([1, None, 2, 3])
# print(val1.sum())

val1 = np.array([1, 2, 3])
print(val1.sum())

# числовой nan
val1 = np.array([1, np.nan, 2, 3])
print(val1)
print(val1.sum())
print(np.nansum(val1))

x = pd.Series(range(10), dtype=int)
print(x)

x[0] = None
x[1] = np.nan
print(x)

x1 = pd.Series(['a', 'b', 'c'])
print(x1)
# объекты, булевы значения ведут себя по разному при такой замене
x1[0] = None
x1[1] = np.nan
print(x1)

x2 = pd.Series([1, 2, 3, np.nan, None, pd.NA])
print(x2)

x3 = pd.Series([1, 2, 3, np.nan, None, pd.NA], dtype='Int32')
print(x3)

print(x3.isnull())
print(x3[x3.isnull()])
print(x3[x3.notnull()])

print(x3.dropna())

df = pd.DataFrame([
    [1, 2, 3, np.nan, None, pd.NA],
    [1, 2, 3, 4, 5, 6],
    [1, np.nan, 3, 4, np.nan, 6]
])

print(df)
print(df.dropna())  # останется только вторая строка
# можно выбрать размерность, по которой работает (по умолч. 0)
print(df.dropna(axis=0))
print(df.dropna(axis=1))

# how
# - all - все значения NA
# - any - хотя бы одно значение
# - thresh - x, остаётся, если присутствует минимум x непустых значений

df = pd.DataFrame([
    [1, 2, 3, np.nan, None, pd.NA],
    [1, 2, 3, None, 5, 6],
    [1, np.nan, 3, None, np.nan, 6]
])
print(df.dropna(axis=1, how='all'))
print(df.dropna(axis=1, how='any'))
print(df.dropna(axis=1, thresh=2))
