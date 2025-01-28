import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
array = [1, 2, 3, 4]
series_from_array = pd.Series(array)
print(series_from_array)

np_array = np.array([1, 2, 3, 4])
series_from_np_array = pd.Series(np_array)
print(series_from_np_array)

# - скалярные значения
num = 100
series_from_num = pd.Series(num, index=[0, 1, 2, 3])
print(series_from_num)

# - словари
dictionary = {'A': 1, 'B': 2, 'C': 3}
series_from_dict = pd.Series(dictionary)
print(series_from_dict)

# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series

# Создаем два объекта Series
names = pd.Series(['Jared', 'John', 'Ann'])
surnames = pd.Series(['Smith', 'Black', 'Lee'])

# Объединяем их в DataFrame
df_from_series = pd.DataFrame({'Name': names, 'Surname': surnames})
print(df_from_series)

# - списки словарей
data = [
    {'Name': 'Jared', 'Surname': 'Smith'},
    {'Name': 'John', 'Surname': 'Black'},
    {'Name': 'Ann', 'Surname': 'Lee'}
]

df_from_dict = pd.DataFrame(data)
print(df_from_dict)

# - словари объектов Series

data_dict = {
    'Name': pd.Series(['Jared', 'John', 'Ann']),
    'Surname': pd.Series(['Smith', 'Black', 'Lee'])
}

df_from_series_dict = pd.DataFrame(data_dict)
print(df_from_series_dict)

# - двумерный массив NumPy
data_array = np.array([
    ['Smith', 'Jared'],
    ['Black', 'John'],
    ['Lee', 'Ann']
])

df_from_np_array = pd.DataFrame(data_array, columns=['Surname', 'Name'])
print(df_from_np_array)

# - структурированный массив Numpy
struct_array = np.array(
    [(40, 'Jared'), (20, 'John'), (30, 'Ann')],
    dtype=[('Age', 'i4'), ('Name', 'U10')]
)

df_from_struct_array = pd.DataFrame(struct_array)
print(df_from_struct_array)


# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так,
# чтобы вместо NaN было установлено значение 1

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

# Объединение индексов (недостающее заполняется Nan)
cities = pd.DataFrame({'area1': area, 'pop1': pop})

# Замена NaN на 1
cities.fillna(1, inplace=True)

print(cities)


# 4. Переписать пример с транслированием для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
rng = np.random.default_rng(1)
A = rng.integers(0, 10, (3, 4))
df = pd.DataFrame(A, columns=['a', 'b', 'c', 'd'])
print(df)

# Получение значений из четных столбцов первой строки
even_columns_values = df.iloc[0, ::2]

# Применение вычитания значений из четных столбцов первой строки непосредственно к DataFrame
df.iloc[:, ::2] = df.iloc[:, ::2].subtract(even_columns_values.values)
print(df)


# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

# Создаем DataFrame с несколькими NaN значениями
na_data = {
    'A': [1, 2, np.nan, np.nan, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, np.nan, np.nan, np.nan, 5]
}

na_df = pd.DataFrame(na_data)
print(na_df)

# ffill() копирует последнее ненулевое значение вниз
df_ffill = na_df.ffill()
print(df_ffill)

# bfill() копирует первое ненулевое значение вверх
df_bfill = na_df.bfill()
print(df_bfill)
