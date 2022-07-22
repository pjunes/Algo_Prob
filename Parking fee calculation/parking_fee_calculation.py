def solution(fees, records):
    # fees type:list with integer [basic time, basic fee, unit time, unit fee]
    # 1 ≤ fees[0] ≤ 1439, 0 ≤ fees[1] ≤ 100000, 1 ≤ fees[2] ≤ 1439, 1 ≤ fees[3] ≤ 10000

    # records type:list with string ["시각 차량번호 내역", ... ]
    # 1 ≤ len(records) ≤ 1000
    # 시각 HH:MM은 00:00부터 23:59까지
    # 차량번호는 자동차를 구분하기 위한, `0'~'9'로 구성된 길이 4인 문자열
    # 내역은 길이 2 또는 3인 문자열로, IN 또는 OUT

    # 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return
    answer = []  # type:list with integer

    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    access_record = dict() # key serial : value in time
    fee_record = dict() # key serial : value fee
    status_record = dict() # key serial : value in(True)\out(False)

    for record in records: # record type:string "time serial in/out"
        time_s, serial, detail = record.split(' ')
        time = int(time_s[:2]) * 60 + int(time_s[3:]) # conversion "00:00" to 000 minutes (integer)

        if detail == "IN":
            access_record[serial] = time
            status_record[serial] = [True, time]
        else: # if detail == "out":
            unit = max((time - access_record[serial]) - basic_time, 0) / unit_time

            # ceil unit
            if unit%1:
                unit = int(unit) + 1
            else:
                unit = int(unit)

            fee_record[serial] = fee_record.get(serial, 0) + basic_fee + unit * unit_fee
            
            status_record[serial][0] = False

        pass

    for item in status_record.items():
        if item[1][0] == True:
            unit = max(((23*60+59) - item[1][1]) - basic_time, 0) / unit_time

            # ceil unit
            if unit%1:
                unit = int(unit) + 1
            else:
                unit = int(unit)

            fee_record[serial] = fee_record.get(serial, 0) + basic_fee + unit * unit_fee
            
            status_record[serial][0] = False

    fee_record_sorted = sorted(fee_record.items())
    
    for i in range(len(fee_record_sorted)):
        answer.append(fee_record_sorted[i][1])

    return answer

if __name__ == "__main__":
#     a = 2.1
#     b = 2

#     print("a는 ",end="")
#     if (a%1):
#         print("유리수")
#     else:
#         print("정수")

#     print("b는 ",end="")
#     if (b%1):
#         print("유리수")
#     else:
#         print("정수")
#     print(a%1)
#     print(b%1)
    sample_fees = [180, 5000, 10, 600]
    sample_records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    answer = solution(sample_fees, sample_records)
    print(answer)