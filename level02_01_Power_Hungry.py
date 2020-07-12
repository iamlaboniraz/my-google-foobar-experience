from time import time
from operator import mul
from functools import reduce
start_time = time()
def solution(xs):
    # Your code here
    length1 = len(xs)
    length2 = len([i for i in xs if i<0])
    count_zero = xs.count(0)
    if count_zero == length1:
        return str(0)
    if length1 and length2 == 1:
        return (str(xs[0]))
    if length2 == 1 and  count_zero == length1-1:
        return str(0)
    negative_value = []
    positive_value = []    
    negative_value,positive_value = (sorted([i for i in xs if i<0])),([i for i in xs if i>0])
    if (len(negative_value)%2) != 0:
        negative_value.pop()
    return str(reduce(mul,(positive_value+negative_value)))
xs = [int(x) for x in input().split()]
print(solution(xs))
end_time = time()
print(f''' Required time {end_time-start_time} ''')


        

