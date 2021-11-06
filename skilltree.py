import re

def solution(skill, skill_trees):
    answer = 0
    number = 1
    index = 0
    
    nonskill = '[^' + skill + ']'
    
    for i in range(len(skill_trees)):
        skill_trees[i] = re.sub(nonskill, '', skill_trees[i])

    print(skill_trees)

    for i in range(len(skill_trees)):
        number = 1
        index = 0
        while index < len(skill_trees[i]):
            if skill[index] != skill_trees[i][index]:
                number = 0
                break
            index += 1
        answer += number

    
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))