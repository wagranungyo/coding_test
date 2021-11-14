# 1차시도
# 계획
# 1.2차원리스트에서 숫자를 받아와서 array의 리스트 숫자 슬라이싱
# 2.정렬
# 3.commands의 3번째 숫자를 인덱스로 받아서 슬라이싱한 리스트에 해당값 출력 후 answer에 추가 


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        slice=array[commands[i][0]-1:commands[i][1]]
        slice.sort()
        answer.append(slice[commands[i][2]-1])
        
    return answer

#다른 사람의 풀이      
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#기본적으로 for문은 그냥 리스트 컴프리핸션을 쓰는 듯    