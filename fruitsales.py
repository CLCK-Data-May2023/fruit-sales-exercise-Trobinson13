# import denpendecies
import pandas as pd
import os

# create/import dataframe
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

df = pd.DataFrame(data, index = ['2017 Sales', '2018 Sales'])

# export data frame to csv file

df.to_csv('fruit.csv')

# file_path = os.path.join('assets', 'fruit.csv')

# absolute_path = os.path.abspath(file_path)

# df.to_csv(absolute_path)