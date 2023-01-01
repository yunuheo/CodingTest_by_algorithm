n, m, k = map(int, input().split())
data = list(map(int, input().split()))
'''
다양한 수들로 이루어진 배열이 있을 때 M번 더하여
가장 큰 수를 만들어야 한다. 단, 배열의 특정한 인덱스에 해당하는 수가
연속해서 K번을 초과하여 더해질 수 없다.

'''
data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #가장 작은 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second #두 번째로 큰 수 한 번 더하기
    m -= 1

print(result)
