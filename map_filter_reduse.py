'''
m = map(lambda x: x * 2, [1, 2, 3, 4])
print (m)

for x in m :
    print (x)


list_a = [1, 2, 3]
list_b = [10, 20, 30]

m =map(lambda x, y: x + y, list_a, list_b)

for x in m :
    print (x)



a = [1, 2, 3, 4, 5, 6]
f= filter(lambda x : x % 2 == 0, a)
print (f)
for x in f :
    print (x)

'''

dict_a = [{'name': 'python', 'points': 10},
          {'name': 'java', 'points': 8},
          {'name': 'scala', 'points': 6},
          {'name': 'php', 'points': 5},
          ]
f= filter(lambda x : x['points'] > 6, dict_a)
for x in f :
    print (x)