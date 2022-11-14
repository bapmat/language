# 그리디 알고리즘 -> 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# 거스름돈 : 큰 단위의 화폐가 작은 단위의 배수이므로 큰 단위부터 처리한다.
n = 1260
count = 0

# 큰 단위 화폐부터 차례대로 확인
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전 갯수 세기
    n %= coin
    print(coin)
    print(n, end='\n\n') # 줄바꿈
print(count)


# 1이 될 때까지
