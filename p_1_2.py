
n = 11

for i in range(0,n):
    for j in range(0, n):
        if (j % 2 == 0 and i % 2 ==0) or (j % 2 == 1 and i % 2 ==1):
            print ('X ', end='')
        else:
            print('O ', end='')
    print('')

