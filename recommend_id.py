import re

def solution(new_id):
    answer = ''
    length = 0
    #reststr
    
    new_id = new_id.lower()
    
    new_id = re.sub('[^a-z0-9._-]', '', new_id)
    new_id = re.sub('([.]{2,})', '.', new_id)
    new_id = new_id.strip('.')

    if new_id == "":
        new_id = 'a'

    answer = new_id[:15]
    new_id = answer.rstrip('.')

    length = len(new_id)
    if length <= 2:
        new_string = []
        new_string.append(new_id)
        while len(new_id) < 3:
            new_string.append(new_id[length - 1])
            new_id = ''.join(new_string)

    answer = new_id

    return answer

if __name__ == '__main__':
    print(solution("123_.def"))