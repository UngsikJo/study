#def sumcalc(a, b):
    #print(a+b)

#sumcalc(5, 6)

#def minuscalc(c,d):
   # res= c-d
    #return res

#minuscalc(10, 5) #리턴이 있는 함수의 경우
#함수자체를 return 으 값인 res로 봐도 무방


#def calc(num1 , num2, op):
 #   if op == '+':
  #      print(num1 + num2)
   # elif op =='-':
    #    print(num1 - num2)
    #elif op =='x':
     #   print(num1 * num2)

#calc(10, 5, 'x')

#def calc_area(type, a, b, c= None):
 #   if type == 1:
  #      result = a*b
   #     msg = '사각형'
    #elif type == 2:
     #   result = a*b/2
      #  msg = '삼각형'
    #elif type == 3:
     #   result = (a+b)*c/2
      #  msg = '평행사변형'
    #return result, msg

#def say():
    #print('넓이를 구해요')
#def write(result, msg):
    #print(msg, '넓이는',result, 'm^2입니다.')

#say()
#ret = calc_area(type = 1, a= 5, b=5)
#area, msg = calc_area(2, 5, 5)
#area2, _ = calc_area(3, 10, 7,5)

#print(type(ret))
#print(type(area), type(msg))
#write(ret[0], ret[1])
#write(area, msg)
#write(area2, '평행사변형')






def say():
    print("계산하실 문제를 선택하세요\n 1.원의 넓이 \n 2.환율 문제 \n 3.마일-미터")
    j = int(input('선택하시오'))
    return j

def circle():
    r= int(input('원의 넓이:반지름을 입력해주세요'))
    res = r*r*3.14
    print('원의 넓이 :', res)

def moneyrate():
    rate = int(input('현재 미국 환율을 입력해주세요(원/ 달러 환율 = 현재금액'))
    koreamoney = int(input('환전하실 한국돈을 입력해주세요'))
    res = koreamoney/ rate
    print('환전한 금액 : ',res)

def mile_meter():
    print('마일 - 미터 변경입니다. 어떻게 변경할끼요? \n 1.마일을 미터로 \n 2.미터를 마일로')
    i = int(input('번호를 입력하시오.'))
    if i == 1:
        meter = int(input('미터를 입력하시오'))
        res = meter * 1.6
        print('meter -> mile :',res )
    elif i == 2:
        mile = int(input('마일을 입력하시오.'))
        res = mile / 1.6
        print('mile - > meter :',res)




