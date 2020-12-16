import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(5), columns=['number'])
def square(x):
    return x**2

new_df = df['number'].apply(square)
print('\n----------------')
print(df)
print(new_df)
print('\n----------------')
df['square'] = df.number.apply(square)
print(df)