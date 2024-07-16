# Dictionary function
# 딕셔너리명[키] 로  값을 출력할 수 있다
#%%
# 딕셔너리 생성
contact_info = {
		"Alice": "555-1234", 
		"Bob": "555-5678"
}
print(contact_info)  # {"Alice": "555-1234", "Bob": "555-5678"}

# 딕셔너리에 새로운 키-값 쌍 추가
contact_info["Charlie"] = "555-8765"
print(contact_info)  # {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-8765"}

# 딕셔너리에 또 다른 키-값 쌍 추가
contact_info["Diana"] = "555-4321"
print(contact_info)  # {"Alice": "555-1234", "Bob": "555-5678", "Charlie": "555-8765", "Diana": "555-4321"}

#%%
# 딕셔너리 생성
student_grades = {
    "John": "A",
    "Emily": "B"
}
print(student_grades)  # {"John": "A", "Emily": "B"}

# 딕셔너리에 새로운 키-값 쌍 추가
student_grades["Michael"] = "A-"
print(student_grades)  # {"John": "A", "Emily": "B", "Michael": "A-"}

# 딕셔너리에 또 다른 키-값 쌍 추가
student_grades["Sophia"] = "B+"
print(student_grades)  # {"John": "A", "Emily": "B", "Michael": "A-", "Sophia": "B+"}

#항목 제거할 때 딕셔너리명.pop(키)
# pop() 은 엄밀히 말하면 딕셔너리에서 항목을 제거하는 것이 아니라 꺼내는 것


#%%
# f-string으로 문자열 안에서 변수값 사용하기
name = "JongHun"
job = "Data Analyst"

print(f"안녕하세요. 저는 {name}입니다. 직업은 {job}입니다.")
