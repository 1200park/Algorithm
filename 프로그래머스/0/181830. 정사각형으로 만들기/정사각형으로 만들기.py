def solution(arr):
    if len(arr) == len(arr[0]):
        return arr
    
    if len(arr) > len(arr[0]):
        count = len(arr) - len(arr[0])
        for idx in arr:
            idx += [0] * count
        return arr
    else:
        count = len(arr[0]) - len(arr)
        new_list = [0 for _ in range(len(arr[0]))]
        for i in range(count):
            arr.append(new_list)
        return arr