import pandas as pd
import numpy as np

A = pd.DataFrame(np.random.randint(0, 10, (2,2)), columns=['A', 'B'])
B = pd.DataFrame(np.random.randint(0, 10, (3,3)), columns=['A', 'B', 'C'])
print(A)
print(B)

print(A + B)

print(A.add(B, fill_value=0))