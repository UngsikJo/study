
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