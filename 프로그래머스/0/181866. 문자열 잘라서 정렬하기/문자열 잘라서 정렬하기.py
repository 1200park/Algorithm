def solution(myString):
    myString = myString.split("x")
    answer = [i for i in myString if len(i)>0]
    answer.sort()
    return answer