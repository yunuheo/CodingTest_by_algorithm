'''
N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재한는 부분은 1로
표시된다. 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음틀의 모양이 주어 졌을 때 생성되는 총 아이스크림의 개수를 구하라.
'''
#N, M을 공백으로 구분하여 입력받는다.
n, m = map(int, input().split())

#2차원 리스트에 맵의 정보를 입력받는다.
graph = []
for i in range(n):
    graph.append(list(map(int,input())))


#DFS로 특정한 노드를 방문하고 상,하,좌,우에 연결된 모든 노드들도 방문한다.
def dfs(x, y):
    #주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

#모든 노드에 대하여 dfs() 실행
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)