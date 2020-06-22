from time import time
start = time()
def solution(l):
    count,length = 0,len(l)
    list_ = [count]*length
    if length<3:
        return 0
    if sum(l)==3:
        return 1
    for i in range(length):
        for j in range(i):
            if l[i]%l[j]!=0:
                continue
            count += list_[j]
        #print("x = ",list_)
        for k in range(i):
            if l[i]%l[k]==0:
                list_[i]+=1
        #print("y = ",list_)
    if count == 0:
        return 0
    else:
        return count
print(solution([1,2,3,4,5,6]))

end = time()
print(end-start)



