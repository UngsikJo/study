
one_marx = 'Groucho',
one_marx
('Groucho',)
marx_tuple='Groucho', 'Chico', 'Harpo'
marx_tuple
('Groucho', 'Chico', 'Harpo')
marx_tuple=('Groucho', 'Chico', 'Harpo')
marx_tuple
('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
a
'Groucho'
b
'Chico'
c

c
'Harpo'
password = 'swordfish'
icecream ='tuttifrutti'
password, icecream = icecream, password
password
'tuttifrutti'
icecream
'swordfish'
marx_list=['Groucho' ,'Chico','Harpo']
tuple(marx_list)
('Groucho', 'Chico', 'Harpo')
empty_dict={}
empty_dict
{}
bierce = {
"day" : "A period of twenty-four hours, mostly misspent",
"positive":"Mistaken at the top of one's voice",
"misfortune":"The kind of fortune that neverr misses",
}
bierce
{'day': 'A period of twenty-four hours, mostly misspent', 'positive': "Mistaken at the top of one's voice", 'misfortune': 'The kind of fortune that neverr misses'}
lol = [['a', 'b'],['c','d'],['e','f']]
dict(lol)
{'a': 'b', 'c': 'd', 'e': 'f'}
lot = [('a','b'),('c','d'),('e','f')]
lot
[('a', 'b'), ('c', 'd'), ('e', 'f')]
dict(lot)
{'a': 'b', 'c': 'd', 'e': 'f'}
tol=(['a','b'],['c','d'],['e','f'])
dict(tol)
{'a': 'b', 'c': 'd', 'e': 'f'}
los =['ab','cd','ef']
dict(los)
{'a': 'b', 'c': 'd', 'e': 'f'}
tos=('ab','cd','ef')
dict(tos)
{'a': 'b', 'c': 'd', 'e': 'f'}
pythons = {
'Chapman':'Graham',
'Cleese':'John',
'Idle':'Eric',
'Jones':'Terry',
'Palin':'Michael'
}
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}
pythons['Gilliam']='Gerry'
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Gerry'}
pythons['Gilliam'] = 'Terry'
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry'}
some_pythons = {
'Graham':'Chapman',
'John':'Cleese',
'Eric':'Idle',
'Terry':'Gilliam',
'Michael':'Palin',
'Terry':'John'
}
some_pythons
{'Graham': 'Chapman', 'John': 'Cleese', 'Eric': 'Idle', 'Terry': 'John', 'Michael': 'Palin'}
list(some_pythons)
['Graham', 'John', 'Eric', 'Terry', 'Michael']
some_pythons
{'Graham': 'Chapman', 'John': 'Cleese', 'Eric': 'Idle', 'Terry': 'John', 'Michael': 'Palin'}
list(pythons)
['Chapman', 'Cleese', 'Idle', 'Jones', 'Palin', 'Gilliam']
others= {'Marx':'Groucho','Howard':'Moe'}
pythons.update(others)
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry', 'Marx': 'Groucho', 'Howard': 'Moe'}
first = {'a':'1','b':'2'}
second = {'b':'platypus'}
first.update(second)
first
{'a': '1', 'b': 'platypus'}
del pythons['Marx']
del pythons['Howard']
pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry'}
pythons.clear()
pythons
{}
pythons ={}
pythons
{}
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gilliam': 'Terry'}
'Chapman' in pythons
True
'Palin' in pythons
True

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
{'green': 'go', 'yellow': 'go faster', 'red': 'smile for camera', 'blue': 'confuse everyone'}

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for camera'}

original_signals = signals.copy()

signals['blue'] = 'confuse everyone'

signals
Out[5]:
{'green': 'go',
 'yellow': 'go faster',
 'red': 'smile for camera',
 'blue': 'confuse everyone'}

original_signals
Out[6]: {'green': 'go', 'yellow': 'go faster', 'red': 'smile for camera'}

empty_set = set()

empty_set
Out[8]: set()

even_number = {0, 2, 4, 6, 8}

ene_number
Traceback(most
recent
call
last):

Cell
In[10], line
1
ene_number

NameError: name
'ene_number' is not defined

even_number
Out[11]: {0, 2, 4, 6, 8}

odd_numbers = {1, 3, 5, 7, 9}

odd_numbers
Out[13]: {1, 3, 5, 7, 9}

set
{'letter')
Cell
In[14], line
1
set
{'letter')
^
SyntaxError: closing
parenthesis
')'
does
not match
opening
parenthesis
'{'

set('letter')
Out[15]: {'e', 'l', 'r', 't'}

set(['DAsher', 'Dancer', 'Prancer', 'Mason-Dixon'])
Out[16]: {'DAsher', 'Dancer', 'Mason-Dixon', 'Prancer'}

set(('Ummagumma', 'Echoes', 'Atio Heart Mother'))
Out[17]: {'Atio Heart Mother', 'Echoes', 'Ummagumma'}

set({'apple': 'red', 'orange': 'orange', 'Cherry': 'red'})
Out[18]: {'Cherry', 'apple', 'orange'}

drinks - {
    'martin': {'vodka', 'vermouth'}
    'black russian': {'vodka', 'kahula'}
    Cell In[19], line 1
    drinks - {
    ^
    SyntaxError: '{' was never closed


        drinks - {
            'martin': {'vodka', 'vermouth'},
            'black russian': {'vodka', 'kahula'},
            'white russian': {'cream', 'kahula', 'vodka'},
            'manhattan': {'rye', 'vermouth', 'bitters'},
            'screwdriver': {'ornage juice': 'vodka'}
        }
    Traceback(most recent call last):

Cell
In[20], line
1
drinks - {

    NameError: name 'drinks' is not defined


        drinks = {
    'martin': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahula'},
    'white russian': {'cream', 'kahula', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'ornage juice': 'vodka'}
}

for name, contents in drinks.items():
    if
'vodka' in contents:
print(name)

martin
black
russian
white
russian

drinks = {
    'martin': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahula'},
    'white russian': {'cream', 'kahula', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'ornage juice': 'vodka'}
}

drinks = {
    'martin': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahula'},
    'white russian': {'cream', 'kahula', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'ornage juice', 'vodka'}
}

for name, contents in drinks.items()
Cell In[25], line 1
for name, contents in drinks.items()
^
SyntaxError: expected
':'

for name, contents in drinks.items():
    if
'vodka' in contents and not ('vermouth' in contents and 'cream' in contents):
print(name)

martin
black
russian
white
russian
screwdriver

for name, contents in drinks.items():
    if
'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
print(name)

black
russian
screwdriver

for name, contents in drinks.items():
    if
contents & {'vermouth', 'orange juice'}:
print(name)

martin
manhattan

for name, contents in drinks.items():
    if
'vodka' in contents and not contents & {'vermouth', 'cream'}:
print(name)

black
russian
screwdriver

bruss = drinks['blue russian']
Traceback(most
recent
call
last):

Cell
In[30], line
1
bruss = drinks['blue russian']

KeyError: 'blue russian'

bruss = drinks['black russian']

wruss = drinks['white russian']

a = {1, 2}

b = {3, 4}

a & b
Out[35]: set()

a & b
Out[36]: set()

a = {1, 2}

b = {2, 3}

a & b
Out[39]: {2}

a.intersection(b)
Out[40]: {2}

bruss & wruss
Out[41]: {'kahula', 'vodka'}

a | b
Out[42]: {1, 2, 3}

a.unnion(b)
Traceback(most
recent
call
last):

Cell
In[43], line
1
a.unnion(b)

AttributeError: 'set'
object
has
no
attribute
'unnion'

a.union(b)
Out[44]: {1, 2, 3}

bruss | wruss
Out[45]: {'cream', 'kahula', 'vodka'}

drinks['black russian'].add("bruss")

drinks['black russian']
Out[47]: {'bruss', 'kahula', 'vodka'}

drinks
Out[48]:
{'martin': {'vermouth', 'vodka'},
 'black russian': {'bruss', 'kahula', 'vodka'},
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks.add("bruss") = 'black russian'
Cell
In[49], line
1
drinks.add("bruss") = 'black russian'
                      ^
                      SyntaxError: cannot
assign
to
function
call
here.Maybe
you
meant
'=='
instead
of
'='?


drinks['black russian'] = drinks['black russian'].add("bruss")

drinks['black russian']

drinks['black russian']

drinks
Out[53]:
{'martin': {'vermouth', 'vodka'},
 'black russian': None,
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks['black russian'] = {'vodka', 'kahula'}

drinks
Out[55]:
{'martin': {'vermouth', 'vodka'},
 'black russian': {'kahula', 'vodka'},
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

t = drinks['black russian'].copy()

t
Out[57]: {'kahula', 'vodka'}

drinks['black russian'].add("bruss")

drinks
Out[59]:
{'martin': {'vermouth', 'vodka'},
 'black russian': {'bruss', 'kahula', 'vodka'},
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks['black russian'] = drinks['black russian'].add("bruss")

drinks['black russian']

drinks['black russian']

dirinks
Traceback(most
recent
call
last):

Cell
In[63], line
1
dirinks

NameError: name
'dirinks' is not defined

drinks
Out[64]:
{'martin': {'vermouth', 'vodka'},
 'black russian': None,
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks['black russian'].add("bruss")
Traceback(most
recent
call
last):

Cell
In[65], line
1
drinks['black russian'].add("bruss")

AttributeError: 'NoneType'
object
has
no
attribute
'add'

drinks['black russian'] = {'vodka', 'kahula'}

drinks['black russian'].add("bruss")

type(drinks)
Out[68]: dict

type(drinks['black russian')
Cell
In[69], line
1
type(drinks['black russian')
^
SyntaxError: closing
parenthesis
')'
does
not match
opening
parenthesis
'['

type(drinks['black russian'])
Out[70]: set

type(drinks['black russian'].add("bruss"))
Out[71]: NoneType

bruss - wruss
Out[72]: {'bruss'}

drinks = {
    'martin': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahula'},
    'white russian': {'cream', 'kahula', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'ornage juice', 'vodka'}
}

bruss = drinks['black russian']

wruss = drinks['white russian']

bruss - wruss
Out[76]: set()

wruss - bruss
Out[77]: {'cream'}

a ^ b
Out[78]: {1, 3}

a.symmetric)diffence(b)
Cell
In[79], line
1
a.symmetric)diffence(b)
            ^
            SyntaxError: unmatched
')'

a.symmetric_diffence(b)
Traceback(most
recent
call
last):

Cell
In[80], line
1
a.symmetric_diffence(b)

AttributeError: 'set'
object
has
no
attribute
'symmetric_diffence'

a.symmetric_diffrence(b)
Traceback(most
recent
call
last):

Cell
In[81], line
1
a.symmetric_diffrence(b)

AttributeError: 'set'
object
has
no
attribute
'symmetric_diffrence'

a.symmetric_difference(b)
Out[82]: {1, 3}

bruss ^ wruss
Out[83]: {'cream'}

a <= b
Out[84]: False

a.issubset(b)
Out[85]: False

bruss <= wruss
Out[86]: True

marx_list = ['Guocho', 'Chico', 'Harpo']

marx_tuple = 'Goucho', 'Chico', 'Harpo'

marx_dict = {'Goucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}

marx_list[2]
Out[90]: 'Harpo'

marx_tuple[2]
Out[91]: 'Harpo'

marx_dict[Harpo]
Traceback(most
recent
call
last):

Cell
In[92], line
1
marx_dict[Harpo]

NameError: name
'Harpo' is not defined

marx_dict['Harpo']
Out[93]: 'harp'signals = {'green':'go', 'yellow':'go faster', 'red':'smile for camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
{'green': 'go', 'yellow': 'go faster', 'red': 'smile for camera', 'blue': 'confuse everyone'}

signals = {'green':'go', 'yellow':'go faster', 'red':'smile for camera'}

original_signals = signals.copy()

signals['blue'] = 'confuse everyone'

signals
Out[5]:
{'green': 'go',
 'yellow': 'go faster',
 'red': 'smile for camera',
 'blue': 'confuse everyone'}

original_signals
Out[6]: {'green': 'go', 'yellow': 'go faster', 'red': 'smile for camera'}

empty_set = set()

empty_set
Out[8]: set()

even_number={0,2,4,6,8}

ene_number
Traceback (most recent call last):

  Cell In[10], line 1
    ene_number

NameError: name 'ene_number' is not defined


even_number
Out[11]: {0, 2, 4, 6, 8}

odd_numbers = {1,3,5,7,9}

odd_numbers
Out[13]: {1, 3, 5, 7, 9}

set{'letter')
  Cell In[14], line 1
    set{'letter')
                ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'


set('letter')
Out[15]: {'e', 'l', 'r', 't'}

set(['DAsher','Dancer','Prancer','Mason-Dixon'])
Out[16]: {'DAsher', 'Dancer', 'Mason-Dixon', 'Prancer'}

set(('Ummagumma','Echoes','Atio Heart Mother'))
Out[17]: {'Atio Heart Mother', 'Echoes', 'Ummagumma'}

set({'apple':'red','orange':'orange','Cherry':'red'})
Out[18]: {'Cherry', 'apple', 'orange'}

drinks - {
'martin':{'vodka','vermouth'}
'black russian':{'vodka','kahula'}
  Cell In[19], line 1
    drinks - {
             ^
SyntaxError: '{' was never closed


drinks - {
'martin':{'vodka','vermouth'},
'black russian':{'vodka','kahula'},
'white russian':{'cream','kahula','vodka'},
'manhattan':{'rye','vermouth','bitters'},
'screwdriver':{'ornage juice' : 'vodka'}
}
Traceback (most recent call last):

  Cell In[20], line 1
    drinks - {

NameError: name 'drinks' is not defined


drinks = {
'martin':{'vodka','vermouth'},
'black russian':{'vodka','kahula'},
'white russian':{'cream','kahula','vodka'},
'manhattan':{'rye','vermouth','bitters'},
'screwdriver':{'ornage juice' : 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

martin
black russian
white russian

drinks = {
'martin':{'vodka','vermouth'},
'black russian':{'vodka','kahula'},
'white russian':{'cream','kahula','vodka'},
'manhattan':{'rye','vermouth','bitters'},
'screwdriver':{'ornage juice' : 'vodka'}
}

drinks = {
'martin':{'vodka','vermouth'},
'black russian':{'vodka','kahula'},
'white russian':{'cream','kahula','vodka'},
'manhattan':{'rye','vermouth','bitters'},
'screwdriver':{'ornage juice' , 'vodka'}
}

for name, contents in drinks.items()
  Cell In[25], line 1
    for name, contents in drinks.items()
                                        ^
SyntaxError: expected ':'


for name, contents in drinks.items():
    if 'vodka' in contents and not('vermouth' in contents and 'cream' in contents):
        print(name)

martin
black russian
white russian
screwdriver

for name, contents in drinks.items():
    if 'vodka' in contents and not('vermouth' in contents or 'cream' in contents):
        print(name)

black russian
screwdriver

for name, contents in drinks.items():
    if contents & {'vermouth','orange juice'}:
        print(name)

martin
manhattan

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

black russian
screwdriver

bruss = drinks['blue russian']
Traceback (most recent call last):

  Cell In[30], line 1
    bruss = drinks['blue russian']

KeyError: 'blue russian'


bruss = drinks['black russian']

wruss = drinks['white russian']

a = {1,2}

b= {3,4}

a&b
Out[35]: set()

a & b
Out[36]: set()

a = {1,2}

b= {2,3}

a&b
Out[39]: {2}

a.intersection(b)
Out[40]: {2}

bruss & wruss
Out[41]: {'kahula', 'vodka'}

a | b
Out[42]: {1, 2, 3}

a.unnion(b)
Traceback (most recent call last):

  Cell In[43], line 1
    a.unnion(b)

AttributeError: 'set' object has no attribute 'unnion'


a.union(b)
Out[44]: {1, 2, 3}

bruss | wruss
Out[45]: {'cream', 'kahula', 'vodka'}

drinks['black russian'].add("bruss")

drinks['black russian']
Out[47]: {'bruss', 'kahula', 'vodka'}

drinks
Out[48]:
{'martin': {'vermouth', 'vodka'},
 'black russian': {'bruss', 'kahula', 'vodka'},
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks.add("bruss") = 'black russian'
  Cell In[49], line 1
    drinks.add("bruss") = 'black russian'
    ^
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?


drinks['black russian'] = drinks['black russian'].add("bruss")

drinks['black russian']

drinks['black russian']

drinks
Out[53]:
{'martin': {'vermouth', 'vodka'},
 'black russian': None,
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks['black russian'] = {'vodka','kahula'}

drinks
Out[55]:
{'martin': {'vermouth', 'vodka'},
 'black russian': {'kahula', 'vodka'},
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

t = drinks['black russian'].copy()

t
Out[57]: {'kahula', 'vodka'}

drinks['black russian'].add("bruss")

drinks
Out[59]:
{'martin': {'vermouth', 'vodka'},
 'black russian': {'bruss', 'kahula', 'vodka'},
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks['black russian'] = drinks['black russian'].add("bruss")

drinks['black russian']

drinks['black russian']

dirinks
Traceback (most recent call last):

  Cell In[63], line 1
    dirinks

NameError: name 'dirinks' is not defined


drinks
Out[64]:
{'martin': {'vermouth', 'vodka'},
 'black russian': None,
 'white russian': {'cream', 'kahula', 'vodka'},
 'manhattan': {'bitters', 'rye', 'vermouth'},
 'screwdriver': {'ornage juice', 'vodka'}}

drinks['black russian'].add("bruss")
Traceback (most recent call last):

  Cell In[65], line 1
    drinks['black russian'].add("bruss")

AttributeError: 'NoneType' object has no attribute 'add'


drinks['black russian'] = {'vodka','kahula'}

drinks['black russian'].add("bruss")

type(drinks)
Out[68]: dict

type(drinks['black russian')
  Cell In[69], line 1
    type(drinks['black russian')
                               ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['


type(drinks['black russian'])
Out[70]: set

type(drinks['black russian'].add("bruss"))
Out[71]: NoneType

bruss - wruss
Out[72]: {'bruss'}

drinks = {
'martin':{'vodka','vermouth'},
'black russian':{'vodka','kahula'},
'white russian':{'cream','kahula','vodka'},
'manhattan':{'rye','vermouth','bitters'},
'screwdriver':{'ornage juice' , 'vodka'}
}

bruss = drinks['black russian']

wruss = drinks['white russian']

bruss-wruss
Out[76]: set()

wruss-bruss
Out[77]: {'cream'}

a^b
Out[78]: {1, 3}

a.symmetric)diffence(b)
  Cell In[79], line 1
    a.symmetric)diffence(b)
               ^
SyntaxError: unmatched ')'


a.symmetric_diffence(b)
Traceback (most recent call last):

  Cell In[80], line 1
    a.symmetric_diffence(b)

AttributeError: 'set' object has no attribute 'symmetric_diffence'


a.symmetric_diffrence(b)
Traceback (most recent call last):

  Cell In[81], line 1
    a.symmetric_diffrence(b)

AttributeError: 'set' object has no attribute 'symmetric_diffrence'


a.symmetric_difference(b)
Out[82]: {1, 3}

bruss^wruss
Out[83]: {'cream'}

a<=b
Out[84]: False

a.issubset(b)
Out[85]: False

bruss<=wruss
Out[86]: True

marx_list = ['Guocho' , 'Chico','Harpo']

marx_tuple = 'Goucho', 'Chico','Harpo'

marx_dict = {'Goucho' : 'banjo','Chico':'piano','Harpo':'harp'}

marx_list[2]
Out[90]: 'Harpo'

marx_tuple[2]
Out[91]: 'Harpo'

marx_dict[Harpo]
Traceback (most recent call last):

  Cell In[92], line 1
    marx_dict[Harpo]

NameError: name 'Harpo' is not defined


marx_dict['Harpo']
Out[93]: 'harp'