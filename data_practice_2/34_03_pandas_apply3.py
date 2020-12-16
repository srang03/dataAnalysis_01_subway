# 함수로 데이터 처리하기
# apply() 를 이용하면 함수를 이용하여 데이터 프레임에 값을 적용할 수 있습니다
# 일정한 동작으로 데이터 프레임을 수정하고자 할 때 편리하게 이용할 수 있는 기능입니다.
# apply()의 다양한 활용법을 알아보고, 실습 문제도 풀어보세요.

import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(5), columns=["Num"])
print(df, "\n")

# 값을 받으면 제곱을 해서 돌려주는 함수

def square(x):
    return x**2


# apply로 컬럼에 함수 적용
df['Square'] = df['Num'].apply(square)


# 람다 표현식으로도 적용하기
df['Square'] = df['Num'].apply(lambda x : x**2)


# 지시사항
# 데이터 프레임df에는 정수를 담고있는 Num 칼럼이 있습니다.

# df 데이터 프레임에 함수를 이용하여 Num의 제곱수를 나타내는 
# 칼럼인 Square 칼럼을 추가하고, 데이터프레임을 출력해봅시다.