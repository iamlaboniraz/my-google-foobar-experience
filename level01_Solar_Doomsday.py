import math
def solution(area):
    area_store = area
    final_array_list =[]
    while area>0:
        sqrt_calculate = math.sqrt(area_store)
        if sqrt_calculate == int(sqrt_calculate):
            final_array_list.append(area_store)
            area -= area_store
            area_store=area
            #print(area_store)
            continue
        area_store-=1
    return final_array_list

area = int(input())
x = solution(area)
print(x)
