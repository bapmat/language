# # 숫자형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# # 문자형
# print('풍선')
# print("나비")
# print('ㅋ'*8)

# # 참, 거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# 리스트
# subway = [10, 20, 30]
# print(subway)

subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호가 몇 번째 칸에 타고 있는가
# print(subway.index("조세호"))

# # 다음 정류장에서 하하가 탐
# subway.append("하하")   # 리스트 뒤에 추가됨
# print(subway)

# # 정형돈을 유재석 / 조세호 사이에 추가
# subway.insert(1, "정형돈")
# print(subway)

# # 뒤에서부터 한명씩 꺼냄
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지
#subway.append("유재석") 
#print(subway.count("유재석"))

# 정렬
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형과 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)