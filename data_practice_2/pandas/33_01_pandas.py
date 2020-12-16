import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1, 10, (5, 2)), columns=['A', 'B'])
print(df)
print(df['A'] > 5)

print(df[(df['A'] > 5) & (df['B'] < 5)])
print('\n')
print(df.query('A > 5 and B < 5'))