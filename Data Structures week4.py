# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kqoPKfoaypExFgzeOJeg4NsCI2KLQjTl
"""

import numpy as np
np.sin(3.141592)

d= 3
type(d)

d =3.5
 type(d)

d="K"
type(d)

d= True
type(d)

d= "I love you"
type(d)

import numpy as np
np.round (decimals = 1, a = 3.567)

a = '4.56'
 b= '3.42'

float(a)+float(b)

a= 4.43
print('your score is ', a)

print(f'your score is {a:.1f}. Good Job!')

scores = 85
if scores >= 90:
  print('A')
elif scores >= 80:
  print('B')
elif scores >=70:
  print('C')
elif scores >=60:
  print('D')
else:
  print('F')



weight = 65.3
height = 1.78

bmi = weight/(height*height)

if bmi >= 25:
  print('비만')
elif bmi <18.5:
  print('저체중')
else:
  print('정상')

signals = {'green':'go', 'yellow':'go faster', 'red':'smile for camera'}
signals.keys()

list(signals.values())

list(signals.item())

signals = {'green':'go', 'yellow':'go faster', 'red':'smile for camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

total_amount = 100000 #총 구매금액
discount_rate = 0      #할인율

if total_amount >= 100000:
  discount_rate = 0.2
elif total_amount >= 50000:
  discount_rate = 0.1
else:
  discount_rate = 0
price = total_amount * (1 - discount_rate)
print(f' 최종 가격 : {price}원')

age = 90
intensity = "high" #"low", "moderate", "high"중 하나

if intensity == "low":
  rate = 0.5
elif intensity == "moderate":
  rate = 0.7
else:
 rate = 0.85


BPM = (220 - age)*rate

print(f'목표 BPM은 {BPM}입니다.')

time = 27 #분 단위
distance = 2400 #m 단위

avg_speed = distance / time
print(f'평균속도 : {avg_speed:.3f}')

credit_score = 650
loan_amount = 10000000

if credit_score >= 700:
  money_payback = loan_amount * 1.035
elif credit_score >= 600:
  money_payback = loan_amount * 1.05
else:
  money_payback = loan_amount * 1.07

print(f'1년 뒤 갚아야 할 돈 : {money_payback:.0f}')

time_diffrence = 10 # 시간차 초
sound_speed = 343 # 소리의 속도 초
distance = time_diffrence * sound_speed #m단위

print(f'번개와의 거리 :{distance}m')

a = range(0,10)
type(a)

a= list(range(0,10,2))
a

a= (3,4,5,6,7)
b = list(a)
b[3] = 10000
a

v= [3,4,5,6]
(v[0]+v[1]+v[2]+v[3])/4

v=list(range(1,30,2))
v[14]

import numpy as np

v=[3,4,5,6]
np.mean(v)

a=3
b=5
def add(c,d):
  sum= b + d
  return sum

d = add(3,6)
d

a = [1,2,3,4,5]
def avg(var_list):
  sum = 0
  for x in var_list:
    sum = sum+ x

  return sum / len(var_list)

avg(a)

a = [[1,2,3],[12,3],[1,2,4]]
def diag_list(a1, a2,a3):
  sum = 0
  a1 = 0
  a2 = 0
  for x in a1:
    for y in a2:
      sum = sum + a3[a1,a2]
      a2 = a2 + 1
    a1 = a1 + 1

  return sum/a1

  diag_list(3,4,a)

a = [[1,2,3],[12,3],[1,2,4]]
def diag_avg(arr):
  sum = 0
  cnt = 0
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if i ==j:
        sum = sum + arr[i][j]
        cnt = cnt + 1
  return sum/cnt

  diag_avg(a)

def sum():
  sum = 0
  for i in range(1,201):
    if i % 4 == 0 and i % 6 ==0:
     sum += i
     if sum > 1000:
      break
  return sum

sum()

def find_max_min(a,b,c):
  if a > b and a > c:
    max = a
  elif b > a and b > c:
    max = b
  else:
    max = c
  if a < b and a < c:
    min = a
  elif b < a and b < c:
    min = b
  else:
    min = c

  if min == max:
    return '모든 수가 같습니다.'
  else:
    return max, min

find_max_min(5,5,5)

del sum
amount_payment = [5000, 2500, 1500, 2000, 2200, 2300, 7500]

def calculate(cost_list):
  total = sum(cost_list)
  average = total/len(cost_list)
  return total, average

calculate(amount_payment)

saving = [20, 30, 25, 18, 57, 19, 50, 20, 10, 100, 14, 5]
year = [2024,2024,2024,2024,2024,2024,2024,2024,2024,2024,2024,2024]
month = [1,2,3,4,5,6,7,8,9,10,11,12]

saving.index(5)

def cal(money,y, m):
  total = sum(money)
  min_save = min(money)
  min_index =  saving.index(min_save)
  min_year = y[min_index]
  min_month = m[min_index]
  return total, min_year, min_month

cal(saving,year,month)

def gugudan():
  gugu = []
  for i in range(0,9):
    gugu.append([])#2차원 리스트를 만드는 방법
    for j in range(0,9):
      gugu[i].append((i+1)*(j+1))
  return gugu
gugudan()

g= gugudan()
g[3][4]

food_list = ["피자","햄버거","피자","치킨","피자","햄버거","치킨"]

def count_str(word_list):
  word_dict={}
  for x in word_list:
    if x in word_dict:
      word_dict[x] += 1
    else:
      word_dict[x]=1
  return word_dict

count_str(food_list)

workout_time = [1,2,1.5,3,0.4,0,0.6,0.5,1,0.5,2,0,1,1.5,1.5,1,0.5,2.5,0.1,0,1,2,2,1.0,2,0.5,0,1.5]
def get_workout_time_weekByWeek(w_time):
  avg_workout = []
  for i in range(0,4):
    d = workout_time[7*i:7*(i+1)]
    avg_workout.append(sum(d)/len(d))
  return avg_workout

get_workout_time_weekByWeek(workout_time)

observatories = ['천문대 A','천문대 B', '천문대 C', '천문대 D']
observations = [
    [15,20,35,10,5],#천문대 A
    [12,25,22,18,30],#천문대 B
    [20,30,25,15,10],#천문대 C
    [5,10,20,35,25]#천문대 D
]
def stats_observatories(station,obs):
  stats = []
  for i in range(0,4):
    d = {}
    d['name']= station[i]
    d['total'] = sum(obs[i])
    d['max'] = max(obs[i])
    d['date'] = obs[i].index(d['max']) + 1
    stats.append(d)
  return stats
stats_observatories(observatories, observations)