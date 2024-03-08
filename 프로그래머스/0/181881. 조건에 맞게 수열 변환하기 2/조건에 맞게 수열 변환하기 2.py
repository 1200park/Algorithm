def solution(arr):
    answer = 0
    bef = arr
    while True:
        aft = []
        for i in bef:
            if i >= 50 and i%2 == 0:
                aft.append(i/2)
            elif i < 50 and i%2 == 1:
                aft.append(i*2+1)
            else:
                aft.append(i)
        if bef == aft:
            break
        else:
            bef = aft
            answer += 1
    return answer