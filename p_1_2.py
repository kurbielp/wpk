
n = 11


for i in range(0,n):
    if i % 2 ==0:
        for j in range(0, n):
            if j % 2 == 0:
                print ('X ', end='')
            else:
                print('O ', end='')
        print('')
    if i % 2 ==1:
        for k in range(0, n):
            if k % 2 == 0:
                print ('O ', end='')
            else:
                print('X ', end='')
        print('')
