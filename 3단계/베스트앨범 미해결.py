def solution(genres, plays):
    answer = []

    dict_genres = {}

    for i in range(len(genres)):
        dict_genres[genres[i]] = dict_genres.get(genres[i], list()) + [(i, plays[i])]

    for key, value in dict_genres.items():
        dict_genres[key] = sorted(dict_genres[key], key = lambda x:(x[1], -x[0]), reverse = True)

    print(dict_genres)

    dict_genres = dict(sorted(dict_genres.items(), key = lambda x:x[1][1], reverse = True))

    print(dict_genres)

    for key, value in dict_genres.items():
        for i in range(2):
            answer.append(value[i][0])

    return answer

print(solution(["classic", "aop", "classic", "classic", "aop"], [500, 600, 150, 800, 2500]))
