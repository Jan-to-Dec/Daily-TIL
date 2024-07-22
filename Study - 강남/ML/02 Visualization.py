#######################
# 기본 그래프
#######################

import matplotlib.pyplot as plt # 시각화 
import random 

plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.rcParams['axes.unicode_minus'] = False 

# 1. 그래프 자료 생성 
data = range(-3, 7) # (start, stop-1)
print(data) # [-3, ... ,6]
len(data) # 10

# 2. 기본 그래프 
help(plt.plot)

# plot(x, y)        # plot x and y using default line style and color
# plot(x, y, 'bo')  # plot x and y using blue circle markers
# plot(y)           # plot y using x as index array 0..N-1
# plot(y, 'r+')     # ditto, but with red plusses

plt.plot(data) # 선색 : 파랑, 스타일 : 실선 
plt.title('선 색 : 파랑, 선 스타일 : 실선 ')
plt.show()

# 3. 색상 : 빨강, 선스타일(+)
plt.plot(data, 'r+') 
plt.title('선 색 : 빨강, 선 스타일 : +')
plt.show()

# 4. x,y축 선스타일과 색상 & 마커(circle marker)  
data2 = [random.gauss(0, 1) for i in range(10)]  

plt.plot(data, data2, 'ro') # (x=data, y=data2)
plt.show()

#######################
# Discreate
#######################
 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False



data = [127, 90, 201, 150, 250] # 국가별 수출현황 
year = [2010, 2011, 2012, 2013, 2014] # 년도 


# 1. 세로막대  
plt.bar(x = year, height=data) 
plt.title('국가별 수출현황')
plt.xlabel('년도별')
plt.ylabel('수출현황(단위 : 달러)')
plt.show()

# 2. 가로막대 
plt.barh(y= year, width = data, color='blue') 
plt.title('국가별 수출현황')
plt.xlabel('수출현황(단위 : 달러)')
plt.ylabel('년도별')
plt.show()

# 3. 누적형 세로막대 
cate = ['A', 'B', 'C', 'D'] 
val1 = [15, 8, 12, 10]  
val2 = [5, 12, 8, 15]  

plt.bar(cate, val1, label='데이터셋1', alpha=0.5)
plt.bar(cate, val2, bottom=val1, label='데이터셋2', alpha=1) 
plt.title('누적형 막대 그래프')
plt.xlabel('카테고리')
plt.ylabel('값')
plt.legend() 
plt.show()

# 4. 원 그래프 : 비율 적용 
labels = ['싱가폴','태국','한국','일본','미국'] 
print(data) # [127, 90, 201, 150, 250]

plt.pie(x = data, labels = labels) # 100% 
plt.show()

# 비율 계산 
tot = sum(data) 
rate = [round((d / tot)*100, 2)  for d in data ]  
rate 

# 새로운 lable 
new_lables = [] 

for i in range(len(labels)) :
    new_lables.append(labels[i] + '\n' + str(rate[i]) + '%')
    
plt.pie(x = data, labels = new_lables) 
plt.show()

#######################
# Continuous
#######################

import random # 난수 생성 
import statistics as st # 수학/통계 함수 
import matplotlib.pyplot as plt # data 시각화 

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 그래프 자료 생성 
data1 = range(-3, 7) # -3 ~ 6
data2 = [random.random() for i in range(10)] # 0~1사이 난수 실수 
data2

# 1. 산점도 그래프 : 2개 변수 이용, 단일 색상  
plt.scatter(x=data1, y=data2, c='r', marker='o')
plt.title('scatter plot')
plt.show()

# 군집별 산점도 : 군집별 색상 적용 
cdata = [random.randint(a=1, b=4) for i in range(10)]  # 난수 정수(1~4) 
cdata

plt.scatter(x=data1, y=data2, c=cdata, marker='o')
plt.title('scatter plot')
plt.show()

# 군집별 label 추가 
plt.scatter(x=data1, y=data2, c=cdata, marker='o') # 산점도 

for idx, val in enumerate(cdata) : # 색인, 내용
    plt.annotate(text=val, xy=(data1[idx], data2[idx]))
    #plt.annotate(text=텍스트, xy=(x좌표, y좌표)
plt.title('scatter plot') # 제목 
plt.show()

# 2. 히스토그램 그래프 : 1개 변수, 대칭성 확인     
data3 = [random.gauss(mu=0, sigma=1) for i in range(1000)] 
print(data3) # 표준정규분포(-3 ~ +3) 

# 난수 통계
min(data3)
max(data3) 

# 평균과 표준편차 
st.mean(data3) 
st.stdev(data3) 

# 정규분포 시각화 
help(plt.hist)
plt.hist(data3, label='hist1') # 기본형(계급=10),histtype='bar'  
plt.hist(data3, bins=20, histtype='stepfilled', label='hist2') # 계급, 계단형 적용  
plt.legend(loc = 'best') # 범례
plt.show()
'''
loc 속성
best 
lower left/right
upper left/right
center 
'''
# 3. 박스 플롯(box plot)  : 기초통계 & 이상치(outlier) 시각화
data4 = [random.randint(a=45, b=85) for i in range(100)]  # 45~85 난수 정수 
data4

plt.boxplot(data4)
plt.show()

# 기초통계 : 최솟값/최댓값, 사분위수(1,2,3)
min(data4) 
max(data4) 

# 사분위수 : q1, q2(중위수), q3
st.quantiles(data4) 

st.median(data4)
st.mean(data4)


# 4. 이상치(outlier) 발견 & 처리 
import pandas as pd 

path = r'C:\ITWILL\4_Python_ML\data'

insurance = pd.read_csv(path + '/insurance.csv')
insurance.info()

# 1) subset 만들기 
df = insurance[['age','bmi']] # 비율척도(절대0점)
df.shape # (1338, 2)

# 2) 이상치 발견과 처리 
df.describe() 

# 3) 이상치 시각화 
plt.boxplot(df)
plt.show()

# 4) 이상치 처리 : 100세 이하 -> subset 
new_df = df[df['age'] <= 100] # age 이상치 제거 
new_df.shape # (1335, 2)

plt.boxplot(new_df)
plt.show()

# 5) bmi 이상치 처리 : iqr 방식  
new_df['bmi'].describe()

q1 = 26.22
q3 = 34.6875
iqr = q3 - q1
outlier_step = 1.5 * iqr

minval = q1 - outlier_step 
maxval = q3 + outlier_step  

# 정상범위 : 13.51 ~ 47.38
minval 
maxval 

# 정상범위 subset 만들기 
new_df2 = new_df[(new_df.bmi >= minval) & (new_df.bmi <= maxval)] 
new_df2.shape 

# age, bmi 정상범주 확인 
plt.boxplot(new_df2)
plt.show()

#######################
# Subplot
#######################

fig = plt.figure(figsize = (10, 5))
x1 = fig.add_subplot(2,2,1) 
x2 = fig.add_subplot(2,2,2) 
x3 = fig.add_subplot(2,2,3) 
x4 = fig.add_subplot(2,2,4)

# 2.차트 데이터 생성 
data1 = [random.gauss(mu=0, sigma=1) for i in range(100)] 
data2 = [random.randint(1, 100) for i in range(100)] 
cdata = [random.randint(1, 4) for i in range(100)] 

# 3. 각 격차에 차트 크리기 
x1.hist(data1)
x2.scatter(data1, data2, c=cdata) 
x3.plot(data2) 
x4.plot(data1, data2, 'g--') 

x1.set_title('hist', fontsize=15)
x2.set_title('scatter', fontsize=15)
x3.set_title('default plot', fontsize=15)
x4.set_title('color plot', fontsize=15)

# figure 수준 제목 적용 
fig.suptitle('suptitle title', fontsize=20)
plt.show()

#######################
# Time Series 
#######################
plt.style.use('ggplot') # 차트내 격차 제공 

# 1. data 생성 : 정규분포
data1 = [random.gauss(mu=0.5, sigma=0.3) for i in range(100)] 
data2 = [random.gauss(mu=0.7, sigma=0.2) for i in range(100)] 
data3 = [random.gauss(mu=0.1, sigma=0.9) for i in range(100)]   

# 2. Fugure 객체 
fig = plt.figure(figsize = (12, 5)) 
chart = fig.add_subplot()  # 1개 격자

# 3. plot : 시계열 시각화 
chart.plot(data1, marker='o', color='blue', linestyle='-', label='data1')
chart.plot(data2, marker='+', color='red', linestyle='--', label='data2')
chart.plot(data3, marker='*', color='green', linestyle='-.', label='data3')
plt.title('Line plots : marker, color, linestyle')
plt.xlabel('index')
plt.ylabel('random number')
plt.legend(loc='best')
#plt.show()

# 4.이미지 파일 저장 & 읽기
plt.savefig(r"ts_plot.png") # 이미지 파일 저장 
plt.show()

# 이미지 파일 읽기 
import matplotlib.image as img 

image = img.imread(r"ts_plot.png") # 이미지 파일 읽기 
plt.imshow(image)
image.shape