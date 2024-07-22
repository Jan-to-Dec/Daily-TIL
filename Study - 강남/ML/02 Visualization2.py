import pandas as pd # Series, DataFrame 
import numpy as np  
import matplotlib.pyplot as plt 

# 1. 기본 차트 시각화 

# 1) Series 객체 시각화 : 1d  
ser = pd.Series(np.random.randn(10),
          index=np.arange(0, 100, 10))
ser.plot() # 선 그래프 
plt.show()

# 2) DataFrame 객체 시각화 : 2d
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one', 'two', 'three', 'fore'])
df.plot()  
plt.show()

# 막대차트 
df.plot(kind='bar', title='bar chart')
plt.show()

# 2. dataset 이용 
path = r'C:\ITWILL\4_Python_ML\data'

tips = pd.read_csv(path + '/tips.csv')
tips.info() 

# 행사 요일별 : 파이 차트 
cnt = tips['day'].value_counts() # 4개 
cnt.plot(kind='pie')
plt.show()

tips['size'].value_counts() # 6개 

# 요일(day) vs 규모(size) : 교차분할표
table = pd.crosstab(index=tips['day'], 
                    columns=tips['size'])
table.plot(kind='bar')

# size : 2~5칼럼으로 subset 
new_table = table.loc[:,2:5]
new_table.plot(kind='barh', stacked=True,
               title='day vs size')
plt.show()

####################################
# Seaborn Code 
####################################
import seaborn as sns

# 1. 데이터셋 확인 
names = sns.get_dataset_names() 
print(names)
len(names) 

iris = sns.load_dataset('iris')
print(iris.info())

tips = sns.load_dataset('tips')
print(tips.info())

titanic = sns.load_dataset('titanic')
print(titanic.info())

# subset 만들기 
df = titanic[['survived', 'age', 'class', 'who']]
print(df.info())
print(df.head())

# category형 정렬
df.sort_values(by='class') # category 오름차순

# object형 정렬 
df.sort_values(by='who') # object 오름차순 

# category형 변수 순서 변경 
df['class_new'] = df['class'].cat.set_categories(['Third', 'Second', 'First'])
df.sort_values(by='class_new')

# object -> category형 변환 
df['who_new'] = df['who'].astype('category') 
print(df.info())

# 2. 범주형 자료 시각화 

# 1) 배경 스타일 
sns.set_style(style='darkgrid')

tips = sns.load_dataset('tips')
print(tips.info())

tips.smoker.value_counts()
sns.countplot(x='smoker', data=tips) # 빈도수 + 막대차트 
plt.title('smoker of tips')
plt.show()

tips.day.value_counts()
sns.countplot(x='day', data=tips) # 빈도수 + 막대차트 
plt.title('day of tips')
plt.show()

sns.set(font="Malgun Gothic", 
            rc={"axes.unicode_minus":False}, style="darkgrid")

# dataset 로드 
flights = sns.load_dataset('flights')
print(flights.info())

iris = sns.load_dataset('iris')
print(iris.info())

# 1. 오차대역폭을 갖는 시계열 
sns.lineplot(x='year', y='passengers', data=flights)
plt.show()

# hue 추가 
sns.lineplot(x='year', y='passengers', hue='month',
            data=flights)
plt.show()

# 2. 선형회귀모델 
sns.regplot(x='sepal_length', y='petal_length', 
           data=iris)  
plt.show()

# 3. heatmap 
y_true = pd.Series([1,0,1,1,0]) # 정답 
y_pred = pd.Series([1,0,0,1,0]) # 예측치 

# 1) 교차분할표(혼동 행렬) 
tab = pd.crosstab(y_true, y_pred, 
            rownames=['관측치'], colnames=['예측치'])
print(tab)

# 2) heatmap
sns.heatmap(data=tab, annot=True) # annot = True : box에 빈도수 
plt.show()
