'''
8x8 좌표평면의 체스판이 있다. 나이트는 아래의 2가지 경우로 이동한다.
1. 수평으로 두 칸 이동 후 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동 후 수평으로 한 칸 이동하기
단, 체스판 밖으로 이동할 수 없음 (=경우의 수로 세지 않음.)

나이트가 이동할 수 있는 경우의 수를 구하시오.
'''

data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1 # 열의 문자를 아스키코드로 변환한 뒤 , a의 아스키 코드를 빼고 1을 더해줌 (= 'a'가 1에 대응되게 구현됨)
#나이트가 이동할 수 있는 8가지 방향
steps = [(-2,-1),(-1,-2),(1, -2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

cnt = 0
for step in steps:
    next_row = row + step[1]
    next_col = col + step[0]
    #해당 위치로 이동이 가능하면 카운트(cnt) 증가
    if next_row >= 1  and next_row <= 8 and next_col >= 1 and next_col <= 8:
        cnt += 1

print(cnt)