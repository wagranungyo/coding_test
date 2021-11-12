#1차시도
#def solution(participant, completion):
#    result=list(set(participant)-set(completion))
#    for i in result:
#        return i

# 중복된 사람을 반영을 못함 70점(정확도 3문제, 효율성 4문제)



#2차시도
# from collections import Counter
# def solution(participant, completion):
#     double=participant+completion
#     result= Counter(double)
#     for key,value in result.items():
#         if value >= 3 or value ==1:
#             return(key)

# 문제는 다 맞았으나 제출해보니 10점짜리 (정확도 1문제, 효율성0문제)



#3차시도, 길이 비교를 하여 기존의 것하고 일치하는 것은 그대로 set를 이용해서 해결, 안맞는 부분은 for문 돌려서 각각을 매칭 
#def solution(participant, completion):                        
#    participant_set=list(set(participant)) 
#    if len(participant) == len(participant_set):
#        result=list(set(participant)-set(completion))
#        for i in result:
#            return i 
#    
#    else:                                              
#        for i in participant:
#            for j in completion:
#                if i!=j:
#                    return i

# 문제는 다 맞았느나 제출해보니 또다시 10점짜리(정확도 1문제, 효율성0문제)


#4차시도 zip 사용
# def solution(participant, completion):                        
#     completion.append("자리를 맞추기 위한 요소")
#     participant.sort()
#     completion.sort()
#     for i in zip(participant,completion):
#         if i[0]!=i[1]:
#             return i[0]

#해결했으나 조금 위험함 


#다른 사람의 풀이 카운터에서 객체끼리는 뺄셈이 가능하다. 
#import collections
#def solution(participant, completion):
#    answer = collections.Counter(participant) - collections.Counter(completion)
#    return list(answer.keys())[0]

#제일 간단했음 



