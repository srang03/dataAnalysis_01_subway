import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['gender'])
df.loc[0] = 'M'
df.loc[1] = 'F'
df.loc[2] = 'M'
df.loc[3] = 'F'

df['gender_num'] = df['gender'].replace({'M':1, 'F':0})
print(df)

df['gender'].replace({'M':1, 'F': 0}, inplace=True)
print(df)