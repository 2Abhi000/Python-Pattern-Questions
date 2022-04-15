'''
print equilateral triangle
'''
n=int(input())
for i in range(1,11):
    print(' '*(n-i) + '* '*(i))
'''
Another way

n=int(input())
for i in range(1,11):
    print(' '*n,end=' ')
    print('* '*(i))
    n-=1
'''
