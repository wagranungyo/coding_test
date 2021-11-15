###1차시도 순열이라고 생각하여 접근 

import itertools

def solution(numbers):
    answer=[]
    com=list(itertools.permutations(numbers,len(numbers)))
    for i in com:
        list_com=list(i)
        numbers_str = list(map(str, list_com))
        answer.append(''.join(numbers_str))
    return max(answer)

### 테스트 케이스는 통과하였으나 테스트1~11 시간초과로 실패함 시간을 줄일 수 있는 방안 생각하기!     