n = 12

p_len=n*2-1
hn=0

def space_creator(p_len, i , reduce):
    n_len= int((p_len - i*2 +1)/2)
    for k in range(0, n_len-reduce):
        print(' ', end='')

for i in range(1,n+1):
    if i % 2 == 1:
        hn += 1;
        space_creator(p_len, i , 0)
        for n in range(1, hn+1):
            print(n, end=' ')
        for n in range(1, hn):
            print(hn-n, end=' ')
        space_creator(p_len, i , 1)
        print('')
    if i % 2 == 0:
        space_creator(p_len, i , 0)
        for n in range(1, hn+1 ):
            print(n, end=' ')
        for n in range(1, hn+1):
            print(hn-n+1, end=' ')
        space_creator(p_len, i , 1)
        print('')
