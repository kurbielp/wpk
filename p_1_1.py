
def nww(n1,n2):
    (c_minor, c_major) = (n1, n2) if n1 < n2 else (n2, n1)
    (n1, n2) = (n1, n2) if n1 < n2 else (n2, n1)
    while c_minor != c_major:
        c_minor += n1;
        if c_minor > c_major:
            c_minor, c_major = c_major,c_minor
            n1, n2 = n2, n1

    return c_minor;


ds = [[3,6],[6,3],[5,8],[9,12],[98,34],[38,33]]
print('nww')
for pair in  ds:
    print(nww(pair[0],pair[1]), end=' ')
print('')

def nwd(n1,n2):
    (c_minor, c_major) = (n1, n2) if n1 < n2 else (n2, n1);
    while c_minor != c_major:
        c_major -= c_minor;
        if c_major<c_minor:
            c_major,c_minor = c_minor,c_major;

    return c_minor;


ds = [[8,16],[88,8],[9,12],[98,34],[38,19],[81,64]]
print('nwd')
for pair in  ds:
    print(nwd(pair[0],pair[1]), end=' ')
print('')