'''
숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 
이때 N은 행의 개수, M은 열의 개수를 의미한다.
먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
그다음 선택된 행에 포함된 카드들 중 가장 숫자가 작은 카드를 뽑아야 한다.
위에 제한 사항을 만족하는 카드 중 가장 큰 숫자가 쓰인 카드를 선택하여라.
'''
n, m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int, input().split()))
    n_min = min(arr)
    result = max(result,n_min)

print(result)
