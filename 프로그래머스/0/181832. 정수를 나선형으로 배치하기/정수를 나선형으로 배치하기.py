def turn_right():
    global sight
    sight += 1
    if sight == 4:
        sight = 0
        
def solution(n):
    global sight
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    sight = 0
    x, y = 0, 0
    d = [[0]*n for _ in range(n)]
    num = 2
    d[0][0] = 1
    
    while True:
        nx = x + dx[sight]
        ny = y + dy[sight]
        
        if 0 <= nx < n and 0 <= ny < n and d[nx][ny] == 0:
            x = nx
            y = ny
            d[nx][ny] = num
            num += 1
            
        else:
            turn_right()
            
        if num == n*n + 1:
            break
        
    
    return d