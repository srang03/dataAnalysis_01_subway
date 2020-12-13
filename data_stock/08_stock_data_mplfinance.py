# 캔들 차트 시각화하기
# 이번에는 주식의 차트를 캔들차트로 한번 표현해봅시다.
# 캔들차트는 봉차트라고도 하는데, 캔들차트라는 이름이 붙은 이유는 생김새가 마치 양초(캔들)처럼 생겼기 때문입니다.
# 이런 봉차트는 하나하나가 너무나 중요한데, 그 이유는 하나의 봉 속에 주식투자자들의 심리가 모두 반영되어 있기 때문입니다.
# 그러다 보니 봉차트를 신봉하는 분들 중에는 재무상태표니, 포괄손익계산서니 하는 것들은 볼 필요도 없이 
# 오직 봉차트만으로도 충분히 주식투자를 할 수 있다고 주장하는 사람들도 있을 정도입니다.
# 이번 실습에서는 mplfinance 라이브러리를 사용해 간단히 주가 데이터를 캔들 차트로 시각화해보도록 하겠습니다.



from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import matplotlib.dates as mdates
import numpy as np


# 주식 데이터 불러오기
df = pd.read_csv('./data/stock.csv', index_col = 0, parse_dates = True) 
df2 = pd.read_csv('./data/stock.csv', index_col = 0, parse_dates = True) 

print('주가 데이터 출력')
print(df)


# mplfinance 라이브러리를 사용하면 캔들 차트를 간편하게 시각화할 수 있습니다.
mc = mpf.make_marketcolors(up='r',down='b')
s  = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df, type='candle', figscale=1.2, style=s)


# 시각화 함수
plt.savefig("./data/plot_4.png")


# 봉차트를 이해하는 방법
# 봉차트를 이해하기 위해서 시가, 종가, 최저가, 최고가의 의미를 다시 한 번 복습해보겠습니다.
# 시가 : 아침에 주식시장이 문을 열고나서 처음 이루어진 거래가격
# 종가: 주식시장이 문을 닫을 때의 가격
# 최저가: 하루 중 최저 가격
# 최고가: 하루 중 최고 가격


# 봉차트는 주가가 올랐을 때는 빨간색으로 표현하며 이를 ‘양봉’이라고 합니다. 
# 반대로 주가가 내렸을 때는 파란색으로 그리고, 이를 ‘음봉’이라고 합니다.

# 캔들 차트의 두꺼운 부분의 양쪽 끝은 시가와 종가가 됩니다.
# 양봉의 경우 가격이 아래에서 위로 올라갔다는 의미이므로 두꺼운 부분의 아래쪽이 시가, 윗부분이 종가가 됩니다.
# 음봉의 경우 반대입니다.

# 몇몇 캔들에서는 뾰족한 선이 튀어나온 것이 보입니다. 이 선은 각각 해당 장 시점의 최고가와 최저가를 의미합니다.
# 캔들차트를 보면 하루의 거래 추세나 주가의 움직임 파악에 도움이 됩니다.