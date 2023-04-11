def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_split = []
    reported = {}

    report_set = set(report)
    #같은 사람이 신고하는걸 제거

    for i in report_set:
        report_split.append(i.split())
    #신고한 사람과 신고 당한 사람 분리

    for key in report_split:
        reported[key[1]] = reported.get(key[1], 0) + 1
    #신고 받은 사람을 기준으로 딕셔너리로 값 생성

    reported = {key:value for key, value in reported.items() if value >= k}
    #k 이하의 신고 받은 사람은 삭제

    for i in report_split:
        if i[1] in reported.keys():
            answer[id_list.index(i[0])] += 1
    #k 이상의 신고를 받은 사람의 이름을 report_split에서 1번쨰로 가지고 있는 사람에게 1씩 증가

    return answer

solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)