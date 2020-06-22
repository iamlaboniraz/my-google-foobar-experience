from time import time
strat_time = time()
def answer(s):
    return sum([s[i:].count("<")for i in range(0,len(s)) if s[i] == ">" ])*2
print(answer("--->-><-><-->-"))
end_time = time()
print(end_time-strat_time)


