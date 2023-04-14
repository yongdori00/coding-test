import math

def solution(fees, records):
    answer = []
    splited_records = []
    in_records = {}
    money_records = {}
    time_records = {}
    
    for info in records:
        splited_records.append(info.split())
        
    for io in splited_records:
        time_str = io[0].split(":")
        time = int(time_str[0]) * 60 + int(time_str[1])
        if io[2] == "IN":
            in_records[io[1]] = time
        elif io[2] == "OUT":
            period = time - in_records[io[1]]
            time_records[io[1]] = time_records.get(io[1], 0) + period
            in_records.pop(io[1])
    
    end_time = 23 * 60 + 59
    for num, in_time in in_records.items():
        period = end_time - in_time
        time_records[num] = time_records.get(num, 0) + period
        
    for num, in_time in time_records.items():
        if in_time <= fees[0]:
            money_records[num] = fees[1]
        elif in_time > fees[0]:
            in_time -= fees[0]
            money_records[num] = money_records.get(num, 0) + math.ceil(in_time / fees[2]) * fees[3] + fees[1]
        # in_records.pop(num)
    
    # money_records = list(money_records)
    
    money_records_list = sorted(money_records.items(), key = lambda x : (x[0]))
    
    for i in money_records_list:
        answer.append(i[1])
    
    return answer