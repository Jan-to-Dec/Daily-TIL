# 함수 - 입력값을 받아 출력 값을 반환하는 코드 모음
# def와 함수 이름, 함수 본문을 이용해 정의내린다

# def function_name(매개변수1, 매개변수2, ...):
#     statement1
#     statement2
#     return 반환값


# 매개변수 - 함수의 입력으로 주어진 값을 저장하는 변수
# 인수 - 함수를 호출할 때 전달하는 입력값

# 덧셈을 수행
def add(a, b):
    result = a + b
    return result 
print(add(3, 4))

# 함수에서 반환값 지정하지 않는 경우
# 함수는 None 값을 반환한다
def print_hello():
    print("Hello, World")
    
print_hello()    

# 튜플을 이용한 함수
def get_stats(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    sum_value = sum(numbers)
    mean_value = sum_value / len(numbers)
    return min_value, max_value, sum_value, mean_value

# 함수 호출
stats = get_stats([1, 2, 3, 4, 5])
print(stats)  
# 반환된 값들을 각각 변수에 저장할 수도 있음
min_val, max_val, total_sum, mean_val = get_stats([1, 2, 3, 4, 5])
print(min_val)    
print(max_val)   
print(total_sum) 
print(mean_val)   

def get_stats(numbers):
    stats = {
        'min': min(numbers),
        'max': max(numbers),
        'sum': sum(numbers),
        'mean': sum(numbers) / len(numbers)
    }
    return stats

# 함수 호출
stats = get_stats([1, 2, 3, 4, 5])
print(stats) 

# 반환된 딕셔너리의 각 값을 가져오려면
print(stats['min'])    
print(stats['max'])   
print(stats['sum'])    
print(stats['mean']) 

# 파이썬에는 이미 구현된 다양한 함수가 제공된다
# abs() - 절댓값을 반환한다
# len() - 길이를 변환한다
# str() - 문자열을 반환한다 


# 람다함수 : 익명 함수를 만들 때 사용한다. 한 줄로 간결하게 표현할 수 있다. 

# List Comprehension
# 기본 구조 : 표현식 + for문
# result = [표현식 for 변수 in 리스트]

# 표현식 + for문 + 조건문
# result = [표현식 for 변수 in 리스트 조건문]

# 조건문 + for문
# result = [조건문 for 변수 in 리스트]

# 중첩 for문
# result = [조건문 for 변수1 in 리스트1 for 변수2 in 리스트2 ...]

# 0부터 9까지의 정수 리스트 생성
a = [i for i in range(10)]
print(a)


# 0부터 9까지의 정수 중 짝수 리스트 생성
b = [i for i in range(10) if i % 2 == 0]
print(b)

# range() - 연속된 숫자의 시퀀스를 생성한다
# range(start, stop, step)

for i in range(1, 10, 2):
    print(i)

# pass() - 아무 것도 하지 않고 넘어갈 때 사용한다. 
# 문법적으로 문장이 필요하지만 프로그램이 특별히 할 일이 없을 때

def my_function():
    pass

# continue() - 반복문에서 사용한다

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

# break() - 반복문을 중단하고 루프에서 벗어난다

while True:
    user_input = input("Type 'quit' to exit: ")
    if user_input == 'quit':
        break
    print("You typed:", user_input)

