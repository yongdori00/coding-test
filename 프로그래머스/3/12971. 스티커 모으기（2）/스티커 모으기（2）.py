def solution(sticker):
    answer = 0

    if len(sticker) == 1:
        return sticker[0]
    
    len_popped = len(sticker) - 1
    
    dp_first = [0 for i in range(len_popped)]
    dp_last = [0 for i in range(len_popped)]
    
    dp_first[0] = sticker[0]
    dp_last[0] = sticker[1]
    
    for i in range(1, len(sticker) - 1):
        if i == 1:
            if sticker[i] > dp_first[i - 1]:
                dp_first[i] = sticker[i]
            else:
                dp_first[i] = dp_first[i - 1]
        else:
            if sticker[i] + dp_first[i - 2] > dp_first[i - 1]:
                dp_first[i] = sticker[i] + dp_first[i - 2]
            else:
                dp_first[i] = dp_first[i - 1]
            # print(dp_first)
                
    for i in range(2, len(sticker)):
        if i == 2:
            if sticker[i] > dp_last[i - 1 - 1]:
                dp_last[i - 1] = sticker[i]
            else:
                dp_last[i - 1] = dp_last[i - 1 - 1]
        else:
            if sticker[i] + dp_last[i - 2 - 1] > dp_last[i - 1 - 1]:
                dp_last[i - 1] = sticker[i] + dp_last[i - 2 - 1]
            else:
                dp_last[i - 1] = dp_last[i - 1 - 1]
            # print(dp_last)
    
    if dp_first[len_popped - 1] > dp_last[len_popped - 1]:
        return dp_first[len_popped - 1]
    else:
        return dp_last[len_popped - 1]