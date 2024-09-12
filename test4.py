money = 0

while True:
    print("음료종류 출력")
    print("1.콜라(500) 2.사이다(400) 3.오로나민씨(600) 4.밀키스(700) 5.종료")

    print("금액을 입력하세요")
    money += int(input()) #돈을 더 안넣으면 됨.5

    print("음료를 선택해주세요.")
    cho = int(input())
    if cho == 1:
        if money >= 500:
            money = money - 500
            print("남은돈은" + str(money) + "입니다")
            print("계속 더 고르시겠습니까?y/n")
            rep = input()
            if rep == "y":
                continue
            elif rep =="n":
                break
        elif money < 500:
            print("금액이 부족합니다.")
            break
    elif cho == 2:
        if money >= 400:
            money = money - 400
            print("남은돈은"+str(money)+"입니다")
            print("계속 더 고르시겠습니까?y/n")
            rep = input()
            if rep == "y":
                continue
            elif rep == "n":
                break
        elif money < 400:
            print("금액이 부족합니다.")
            break
    elif cho == 3:
        if money >= 600:
            money = money - 600
            print("남은돈은"+str(money)+"입니다")
            print("계속 더 고르시겠습니까?y/n")
            rep = input()
            if rep == "y":
                continue
            elif rep == "n":
                break
        elif money < 600:
            print("금액이 부족합니다.")
            break
    elif cho == 4:
        if money >= 700:
            money = money - 700
            print("남은돈은"+str(money)+"입니다")
            print("계속 더 고르시겠습니까?y/n")
            rep = input()
            if rep == "y":
                continue
            elif rep == "n":
                break
        elif money < 700:
            print("금액이 부족합니다.")
            break
    elif cho == 5:
        print("프로그램을 종료합니다.")
        break
