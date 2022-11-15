# 문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 =  """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


# 슬라이싱
# jumin = "891023-1234567"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2])
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[0:6])
# print("생년월일 : " + jumin[:6])    # 처음부터 6 직전까지

# print("뒤 7자리 : " + jumin[7:14])
# print("뒤 7자리 : " + jumin[7:])    # 7 부터 끝까지
# print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지


# 문자열 포맷
# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")   # 한글자만 받는다
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# # 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))

# # 방법 4 (v.3.6이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자 
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
print("저는 '나도코딩'입니다.")     # 밖에 큰따옴표, 안에 작은따옴표
print('저는 "나도코딩"입니다.')     # 밖에 작은따옴표 안에 큰따옴표
print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 \
print("D:\\Projects\\Python")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")