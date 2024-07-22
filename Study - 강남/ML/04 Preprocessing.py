from sklearn.preprocessing import LabelEncoder # class  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

####################################
# Missing Data 1
####################################
path = r'C:\ITWILL\4_Python_ML\data'
data = pd.read_csv(path + '/dataset.csv') 
data.info()

# 1. 칼럼단위 결측치(NaN) 확인  
print(data.isnull().any())
print(data.isnull().sum())
print(data.shape)

# 2. 전체 칼럼 기준 결측치 제거 
new_data = data.dropna()
print(new_data.shape)
print(data.shape[0] - new_data.shape[0])
print(new_data.isnull().sum())

# 3. 특정 칼럼 기준 결측치 제거   
new_data2 = data.dropna(subset=['job'])
print(new_data2.shape)
print(data.shape[0] - new_data2.shape[0])
print(new_data2.isnull().sum())

# 4. 모든 결측치 다른값으로 채우기 : 상수 or 통계
new_data3 = data.fillna(0.0)
print(new_data3.shape)
print(new_data3.isna().sum())

# 5-1. 특정변수 결측치 채우기 : 숫자변수(상수 or 통계 대체) 
new_data4 = data.copy()
print(new_data4.isna().sum())

new_data4['position'].fillna(new_data4['position'].mean(), inplace=True)
print(new_data4.isna().sum())

# 5-2. 특정변수 결측치 채우기 : 범주형변수(빈도수가 높은 값으로 대체)  
new_data5 = data.copy()
print(new_data5['job'].unique())
print(new_data5['job'].value_counts())

new_data5['job'].fillna(3.0, inplace=True)
print(new_data5.isnull().sum())

# 6. 결측치 비율 40% 이상인 경우 해당 컬럼 제거 
print(data.isna().sum())
print(12 / len(data))

new_data6 = data.drop(['job'], axis=1)
print(new_data6.shape)
print(new_data6.head())

####################################
# Missing Data 2
####################################
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정

# 데이터셋 출처 : https://www.kaggle.com/uciml/breast-cancer-wisconsin-data?select=data.csv
cencer = pd.read_csv(r'C:\ITWILL\4_Python_ML\data\brastCencer.csv')
cencer.info()

# 1. 변수 제거 
df = cencer.drop(['id'], axis = 1) # 열축 기준 : id 칼럼 제거  
df.shape # (699, 10)


# 2. x변수 숫자형 변환 : object -> int형 변환
df['bare_nuclei'] 

# DF['칼럼명'].astype('자료형') : Object -> int
df['bare_nuclei'] = df['bare_nuclei'].astype('int') # error 발생 
# ValueError: invalid literal for int() with base 10: '?'


# 3. 특수문자 결측치 처리 & 자료형 변환 

# 1) 특수문자 결측치 대체 : '?' <- NaN  
df['bare_nuclei'] = df['bare_nuclei'].replace('?', np.nan) # ('old','new')

# 2) 전체 칼럼 단위 결측치 확인 
df.isnull().any() 
df.isnull().sum() # 16
# bare_nuclei         True

# 3) 결측치 제거  
new_df = df.dropna(subset=['bare_nuclei'])    
new_df.shape # (683, 10) : 16개 제거 


# 4) int형 변환 
new_df['bare_nuclei'] = new_df['bare_nuclei'].astype('int64') 
new_df.info()
new_df['class'].unique() # [2, 4] -> [0, 1]


# 4. y변수 레이블 인코딩 : 10진수 변환
# 인코딩 객체 
encoder = LabelEncoder().fit(new_df['class']) # 1) 객체에 반영  

# data변환 : [2, 4] -> [0, 1]
labels = encoder.transform(new_df['class']) # 2) 자료 변형  
labels # 0 or 1

# 칼럼 추가 
new_df['y'] = labels

# class 변수 제거 
new_df = new_df.drop(['class'], axis = 1)

new_df.info()

###################################
# Outlier
###################################

data = pd.read_csv(r"C:\ITWILL\4_Python_ML\data\insurance.csv")
print(data.info())

# 1. 범주형 이상치 탐색  
print(data.sex.unique())
print(data.smoker.unique())
print(data.region.unique())

# 2. 숫자형 변수 이상치 탐색  
des = data.describe()
print(des)

# 3. boxplot 이상치 탐색 
plt.boxplot(data['age'])
plt.show()

plt.boxplot(data['bmi'])
plt.show()

plt.boxplot(data['charges'])
plt.show()

# 4. 이상치 처리 : 제거 & 대체 

# 1) bmi 이상치 제거 
df = data.copy()
df = df[df['bmi'] > 0]
print(df.shape)

# 2) age 이상치 대체   
df = data.copy()
df.loc[df.age > 100, 'age'] = 100
print(df.shape)

# 5. IQR방식 이상치 발견 및 처리

# 1) IQR방식으로 이상치 발견   
Q3 = des.loc['75%', 'age'] 
Q1 = des.loc['25%', 'age'] 
IQR = Q3 - Q1

outlier_step = 1.5 * IQR

minval = Q1 - outlier_step 
maxval = Q3 + outlier_step 
print(f'minval : {minval}, maxval : {maxval}') 

minval = 0

# 2) 이상치 제거  
df = data.copy() 
df = df[(df['age'] >= minval) & (df['age'] <= maxval)]
print(df.shape)

df['age'].plot(kind='box')

# 3) 이상치 대체 
df = data.copy()
df.loc[df['age'] < minval, 'age'] = minval  
df.loc[df['age'] > maxval, 'age'] = maxval
print(df.shape)

df['age'].plot(kind='box')

# 평균과 표준편차 이용 
df = data.copy()

avg = df['age'].mean()
std = df['age'].std()
n = 3 

minval = 0 
maxval = avg + n * std 

df = df[(df['age'] >= minval) & (df['age'] <= maxval)]
print(df.shape)

