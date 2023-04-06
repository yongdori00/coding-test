import copy

T = int(input())

que_list = []
answer_list = []

def dfs(reversed, biggest, cards, index, cur_cnt, cnt, remain):
    if reversed == biggest:
        remain = cnt - cur_cnt
        return biggest, remain
    if cur_cnt >= cnt:
        return biggest, remain
    cur_cnt += 1

    for i in range(len(cards)):
        shuffled_cards = copy.deepcopy(cards)
        if i == index:
            continue

        temp = shuffled_cards[i]
        shuffled_cards[i] = shuffled_cards[index]
        shuffled_cards[index] = temp

        print(shuffled_cards)

        if biggest < int(''.join(shuffled_cards)):
            biggest = int(''.join(shuffled_cards))

        biggest, remain = dfs(reversed, biggest, shuffled_cards, i, cur_cnt, cnt, remain)

        if reversed == biggest:
            remain = cnt - cur_cnt
            return biggest, remain

    return biggest, remain

for i in range(T):
    biggest, cnt = map(str, input().split())
    cards = list(biggest)
    cnt = int(cnt)

    reversed = int(''.join(sorted(cards, reverse=True)))

    answer, remain = dfs(reversed, int(biggest), cards, 0, 0, cnt, 0)

    if answer == reversed:
        if remain % 2 == 1:
            answer = list(str(answer))
            temp = answer[-1]
            answer[-1] = answer[-2]
            answer[-2] = temp
            answer = int(''.join(answer))
            print(answer, remain, "hi")

    answer_list.append(answer)

for i in range(len(answer_list)):
    print('#' + str(i+1) + ' ' + str(answer_list[i]))