#import math
#print(math.pi)
#print(math.sqrt(85))
#import random
#print(random.random())
#print(random.choice([1,2,3,4]))
#S='Spam'
#print(len(S))
#print(S[0])
#print(S[1])
#print(S[-1])
#print(S[-2])
#print(S)
#print(S[1:3])
#print(S[0:4])
#print(S+'xyz')
#S='z' + S
#print(S)
#print(S.find('pa'))
#print(S.replace('pa','XYZ'))
#print(S)
#line = 'aaa,bbb,ccc,ddd\n'
#print(line)
#line = line.rstrip()
#print(line.split(','))
#print(S.upper())
#print(S.isalpha())
#print('%s, eggs, and %s' % ('spam', 'SPAM!'))
#print('{0}, eggs, and {1}'.format('spam', 'SPAM!'))
squares = []
for i in range(10,101):
    squares.append(i ** 2)
print(squares)
