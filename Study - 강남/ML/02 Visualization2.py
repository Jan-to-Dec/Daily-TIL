import pandas as pd # Series, DataFrame 
import numpy as np  
import matplotlib.pyplot as plt 

# 1. 기본 차트 시각화 

# 1) Series 객체 시각화 : 1d  
ser = pd.Series(np.random.randn(10),
          index = np.arange(0, 100, 10))
ser
dir(ser) # plot

ser.plot() # 선 그래프 
plt.show()

# 2) DataFrame 객체 시각화 : 2d
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one','two','three','fore'])
df

# 기본 차트 : 선 그래프 
df.plot()  
plt.show()

# 막대차트 
help(df.plot)

df.plot(kind = 'bar', title='bar chart')
plt.show()

# 2. dataset 이용 
path = r'C:\ITWILL\4_Python_ML\data'

tips = pd.read_csv(path + '/tips.csv')
tips.info() 

# 행사 요일별 : 파이 차트 
cnt = tips['day'].value_counts() # 4개 
type(cnt) # pandas.core.series.Series

cnt.plot(kind = 'pie')
plt.show()

tips['size'].value_counts() # 6개 

# 요일(day) vs 규모(size) : 교차분할표(카이제곱검정 도구) 
table = pd.crosstab(index=tips['day'], 
                    columns=tips['size'])

table

type(table) 

# 개별 막대차트 
table.plot(kind='bar')

# size : 2~5칼럼으로 subset 
new_table = table.loc[:,2:5]
new_table

# 누적형 가로막대차트 
new_table.plot(kind='barh', stacked=True,
               title = 'day vs size')
