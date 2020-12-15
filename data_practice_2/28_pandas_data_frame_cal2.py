import pandas as pd
data = {
    'A' : [ i for i in range(3) ],
    'B' : [ i *2 for i in range(3) ]
}

print('\n -----------')
print(data)
print('\n -----------')

print('\n -----------')
df = pd.DataFrame(data)
# print(df)
print('\n -----------')


print(df['A'].sum())
print(df.sum())
print(df.mean())