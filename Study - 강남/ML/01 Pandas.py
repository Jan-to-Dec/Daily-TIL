import pandas as pd 

# ================================
# Pandas
# ================================

pd.set_option('display.max_columns', 100) # 콘솔에서 보여질 최대 칼럼 개수 

path = r'C:\ITWILL\4_Python_ML\data'

wdbc = pd.read_csv(path + '/wdbc_data.csv')
wdbc.info()

print(wdbc.head())


# 전체 칼럼 가져오기 
cols = list(wdbc.columns)

# 1. DF 병합(merge) : 공통칼럼 기준 
DF1 = wdbc[cols[:16]] # id
DF2 = wdbc[cols[16:]] # id(x) 

# 공통칼럼 추가 : id 
DF2['id'] = wdbc.id

DF1.shape # (569, 16)
DF2.shape # (569, 17)

DF3 = pd.merge(left=DF1, right=DF2, on='id') 
DF3.shape # (569, 32)


# 2. DF 결합(concat)
DF2 = wdbc[cols[16:]]

DF4 = pd.concat(objs=[DF1, DF2], axis = 1) # 열축 기준 결합(cbind)
DF4.shape # (569, 32)


# 3. Inner join과 Outer join 
name = ['hong','lee','park','kim']
age = [35, 20, 33, 50]

df1 = pd.DataFrame(data = {'name':name, 'age':age}, 
                   columns = ['name', 'age'])

name2 = ['hong','lee','kim']
age2 = [35, 20, 50]
pay = [250, 350, 250] # 추가 

df2 = pd.DataFrame(data = {'name':name2, 'age':age2,'pay':pay}, 
                   columns = ['name', 'age', 'pay'])

# Inner join
inner = pd.merge(left=df1, right=df2, on=['name','age'], how='inner')
inner


# left Outer join : left 기준 
outer = pd.merge(left=df1, right=df2, on=['name','age'], how='outer')  
outer

# ================================
# DF_reshape
# ================================
buy = pd.read_csv(path + '/buy_data.csv')

print(buy.info())

print(buy)
buy.shape # (22, 3) : 2d 

# 1. 2차원(wide) -> 1차원(long) 구조 변경
buy_long = buy.stack() # 22*3
buy_long.shape # (66,) : 1d 

# 2. 1차원(long) -> 2차원(wide) 구조 변경 
buy_wide = buy_long.unstack() # 복원 기능 
buy_wide.shape # (22, 3) : 2d 

# 3. 전치행렬 : 행축 <-> 열축  
buy_tran = buy.T
buy_tran.shape # (3, 22)

# 4. 중복 행 제거
dir(buy) 
buy.duplicated() # 중복 행 확인 

buy2 = buy.drop_duplicates() # 중복 행 제거
buy2.shape # (20, 3)
buy2

# 5. 특정 칼럼을 index 지정 
new_buy = buy.set_index('Date') # 구매날짜 
new_buy.shape # (22, 2)
new_buy

# 날짜 검색 
new_buy.loc[20150101] # 명칭색인 
new_buy.loc[20150107]

#new_buy.iloc[20150101] # 오류 : out-of-bounds : 색인 범위 초과 
# 색인 자료형은 int형이지만 동일한 구매날짜를 명칭으로 지정한다.  

# [추가] 주가 dataset 적용 
stock = pd.read_csv(path + '/stock_px.csv')
stock.info()
stock.head() 
# 칼럼명 수정  
stock.columns = ['Date','AAPL','MSFT','XOM','SPX']
# object -> date형 변환 
stock['Date'] = pd.to_datetime(stock.Date) 
stock.info()

# Date 칼럼 색인 지정 
new_stock = stock.set_index('Date')
new_stock.head() # 2003-01-02
new_stock.tail() # 2011-10-10
# subset 만들기 
app_ms = new_stock[['AAPL','MSFT']]
# 8년치 주가 변동량 
app_ms.plot() 
# 2011년도 주가 변동량 
app_ms.loc['2011'].plot()
# 2008~2011년도 주가 변동량 
app_ms.loc['2008':'2011'].plot()
# 2011년도 2분기 주가 변동량
app_ms.loc['2011-04':'2011-07'].plot()


# ================================
# CSV file 
# ================================
# 1. csv file read

# 1) 칼럼명이 없는 경우 
st = pd.read_csv(path + '/student.csv', header=None)
st 

# 칼럼명 수정 
col_names = ['sno','name','height','weight'] # list 
st.columns = col_names # 칼럼 수정 
print(st)

# 2) 칼럼명 특수문자(.) or 공백 
iris = pd.read_csv(path + '/iris.csv')
print(iris.info())
iris['Sepal.Length']

# 점(.) -> 언더바(_) 교체 
iris.columns = iris.columns.str.replace('.','_') # ('old','new')
iris.info() # Sepal_Length
iris.Sepal_Length

# 3) 특수구분자(tab키), 천단위 콤마 
# pd.read_csv('file', delimiter='\t', thousands=',')

# 2. data 처리 : 파생변수 추가 
bmi = st.weight / (st.height*0.01)**2
bmi

# bmi 파생변수 추가 : 비율척도(연속형) 
st['bmi'] = bmi
st

# label 파생변수 추가 : 명목척도(범주형)
label = [] 

for bmi in  st.bmi : 
    if bmi >= 18 and bmi <= 23 :
        label.append('normal')
    elif bmi > 23 :
        label.append('fat')
    else :
        label.append('thin')

# 파생변수 추가 
st['label'] = label

print(st)

dir(st)

# 3. csv file 저장 
st.to_csv(path + '/st_info.csv', index = None, encoding='utf-8')
# index = None : 행이름 저장 안함 

# ================================
# group by
# ================================

# 1. 범주형 변수 기준 subset 만들기
# 2. 범주형 변수 기준 group & 통계량
# 3. apply() 함수 : DataFrame(2D) 객체에 함수 적용 
# 4. map() 함수 : Series(1D) 객체에 함수 적용

# dataset load & 변수 확인
wine = pd.read_csv(path  + '/winequality-both.csv')
print(wine.info())

# 칼럼 공백 -> '_' 교체 
wine.columns = wine.columns.str.replace(' ', '_')
wine.head()
print(wine.info())


# 5개 변수 선택 : subset 만들기 
wine_df = wine.iloc[:, [0,1,4,11,12]] # 위치 기반
print(wine_df.info()) 

# 특정 칼럼명 수정 
columns = {'fixed_acidity':'acidity', 'residual_sugar':'sugar'} # {'old','new'} 
wine_df = wine_df.rename(columns = columns) 
wine_df.info()  

# 범주형 변수 확인 : 와인유형   
print(wine_df.type.unique()) # ['red' 'white']
print(wine_df.type.nunique()) # 2
wine_df.type.value_counts()

# 이산형 변수 확인 : 와인 품질    
print(wine_df.quality.unique()) # [5 6 7 4 8 3 9]
print(wine_df.quality.value_counts())


# 1. 범주형 변수 기준 subset 만들기 

# 1) 1개 집단 기준  
red_wine = wine_df[wine['type']=='red']  # DF[DF.칼럼 조건식]
red_wine.shape # (1599, 5)

white_wine = wine_df[wine['type'] == 'white']
white_wine.shape # (4898, 5)


# 2) 2개 이상 집단 기준 : type : {red(o), blue(x), white(o)}
two_wine_type = wine_df[wine_df['type'].isin(['red','white'])] 


# 3) 범주형 변수 기준 특정 칼럼 선택 : 1차원 구조
red_wine_quality = wine.loc[wine['type']=='red', 'quality']  
red_wine_quality.shape # (1599,)

white_wine_quality = wine.loc[wine['type']=='white', 'quality'] 
white_wine_quality.shape # (4898,)


# 2. 범주형 변수 기준 group & 통계량

# 1) 범주형변수 1개 이용 그룹화
# 형식) DF.groupby('범주형변수') 

type_group = wine_df.groupby('type')
print(type_group) # DataFrameGroupBy object 정보 

# 각 집단별 빈도수 
type_group.size()  

# 그룹객체에서 그룹 추출 
red_df = type_group.get_group('red')
white_df = type_group.get_group('white')
red_df.shape # (1599, 5)
white_df.shape # (4898, 5)
    
# 그룹별 통계량 : 연산과정 ppt.52 참고 
print(type_group.sum()) 
print(type_group.mean())

# 2) 범주형 변수 2개 이용 : 나머지 변수(3개)가 그룹 대상 
# DF.groupby(['범주형변수1', '범주형변수2'])
wine_group = wine_df.groupby(['type','quality']) # 2개 x 7개 = 최대 14  

# 각 집단별 빈도수
wine_group.size()

       
# 그룹 통계 시각화 
grp_mean = wine_group.mean()
grp_mean

grp_mean.plot(kind='bar')


# 3. apply() 함수 : DataFrame(2D) 객체에 외부함수 적용

# 1) 사용자 함수 : 0 ~ 1 사이 정규화 
def normal_df(x):
    nor = ( x - min(x) ) / ( max(x) - min(x) )
    return nor


# 2) 2차원 data 준비 : wine 데이터 적용 
wine_x = wine_df.iloc[:, 1:] # 숫자변수만 선택 
wine_x.shape # (6497, 4)

wine_x.describe()

# 3) apply 함수 적용 : 열(칼럼) 단위로 실인수 전달
# 형식) DF.apply(내장함수/사용자함수)   
wine_nor = wine_x.apply(normal_df) 
wine_nor
print(wine_nor.describe()) # 정규화 확인 


# 4. map() 함수 : Series(1D) 객체에 함수 적용   

# 1) 인코딩 함수 
def encoding_df(x):
    encoding = {'red':[1,0], 'white':[0,1]}
    return encoding[x]

# 2) 1차원 data 준비 
wine_type = wine_df['type']
wine_type.shape # (6497,)
type(wine_type) # pandas.core.series.Series

# 3) map 함수 적용 
# 형식) Series.map(내장함수/사용자함수)
label = wine_type.map(encoding_df)
label

# lambda 이용 : 한 줄 함수 적용 
encoding = {'red':[1,0], 'white':[0,1]} # dict : mapping table 

wine_df['label'] = wine_df['type'].map(lambda x : encoding[x])

wine_df.head()
wine_df.tail()


# ================================
# Pivot Table
# ================================

pivot_data = pd.read_csv(path + '/pivot_data.csv')
pivot_data.info()

# 1. 핏벗테이블 작성
ptable = pd.pivot_table(data=pivot_data, 
               values='price', 
               index=['year','quarter'], 
               columns='size', aggfunc='sum')
 
print(ptable)


# 2. 핏벗테이블 시각화 : 누적형 가로막대 
ptable.plot(kind='barh', stacked=True)