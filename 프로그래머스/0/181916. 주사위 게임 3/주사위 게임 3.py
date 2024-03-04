from collections import Counter

def solution(a, b, c, d):
    answer = 0
    arg = [a,b,c,d]
    counter = Counter(arg)
    most_counter = counter.most_common()
    
    if a == b == c == d:
        answer = 1111*a
    elif (a==b==c) or (a==b==d) or (a==c==d) or (b==c==d):
        p=most_counter[0][0]
        q=most_counter[-1][0]
        answer = (10*p+q)**2
    elif (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
        p=most_counter[0][0]
        q=most_counter[-1][0]
        answer = (p+q) * abs(p-q)
    elif (a==b) or (a==c) or (a==d) or (b==c) or (b==d) or (c==d):
        p=most_counter[0][0]
        q=most_counter[-1][0]
        r=most_counter[-2][0]
        answer = q*r
    else:
        answer = min(a,b,c,d)
    return answer