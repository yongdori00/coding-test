def solution(m, musicinfos):
    answer = '(None)'
    splitedByComma = []
    temptime = []
    songlen = 0
    answerlen = -1
    mulLength = 0

    for i in range(len(musicinfos)):
        splitedByComma.append(musicinfos[i].split(','))
        temptime = (splitedByComma[i][0].split(':'))
        temptime.extend(splitedByComma[i][1].split(':'))
        songlen = (int(temptime[3]) + int(temptime[2]) * 60 - int(temptime[1]) - 60 * int(temptime[0]))

        scaleList = []
        k = 0
        index = 0
        mulLength = len(splitedByComma[i][3]) - splitedByComma[i][3].count('#')
        while k < songlen:
            scale = splitedByComma[i][3][k%mulLength]
            mscale = m[index]
            if(k + 1 < len(splitedByComma[i][3]) and splitedByComma[i][3][k%mulLength+1] == '#'):
                scale += '#'
                k+=1
            if(index + 1 < len(m) and m[index+1] == '#'):
                mscale += '#'
                index += 1
            if(mscale == scale):
                index += 1
            else:
                index = 0

            if index == len(m) and answerlen < songlen:
                answer = splitedByComma[i][2]
                answerlen = songlen
                break
            elif index == len(m):
                break
            k+=1

    return answer
    
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))