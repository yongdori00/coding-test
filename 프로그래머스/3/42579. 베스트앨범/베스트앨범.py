#정렬과 인덱스를 포함한 정렬로 풀이
def solution(genres, plays):
    answer = []
    
    list_gp = []
    
    dict_sum = {}
    list_dict = []
    
    #장르만 정리
    genre = []
    
    #(장르, 재생횟수, 인덱스)를 하나의 요소로 리스트 생성
    for i in range(len(plays)):
        list_gp.append((genres[i], plays[i], i))
    
    #장르별 총 재생 수 dict 생성
    for i in range(len(genres)):
        dict_sum[genres[i]] = dict_sum.get(genres[i], 0) + plays[i]
    
    #사용하기 쉽게 dict -> list
    for key, value in dict_sum.items():
        list_dict.append((key, value))
        
    #모든 list_gp를 재생수의 내림차순으로 정렬(2번 조건을 위해서)
    #장르 내에서는 고유 번호가 낮은 노래 먼저 수록 때문에 -x[2]라는 조건도 추가(3번 조건을 위해서)
    list_gp.sort(key = lambda x : (x[1], -x[2]), reverse = True)
    #전체 재생 순서 내림차순 정렬(1번 조건을 위해서)
    list_dict.sort(key = lambda x : x[1], reverse = True)
    
    #각 장르에 대한 전체 재생횟수의 내림차순 중 장르만 추출
    for i in range(len(list_dict)):
        genre.append(list_dict[i][0])
        i += 1
        
    for j in range(len(list_dict)):
        num = 0
        index = 0
        #장르를 두 번 뽑았거나 인덱스 끝까지 갔으면 끝
        while num < 2 and index < len(list_gp):
            #1번 조건의 장르를 만난 경우 정답에 추가
            if list_gp[index][0] == genre[j]:
                answer.append(list_gp[index][2])
                num += 1
            index += 1

    return answer