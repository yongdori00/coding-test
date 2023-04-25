def solution(genres, plays):
    answer = []
    
    list_gp = []
    
    dict_sum = {}
    list_dict = []
    
    for i in range(len(plays)):
        list_gp.append((genres[i], plays[i], i))
    
    for i in range(len(genres)):
        dict_sum[genres[i]] = dict_sum.get(genres[i], 0) + plays[i]
    
    for key, value in dict_sum.items():
        list_dict.append((key, value))
        
    list_gp.sort(key = lambda x : (x[1], -x[2]), reverse = True)
    list_dict.sort(key = lambda x : x[1], reverse = True)
    
    genre = []
    
    i = 0
    
    print(list_dict, genre, list_gp)
    
    while i < len(list_dict):
        genre.append(list_dict[i][0])
        i += 1
        
    for j in range(len(list_dict)):
        num = 0
        index = 0
        while num < 2 and index < len(list_gp):
            if list_gp[index][0] == genre[j]:
                answer.append(list_gp[index][2])
                num += 1
            index += 1

    return answer