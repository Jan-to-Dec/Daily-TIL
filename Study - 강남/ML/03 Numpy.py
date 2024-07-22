import numpy as np # 별칭 
import matplotlib.pyplot as plt 
import pandas as pd

# 1. list 배열 vs numpy 다차원 배열 

# 1) list 배열
lst = [1, 2, 3, 3.5] 
print(lst) 
print(lst * 3 ) 
sum(lst)  

# 2) numpy 다차원 배열 
arr = np.array(lst)   
print(arr) 
print(arr * 0.5) 
arr.sum()

# 2. array() : 다차원 배열 생성 
lst1 = [3, 5.2, 4, 7]
print(lst1) 

arr1d = np.array(lst1) # array(단일list)
print(arr1d.shape)

print('평균 =', arr1d.mean()) 
print('분산=', arr1d.var())
print('표준편차=', arr1d.std()) 

# 3. broadcast 연산 
# - 작은 차원이 큰 차원으로 늘어난 후 연산 
# scala(0) vs vector(1)
print(0.5 * arr1d)

x = arr1d # 객체 복제 
x # [3. , 5.2, 4. , 7. ]

mu = x.mean() # 모평균  
var = sum((x - mu)**2) / len(x)

# 4. zeros or ones 
zerr = np.zeros( (3, 10) ) 
print(zerr) 

onearr = np.ones( (3, 10) ) 
print(onearr)

# 5. arange : range 유사함
range(1, 11)
#range(0.5, 10.5) 
 
arr = np.arange(-1.2, 5.5) # float 사용 가능, 배열 객체  
print(arr) 

# ex) x의 수열에 대한 2차 방정식 
x = np.arange(-1.0, 2, 0.1) 

y = x**2 + 2*x + 3 
print(y)

plt.plot(x, y)
plt.show()

#####################################33
# Indexing
#######################################

import numpy as np

# 1) list 배열 색인
ldata = [0,1,2,3,4,5]
print(ldata[:])
print(ldata[3])
print(ldata[:3])
print(ldata[-1])

# 2) numpy 다차원 배열 색인 : list 동일 
arr = np.arange(10) # 0~9
print(arr[:])
print(arr[3])
print(arr[:3])
print(arr[-1])

# 2. slicing : 특정 부분을 잘라서 new object
arr = np.arange(10) # 0~9
arr_obj = arr[1:4]
print(arr_obj)

arr_obj[:] = 100
print(arr_obj)

print(arr)

arr_obj2 = arr[1:4].copy()
arr_obj2[:] = 200

print(arr)

# 3. 고차원 색인(indexing) : 2차원 이상 

# 1) 2차원 indexing 
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)

print(arr2d[0, :])
print(arr2d[0])
print(arr2d[1:,1:])
print(arr2d[::2])

print(arr2d[[0,2]])
print(arr2d[[0,2], [0,2]])

# 2) 3차원 indexing 
arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])
print(arr3d)

print(arr3d.shape)

print(arr3d[0])
print(arr3d[0, 1])
print(arr3d[0, 1, 1:])

# 4. 조건식 색인(boolean index)
dataset = np.random.randn(3, 4)
print(dataset)

print(dataset[dataset >= 0.7])

result = dataset[np.logical_and(dataset >= 0.1, dataset <= 1.5)]
print(result)

result = dataset[(dataset >= 0.1) & (dataset <= 1.5)]
print(result)

#######################################
# 범용 함수(universal function)
#  - 다차원 배열의 원소를 대상으로 수학/통계 등의 연산을 수행하는 함수
#######################################

import numpy as np

data = np.random.randn(5)
print(data)
print(np.abs(data))
print(np.sqrt(data))
print(np.square(data))
print(np.sign(data))
print(np.var(data))
print(np.std(data))

data2 = np.array([1, 2.5, 3.36, 4.6])

print(-np.log(0.5))

print(np.log(data2))
print(np.exp(data2))

print(np.ceil(data2))
print(np.rint(data2))
print(np.round(data2, 0))

data2 = np.array([1, 2.5, 3.3, 4.6, np.nan])
print(np.isnan(data2))
print(data2[np.logical_not(np.isnan(data2))])
print(data2[~(np.isnan(data2))])

data2 = np.random.randn(3, 4)
print(data2)
print(data2.shape)

print('합계=', data2.sum())
print('평균=', data2.mean())
print('표준편차=', data2.std())
print('최댓값=', data2.max())
print('최솟값=', data2.min())

print(data2.sum(axis=0))
print(data2.sum(axis=1))
print('전체 원소 합계 :', data2.sum())

#####################################33
# Random
#######################################
# 1. 난수 실수와 정수  

# 1) 난수 실수 : [0, 1)
data = np.random.rand(5, 3)
print(data)

# 차원 모양
print(data.shape)

# 난수 통계
print(data.min())
print(data.max())
print(data.mean())

# 2) 난수 정수 : [a, b)
data = np.random.randint(165, 175, size=50)
print(data)

# 차원 모양
print(data.shape)

# 난수 통계
print(data.min())
print(data.max())
print(data.mean())

dir(np.random)

# 2. 이항분포 
np.random.seed(12)
print(np.random.binomial(n=1, p=0.5, size=10))

# 3. 정규분포 : N(mu, sigma^2)
height = np.random.normal(173, 5, 2000)
print(height)

height2 = np.random.normal(173, 5, (500, 4))
print(height2)
print(height2.shape)

# 난수 통계
print(height.mean())
print(height2.mean())

# 정규분포 시각화 
plt.hist(height, bins=100, density=True, histtype='step')
plt.show()

# 4. 표준정규분포 : N(mu=0, sigma=1)
standNormal = np.random.randn(500, 3)
print(standNormal.mean())
print(standNormal.std())

# normal 함수 이용 
standNormal2 = np.random.normal(0, 1, (500, 3))
print(standNormal2.mean())

# 정규분포 시각화 
plt.hist(standNormal[:,0], bins=100, density=True, histtype='step', label='col1')
plt.hist(standNormal[:,1], bins=100, density=True, histtype='step', label='col2')
plt.hist(standNormal[:,2], bins=100, density=True, histtype='step', label='col3')
plt.legend(loc='best')
plt.show()

# 5. 균등분포 
uniform = np.random.uniform(10, 100, 1000)
plt.hist(uniform, bins=15, density=True)
plt.show()

# 6. DataFrame sampling

# csv file 가져오기
path = r'C:\ITWILL\4_Python_ML\data'
wdbc = pd.read_csv(path + '/wdbc_data.csv')
print(wdbc.info())

# 1) seed값 적용 
np.random.seed(123)

# 2) pandas sample() 이용  
wdbc_df = wdbc.sample(400)
print(wdbc_df.shape)
print(wdbc_df.head())

# 3) training vs test sampling
idx = np.random.choice(a=len(wdbc), size=int(len(wdbc) * 0.7), replace=False)

# training dataset : 70%
train_set = wdbc.iloc[idx]
print(train_set.shape)

# testing dataset : 30%
test_idx = [i for i in range(len(wdbc)) if i not in idx]
test_set = wdbc.iloc[test_idx]
print(test_set.shape)

