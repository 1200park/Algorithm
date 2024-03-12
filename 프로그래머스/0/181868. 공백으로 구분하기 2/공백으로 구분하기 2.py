import re
def solution(my_string):
    answer = re.split(r'\s+', my_string.strip())
    return answer