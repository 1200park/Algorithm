import math

num = int(input())
arr = list(map(int, input().split()))
boo = [True for _ in range(num)]

for i in range(num):
    if arr[i] == 1 or arr[i] == 0:  # 1은 소수가 아니므로 바로 처리합니다.
        boo[i] = False
    elif arr[i] == 2:  # 2는 소수이므로 바로 처리합니다.
        continue
    else:
        for j in range(2, int(math.sqrt(arr[i])) + 1):
            if arr[i] % j == 0:
                boo[i] = False
                break
count = boo.count(True)
print(count)




        