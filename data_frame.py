# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd
import random

# Создаем  DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data =pd.DataFrame({'whoAmI':lst})

# Получаем уникальные значиния из столбца

unique_values = data['whoAmI'].unique()

# Создаем новые столбцы для каждого уникального значения и заполняем их нулями

for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop('whoAmI', axis=1, inplace=True)

# Выводим первые строки преоброзованного DataFrame

print(data.head())