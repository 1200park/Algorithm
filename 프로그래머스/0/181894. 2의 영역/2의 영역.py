def solution(arr):
    answer = []
    try:
        a = arr.index(2)
        rev = arr[::-1]
        b = len(arr) - rev.index(2)

        return arr[a:b]
    except: 
        return [-1]