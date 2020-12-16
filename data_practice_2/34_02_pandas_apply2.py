import pandas as pd
import numpy as np

df = pd.DataFrame(columns=['phone'])
df.loc[0] = '010-1234-1234'
df.loc[1] = '공일공-일이삼사-1234'
df.loc[2] = '010.1234-일이삼4'
df.loc[3] = '공1공-1234.1이34'

def preprocessing_phone(phone):
     mapping_dict = {
         '공' : '0', 
         '일' : '1',
         '이' : '2',
         '삼' : '3',
         '사' : '4',
         '오' : '5',
         '-' : '',
         '.' : ''
     }
     for key, value in mapping_dict.items():
        phone = phone.replace(key, value)
    
     return phone

df['preprocessing_phone'] = df['phone'].apply(preprocessing_phone)
print(df)


