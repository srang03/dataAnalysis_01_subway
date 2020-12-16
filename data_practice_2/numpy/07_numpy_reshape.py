import numpy as np

# reshape 메서드를 통해서 1차원 배열에서 2차원 배열로 변경하는 작업이다.
x = np.arange(8)
print(x)
print(x.shape)

x2 = x.reshape((2,4))
print(x2)
print(x2.shape)

# concatenate : 내가 원하는 배열들을 이어 붙이는 기능을 제공하는 메서드이다.
# x 배열과 y 배열을 생성한다.
x = np.array([0, 1, 2])
y = np.array([3, 4, 5])

# x 배열과 y 배열을 합친다.
array = np.concatenate([x, y])
print(array)

# concatenate() 메서드에서 두 번째 인자로 axis를 통해서 어떤 축으로 배열을 이어 붙일지 정할 수 있다.
# axis = 0 : 세로(아래) 방향으로 설정할 수 있다.
# axis = 1 : 가로(좌우)방향으로 설정할 수 있다.

matrix = np.arange(4).reshape(2, 2)

matrix_axis_0 = np.concatenate([matrix, matrix], axis=0)
print(matrix_axis_0 )


matrix_axis_1 = np.concatenate([matrix, matrix], axis=1)
print(matrix_axis_1)


# np.split : axis 축을 기준으로 나누는 메서드
matrix = np.arange(16).reshape(4, 4)
print(matrix)

# axis=0 : 세로축을 기준으로
# 두 번째 인자 [3] : 인덱스가 3인 위치에서
# matrix : 해당 배열을
# np.split : 나누어라

upper, lower = np.split(matrix, [3], axis=0)
print(upper)
print('-------')
print(lower)
