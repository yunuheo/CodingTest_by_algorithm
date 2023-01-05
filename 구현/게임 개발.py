'''
NxM 크기의 직사각형이 있고, 각각의 칸은 바다 또는 육지이다.
캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은(A,B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.
1~4메뉴얼을 진행시키면서 최종적으로 캐릭터가 방문한 칸의 수를 구하시오.

첫째 줄에 맵의 세로(N)와 가로(M)크기가 주어짐
둘째 줄에 캐릭터가 있는 칸의 좌표(A,B)와 바라보는 방향d가 주어지고, 방향은 0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽
셋째 줄부터 맵이 육지인지 바다인지 입력해야함.
'''

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위해 맵을 생성하여 0으로 초기화 시키자.
d = [[0]*m for _ in range(n)]
#현재 캐릭터의 X좌표, Y좌표, 방향을 입력받자.
x, y, direction = map(int, input().split())
d[x][y] = 1 #입력받은 현재 좌표는 방문 처리.

#전체 맵의 경로를 입력받자.
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 회전
def turn_left():
    global direction # 변수 direction이 함수 밖에서 선언된 전역변수이기 때문에 변수명 앞에 global 을 명시해줘야 함
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
cnt = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
    
print(cnt)
