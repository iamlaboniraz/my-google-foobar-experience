def answer2(n):
    number = int(n)
    x = []
    while (number != 1):
        if number%2 == 0:
            number = number // 2
        elif (number==3) or (number-1)%4 == 0:
            number-= 1
        else:
            number += 1
        x.append(number)
    return len(x)
print(answer2("15"))
