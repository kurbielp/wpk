
def nww(n1,n2):
    if n1<n2:
        minor=n1;
        major=n2
    else:
        minor=n2;
        major=n1;

    c_minor=minor
    c_major=major;
    while c_minor!=c_major:
        c_minor+=minor;
        if c_minor>c_major:
            temp=major;
            c_temp = c_major;
            major=minor;
            c_major=c_minor;
            minor=temp;
            c_minor=c_temp;

    return c_minor;

'''
ds = [[3,6],[5,8],[9,12],[98,34],[38,33]]
for pair in  ds:
    print(nww(pair[0],pair[1]))
'''

def nwd(n1,n2):
    if n1<n2:
        minor=n1;
        major=n2
    else:
        minor=n2;
        major=n1;

    c_minor=minor
    c_major=major;
    while c_minor!=c_major:
        c_major-=c_minor;
        if c_major<c_minor:
            c_temp = c_major;
            c_major=c_minor;
            c_minor=c_temp;


    return c_minor;


ds = [[8,16],[88,8],[9,12],[98,34],[38,33],[81,64]]
for pair in  ds:
    print(nwd(pair[0],pair[1]))