import matplotlib.pyplot as plt
import pandas as pd

# 분석해보고 싶은 쇼핑 카테고리를 설정합니다
category = '음식서비스'

def main(category):
	# 온라인 거래량 데이터셋을 불러옵니다
    shopping = pd.read_csv('./data/shopping_data.csv', index_col=['상품군별'])

    # 작성된 이미지를 제출합니다
    draw_image(shopping, category)


# 데이터를 다루고 이미지를 그리는 부분입니다
def draw_image(shopping, category):

    # 데이터의 크기를 확인합니다
    y_max = shopping.loc[category].max()
    y_min = shopping.loc[category].min()

    # 이미지 데이터를 만듭니다.
    plt.figure(figsize=(8,4))
    plt.rc('font', family='NanumBarunGothic')
    plt.plot(shopping.loc[category])

    plt.vlines('20-1', y_min, y_max, color='red')
    plt.text(x='20-1', y=y_max, s='   코로나 발생', color='red')
    plt.title('코로나 발생에 따른 온라인 쇼핑 거래랑 추이')

    # 이미지 데이터를 저장합니다.
    plt.savefig('corona.png')


if __name__ == "__main__":
    main(category)