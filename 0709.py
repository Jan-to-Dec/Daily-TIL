# Dictionary function
# 딕셔너리명[키] 로  값을 출력할 수 있다

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