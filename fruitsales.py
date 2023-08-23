# import denpendecies
import pandas as pd

# create/import dataframe
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34]
}

df = pd.DataFrame(data, index = ['2017 Sales', '2018 Sales'])

# export data frame to csv file 
df.to_csv('fruit.csv')
