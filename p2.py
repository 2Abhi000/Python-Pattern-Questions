'''
prpgram to print pattern like this
*****
*****
*****
*****
*****
'''
n=int(input())
for i in range(1,n+1):
    for j in range(n):
        print('*',end=' ')
    print()
