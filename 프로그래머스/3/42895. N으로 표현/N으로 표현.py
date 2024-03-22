def solution(N, number):
    if N == number:
        return 1
    
    b = [{}, {N}]
    
    for num in range(2, 9):
        current_set = {int(str(N) * num)}
        
        for i in range(1, num):
            for x in b[i]:
                for y in b[num - i]:
                    current_set.add(x + y)
                    current_set.add(x - y)
                    current_set.add(x * y)
                    if y != 0:
                        current_set.add(x // y)
        
        if number in current_set:
            return num
        
        b.append(current_set)
    
    return -1