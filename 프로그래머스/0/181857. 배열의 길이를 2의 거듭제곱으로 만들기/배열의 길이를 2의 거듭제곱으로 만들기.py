def solution(arr):
    arg = [1,2,4,8,16,32,64,128,256,512,1024]
    for i in arg:
        if len(arr) <= i:
            idx = i
            break
    while len(arr) < idx:
        arr.append(0)
    return arr