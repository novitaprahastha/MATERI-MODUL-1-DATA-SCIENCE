#membuat bintang 

star = ''
for i in range (5):
    star += '*'
    print (star)

#dibikinin fungsi: 

def star (x):
    star = ''
    for i in range (x):
        star += '*'
        print (star)
star (5)

#==========================

def rStar (x):
    star = ''
    for i in range (x): 
        star = '*' * (x - i) # i adalah index dari bintangnya, i => 0 = * 
        print(star)
rStar(10)

#==========================

# def angkaSegitiga (x): 
#     angka = ''
#     for i in range (x): 
#         for j in range (i): 
#             print(j + 1, end = ' ')
#         print()
# angkaSegitiga(6)

# def angkaSegitiga (x): 
#     angka = ''
#     for i in range (x): 
#         for j in range (0, x - i): 
#             print(j + 1, end = ' ')
#         print()
# angkaSegitiga (5)

# def angkaSegitiga (x): 
#     angka = ' '
#     for i in range (x): 
#         print(str(i)*i, end = '')
#         print()
# angkaSegitiga (6)

def AngkaSegitiga (x):
    for i in range (x):
        angka = ' '
        a = x - i
        for j in range (i):
            angka = str(i + 1) + ' '
        print(angka)
AngkaSegitiga(5)

# #============================================
#NOTES:
# x = [
#     [1,2,3], [4, 5, 6], [7, 8, 9]
# ]

# for i in x : #[1,2,3] [4,5,6] [7,8,9]
#     for j in (i):
#         print(j)

# for i in range (5): # 012345
#     for j in range(7,9): #7,9
#         print(i, 'dan', j)
# #note: 
# i 0 = 0  // j 0 = 7 // 0 dan 7 
# i 0 = 0  // j 0 = 8 // 0 dan 8 
# i 1 = 1    // j 1 = 7 // 1 dan 7
# i 2 = 1    // j2 = 8 // 1 dan 8 
# dst ...
 #=======================================

 #buat fungsi angka berpangkat
def pangkat (x, y): 
    out = 1
    for i in range (y):
        out =* x
    print (out)

def pangkatB (x, y): 
    if (y == 1): 
        return x 
    else:
        return x * pangkatB (x, y - 1)
print (pangkatB(2,3))

# rekursif fungsi(memakai fungsi itu sendiri)=  (harus return fungsi)

# pangkatB (2, 3) = return 2 * pangkatB (2, 2) => 2 * 4 
# pangkatB (2, 2) = return 2 * pangkatB (2, 1) => 2 * 2
# pangkatB (2, 1) = return 2  #berhubungan sama if yang y == 1 maka dia di angka 1 berhenti

#======================================================================
#fungsi faktorial 
def faktor (x): 
    angka = 1 
    for i in range (1, x+1): 
        angka *= i
    return angka 

# #pakai if else

def faktorial2(x): 
    if x <= 2: 
        return x 
    else: 
        return x * faktorial2(x-1)
print (faktorial2(2))












