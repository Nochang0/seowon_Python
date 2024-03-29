# 295P

board = [[' ' for x in range(3)] for y in range(3)]

while True:
    # 게임 보드를 그린다.
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "|  " + board[r][2])
        if(r != 2):
            print("---|---|---")
            
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))
    
    
    # 사용자가 입력한 좌표를 검사한다.
    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = 'X'
        
    # 컴퓨터가 놓을 위치를 결정한다.
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 0;
                done=True
                break;