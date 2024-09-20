while True:
 print("계산하실 문제를 선택하세요")
 print("1.원의 넓이 2.환율 3.마일-미터변경 4.종료")
 number = int(input())
 if number == 1:
    print("원의 넓이: 반지름을 입력해주세요")
    r = float(input(1))
    print((r*r)*3.14)
 elif number == 2:
    print("현재 미국환율을 입력해주세요.")
    moneyrate = float(input())
    print("환전하실 한국돈을 입력해주세요")
    koreanmoney = int(input())
    print("한국돈을 달러로 환전했을 때 전체 금액 출력")
    result = koreanmoney / moneyrate
    print(result)
 elif number == 3:
    print("마일- 미터 변경입니다. 어떻게 변경할까요?")
    print("1. 마일을 미터로    2.미터를 마일로")
    number1 = int(input())
    if number1 ==  1:
        print("몇 마일인지 입력하시오")
        mile = float(input())
        meter = mile*1600
        print(meter)
    elif number1 == 2:
        print("몇 미터인지 입력하시오")
        meter = float(input())
        mile = meter/1600
        print(mile)
 elif number == 4:
    print("프로그램을 종료합니다.")
    break