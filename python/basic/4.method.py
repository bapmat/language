# # 숫자 처리 함수
# print(abs(-5))
# print(pow(4, 2)) #4^2
# print(max(5, 12)) # 입력값 중 최대값
# print(min(5, 12)) # 입력값 중 최소값
# print(round(3.14))
# print(round(4.99))

# # 랜덤함수
# from random import *
# print(random()) # 0.0~1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0~1.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 1~10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1~10 이하의 임의의 값 생성

# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값 생성
# print(randrange(1, 45)) # 1~46 미만의 임의의 값 생성
# print(randint(1, 45)) # 1~45 이하의 임의의 값 생성

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 첫번째 글자가 대문자인지
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 첫번째 찾고 난 다음 글자부터 다음 거 찾음
print(index)

print(python.find("n"))
print(python.find("Java"))  # 원하는 값이 없으면 -1
#print(python.index("Java")) # 원하는 값이 없으면 에러남

print(python.count("n"))