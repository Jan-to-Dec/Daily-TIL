# 데이터 시각화의 한 형태
# 행렬 형태의 데이터를 색상으로 표현하여 각 값의 크기를 직관적으로 비교할 수 있게
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.standard_normal((30, 40))
plt.matshow(arr)
plt.show()

# 컬러바 나타내기
arr = np.random.standard_normal((30, 40))
plt.matshow(arr)
plt.colorbar()
plt.show()

# 색상 범위 지정하기
arr = np.random.standard_normal((30, 40))
plt.matshow(arr)
plt.colorbar(shrink=0.8, aspect=10)
# plt.clim(-1.0, 1.0)
plt.clim(-3.0, 3.0)
plt.show()

# 컬러맵 지정하기
arr = np.random.standard_normal((30, 40))
cmap = plt.get_cmap('PiYG')
cmap = plt.get_cmap('BuGn')
cmap = plt.get_cmap('Greys')
cmap = plt.get_cmap('bwr')

plt.matshow(arr, cmap=cmap)
plt.colorbar()
plt.show()

