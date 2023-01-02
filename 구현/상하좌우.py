n = int(input())
#처음위치 = (1,1)
#L, R, U, D로 움직임
#영역 밖으로 움직이면 무시

plan = input().split()

x = 1
y = 1

for i in plan:
    if i == 'R':
        x += 1
        if x > n:
            x -= 1
    elif i == 'L':
        x -= 1
        if x < 1:
            x += 1
    elif i == 'U':
        y -= 1
        if y < 1:
            y += 1
    elif i == 'D':
        y += 1
        if y > n:
            y -= 1

print(y,x)

'''
<교재 풀이>
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        #공간을 벗어나면 무시
        if nx< 1 or ny < 1 or nx > n or ny >n:
            continue
        #이동 수행
        x, y = nx, ny

print(x,y)
'''

