def Search(search,map):
    LRUD = []
    q = []
    Dictionary = {}
    q.append(search)
    string = str(search[0])+','+str(search[1])
    Dictionary[string]=1
    while(0<len(q)):
        present = q.pop(0)
        LRUD.append([present[0]-1,present[1]])
        LRUD.append([present[0]+1,present[1]])
        LRUD.append([present[0],present[1]+1])
        LRUD.append([present[0],present[1]-1])
        for i in LRUD:
            string1 = str(i[0])+','+str(i[1])
            string2 = str(present[0])+','+str(present[1])
            if i[0]<0 or i[1]<0 or i[0]>len(map)-1 or i[1]>len(map[0])-1:
                continue
            if string1 not in Dictionary:
                if map[i[0]][i[1]] == 0:
                    q.append(i)
                    Dictionary[string1] = Dictionary[string2]+1
    return Dictionary
def Find(i,map):
    list_ = []
    integer = i.split(",")
    node = [int(integer[0]),int(integer[1])]
    L = str(node[0]-1)+','+str(node[1])
    if L in map:
        list_.append(map[L])
    R = str(node[0]+1)+','+str(node[1])
    if R in map:
            list_.append(map[R])
    U = str(node[0])+','+str(node[1]+1)
    if U in map:
        list_.append(map[U])
    D = str(node[0])+','+str(node[1]-1)
    if D in map:
        list_.append(map[D])
    if len(list_) == 0:
        return
    else:
        return min(list_)
def solution(map):
    # Your code here
    MinimumPath = []
    length1,length2 = len(map),len(map[0])
    Allwall = []
    starting = Search([0,0],map)
    ending = Search([length1-1, length2-1],map)
    for i in range(0,length1):
        for j in range(0,length2):
            if map[i][j] == 1:
                Allwall.append((str(i)+','+str(j)))
    for i in Allwall:
        start,end = Find(i,starting),Find(i,ending)
        if start and end:
            MinimumPath.append(start + end)
    return min(MinimumPath)+1
map = [[0,1,1],
        [1,0,0],
        [1,0,0]]
print(solution(map))

