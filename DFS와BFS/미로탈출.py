'''
N X M 크기의 직사각형 미로가 있다. (1,1)부터 시작하고 (N,M)의 위치에 출구가 존재한다.
0으로된 부분은 갈 수 없고 1로 표시된 부분만 이동 가능하다. 한번에 한 칸씩 움직일 수 있다.
이 때 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라.
'''
from collections import deque

n, m = map(int,input().split())
#2차원 리스트에 맵 정보를 입력받자.
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#이동할 네 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#BFS 구현
def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #공백큐가 될 때까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    #가장 오른쪽 아래의 최단거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))