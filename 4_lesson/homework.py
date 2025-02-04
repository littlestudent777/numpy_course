import numpy as np
import pandas as pd

#1. Разобраться как использовать мультииндексные ключи в данном примере
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]

# Вначале создаём мультииндекс
index = pd.MultiIndex.from_tuples(index)

pop = pd.Series(population, index=index)

pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)
# Тогда операции работают
pop_df_1 = pop_df.loc['city_1', 'something']
print(pop_df_1)
pop_df_2 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print(pop_df_2)
pop_df_3 = pop_df.loc[['city_1', 'city_3'], 'something']
print(pop_df_3)


# 2. Из получившихся данных выбрать данные по
# - 2020 году (для всех столбцов)
# - job_1 (для всех строк)
# - для city_1 и job_2

index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

rng = np.random.default_rng(1)
data = rng.random((4, 6))
data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)

# 1
data_2020 = data_df.xs(2020, level='year')
print(data_2020)

# 2
job_1_data = data_df.xs('job_1', level='job', axis=1)
print(job_1_data)

# 3
city_job_data = data_df.loc['city_1'].xs('job_2', level='job', axis=1)
print(city_job_data)


# 3. Взять за основу DataFrame со следующей структурой
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
# - все данные по первому городу и первым двум person-ам (с использование срезов)

data = np.random.rand(4, 6)  # 4 строки и 6 столбцов
df = pd.DataFrame(data, index=index, columns=columns)

# 1
data_person_1_3 = df.loc[:, ['person_1', 'person_3']]
print(data_person_1_3)
# 2
data_city_1_person_1_2 = df.loc['city_1', 'person_1':'person_2']
print(data_city_1_person_1_2)

# Приведите пример (самостоятельно) с использованием pd.IndexSlice

data_person_1_3_sl = df.loc[:, pd.IndexSlice[['person_1', 'person_3'], :]]
print(data_person_1_3_sl)


#4. Привести пример использования inner и outer джойнов для Series
ser1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
ser2 = pd.Series(['b', 'c', 'f'], index=[4, 5, 6])

outer_join = pd.concat([ser1, ser2], axis=0)  # По умолчанию outer
print(outer_join)

inner_join = ser1[ser1.index.intersection(ser2.index)]  # Пустое, так как индексы не пересекаются
print(inner_join)
