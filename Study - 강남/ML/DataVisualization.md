# Data Visualization

## 1. Matplotlib 
라인 플롯, 바 차트, 파이 차트, 히스토그램, 박스 플롯, Scatter 플롯 등을 비롯하여 다양한 차트와 플롯 스타일을 지원

```python
import numpy as np # data 생성
import matplotlib.pyplot as plt # data 시각화

# 한글 지원
plt.rcParams['font.family'] = 'Malgun Gothic'

#음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 정규분포 시각화 : 한글지원
data = np.random.randn(100) # 정규분포 자료 생성

plt.plot(data)
plt.title("정규분포를 따르는 난수 시각화")
plt.xlabel("색인(index)")
plt.ylabel("난수(random number")
plt.show()

```

## 2. pandas 객체 

```python 
df = DataFrame(np.random.randn(10, 4),columns=['one', 'two', 'three', 'four'])
print(df)

df.plot()
plt.show()
```

## 3. Seaborn
Seaborn은 Matplotlib 기반으로 다양한 배경 테마와 통계용 차트를 제공한다

```python
sns.set_style(style='darkgrid')

sns.countplot(x='day', data=tips) 

plt.title('day of tips')
plt.show()
```
