def angkaSegitiga (x): 
    # angka = ''
    for i in range (x): 
        for j in range (i): 
            print(j + 1, end = ' ')
        print()
angkaSegitiga(6)

def angkaSegitiga (x): 
    # angka = ''
    for i in range (x): 
        for j in range (0, x - i): 
            print(j + 1, end = ' ')
        print()
angkaSegitiga (5)

def angkaSegitiga (x): 
    # angka = ' '
    for i in range (x): 
        print(str(i)*i, end = '')
        print()
angkaSegitiga (6)

def angkaSegitiga (x):
    for i in range (x):
        print((i * i) - x, end = '')
        print()
angkaSegitiga(5)




