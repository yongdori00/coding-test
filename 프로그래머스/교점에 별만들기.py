def solution(line):
    answer = []
    loclist = []
    
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    isfirst = True

    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            if line[i][0]*line[j][1] - line[i][1]*line[j][0] != 0:
                sonx = (line[i][1]*line[j][2] - line[i][2]*line[j][1])
                sony = (line[i][2]*line[j][0] - line[i][0]*line[j][2])
                mom = (line[i][0]*line[j][1] - line[i][1]*line[j][0])
                if sonx % mom == 0 and sony % mom == 0:
                    x = sonx // mom
                    y = sony // mom
                    loclist.append([x, y])

                    if isfirst:
                        minx = x
                        maxx = x
                        miny = y
                        maxy = y
                        isfirst = False

                    if minx > x:
                        minx = x
                    if maxx < x:
                        maxx = x
                    if miny > y:
                        miny = y
                    if maxy < y:
                        maxy = y

    stringlist = ['.' for i in range((int)(maxx-minx)+1)]
    tempanswer = [list(stringlist) for i in range((int)(maxy-miny)+1)]
    #여기서 list(stringlist)가 아니라 그냥 stringlist했다가
    for loc in loclist:
        tempanswer[maxy-loc[1]][loc[0]-minx] = '*'
    #여기서 *찍은게 모든 행들에 다 들어가서 한참 걸림
    #꼭 참조가 아니라 복사를 할 것.

    for ansstring in tempanswer:
        answer.append(''.join(ansstring))

    #print(answer)

    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])