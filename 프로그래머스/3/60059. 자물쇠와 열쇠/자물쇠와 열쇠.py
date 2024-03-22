def turn_right(key):
    
    n = len(key)
    rotated = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = key[i][j]
            
    return rotated

def check(new_lock):
    n = len(new_lock)//3
    
    for i in range(n,n*2):
        for j in range(n,n*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        key = turn_right(key)
        for i in range(2*n):
            for j in range(2*n):
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]

                if check(new_lock):
                    return True

                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y]
            
      
    return False