# 제어문 If

# if 조건:
#     # 조건이 참일 때 실행될 코드 블록
#     statement1
#     statement2
#     ...
# elif 다른조건:  # 선택사항, 여러개의 조건을 사용할수 있습니다.
#     # 다른 조건이 참일 때 실행될 코드 블록
#     

# 조건이 여러개일 때 
x = 10
y = 5

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")

# 리스트에서 특정 값
numbers = [1, 2, 3, 4, 5]
searched_n = 3

if searched_n in numbers:
    print(f"{searched_n} is found in the list.")
else:
    print(f"{searched_n} is not found in the list.")


# 제어문 For 

# for 요소 in 순회할_자료구조:
#     # 반복 실행할 코드 블록
#     statement1
#     statement2
#     ...

fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)


# 글자세기
word = "Python"

count = 0
for char in word:
    count += 1

print(f"The word '{word}' has {count} characters.")

# 범위 반복
for i in range(5):
    print(i)

# 제어문 while - 조건이 True인 동안 반복적으로 코드 블록을 실행한다

count = 0

while count < 5:
    print(f"Count is {count}")
    count += 1

