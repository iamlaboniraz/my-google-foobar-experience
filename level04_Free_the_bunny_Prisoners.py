from itertools import combinations
def solution(num_buns, num_required):
    # Your code here
    AllKey = []
    com = list(combinations(range(0,num_buns),num_buns-num_required+1))
    for i in range(0,num_buns):
        AllKey.append([])
    key = 0
    for value in com:
        [AllKey[j].append(key) for j in value]
        key+=1
    return AllKey
print(solution(5,3))
#print(solution(5,2))
#print(solution(4,4))
#print(solution(2,1))
#print(solution(3,2))
#print(solution(3,1))
