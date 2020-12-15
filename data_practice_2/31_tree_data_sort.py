# 쑥쑥 자라라 콩나무야!
# 잭은 여러 개의 신비한 힘을 지닌 콩을 심고 하늘까지 쑥쑥 자라는 콩나무의 모습을 보았어요.
# 쑥쑥 자란 콩나무들의 키, 둘레, 열린 콩의 갯수 데이터가 csv파일로 만들어져 있네요.
# 우리는 csv 데이터를 읽고, 정렬해서 어떤 나무가 가장 큰 나무인지 확인해 보고자 해요!
# 어떤 나무의 height 변수가 가장 큰 값을 갖는지 알아보고, 해당 나무의 정보를 출력하는 실습을 진행해 봐요.

import pandas as pd

def main():
    df = pd.read_csv('./data/tree_data.csv')

    sorted_df = df.sort_values('height', ascending=False)
    print(sorted_df.loc[0])
    

if __name__ == "__main__":
    main()
