#LAMDA FUNCTION (fungsi di dalam variabel)
#ex:
# x = lambda a : a 

# #artinya sama dengan 

# def y (a):
#     return a 

# x = lambda a, b, c : a + b + c

# #artinya sama dengan 

# def y (a, b, c):
#     return a + b +c 
#======================================================================

def myFunction (x): 
    return lambda a : a ** x 

pangkat2 = myFunction (2) #=> dipangkatkan 2 berasal dari function lamda a 
pangkat3 = myFunction (3)
pangkat4 = myFunction (4)
pangkat1000 = myFunction (1000)

print(pangkat4(2))

#  if else dengan lambda:
x = lambda a : True if a % 2 == 0 else False
print (x(3))

# # atau dengan function

def y (a):
    if a%2 == 0 :
        return True
    else: 
        return False 

x = lambda a : 'Angka Genap' if a % 2 == 0 else 'Angka Ganjil'
print (x(3))

x = lambda a : print (a)
x ('Hello') =>  hasilnya Hello
# berbeda dengan print(x('Hello')) => hasilnya none 

#======================================================================

#MAP PYTHON (mengeksekusi function tertentu untuk setiap elemen dalam variable yang itterable) harus d list
# sebelum di print

a = ['Coklat', 'Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']

def combi (a, b): 
    return a + ' ' + b

x = map (combi,a, b)
print (x)
print(list(x))
#======================================================================

x = [2, 4, 6, 8, 10]

def pangksat2 (a):
    return a ** 2 
# y = map(pangkat2, x) => x akan dimasukan ke dalam parameter a lalu akan di return menjadi a ** 2 
print(list(y))
 
# atau

list(z))

# #atau

b = []

for i in x:
    b.append (i ** 2)
print(b)

#FILTER FUNCTION (untuk menyaring)

x = range (11)
def kuranglima (x):
    if x < 5: 
        return True
    else: 
        return False
    
y = filter (kuranglima, x)
print(list(y))

# # atau

z = filter(lambda a : True if a >= 5 else False, x)
print(list(z))

x = pow (2, 2)
y = pow (3, 3)
print(x)
print(y)

# z = list(map(pow, [2, 3], [3, 3])) => kurung ke dua adalah pangkatnya
# print(z)

x = [1, 2, 3, 4, 5, 99]
y = [1, 2, 6, 7, 8, 99]

z = list(filter(lambda a : a in x, y))
print(z)

# atau

z = list(filter(lambda x : True if x < 3 else False, x))
z = list(filter(lambda x: x < 3 , x ))

angka = [1, 2, 3, 4]
#1 x 2 x 3 x 4 = 24

hasil = 1 
for i in angka: 
    hasil *= i
print(hasil)
#======================================================================
from functools import reduce
z = reduce(lambda a, b : a * b, angka)
print(z)

kata = ['Ini', 'Ibu', 'Budi']

print(' '.join(kata))

z = [a, b, c,......]
def x (z): 
    return z [0] + z [1] +......z[n]

angka = [1, 2, 3, 4]
z = list(map(lambda x: x * 2, filter(lambda x : x > 3, angka))) => ini hasilnya di filter dulu (4) lalu kali 2
print (z)

z = list(filter(lambda x : x > 3, map (lambda x: x * 2, angka)))
#======================================================================

# latihan

# nomor = [1 - 100]
# => amgka genap (filter)
# [2, 4, 6, 8,.....
# => setiap angka genap dikali 2 (map)
# [4, 8, 12, ......]
# => semua angka hasilnya dijumlahkan satu sama lain (reduce)
# [4 + 8 + 12+..........]

x = list(range(101))
# print(angka)

def angkaGenap (x): 
    if x % 2 == 0: 
        return True 
    else: 
        return False 
y = filter(angkaGenap, x)
# print(list(y))

z = list(map(lambda a: a * 2, x))
print(z)

from functools import reduce

 #CARA SINGKAT
z = reduce(lambda a, b : a + b, map(lambda a : a * 2, filter (lambda a : a % 2 == 0, x)))
print(z)
#========================================================================

# berapa bilangan prima dari 1-100? 

def prima (x): 
    a = False
    if x > 1:
        if x == 2: a = True
        else: 
            for i in range (2, x):
                if x % i == 0: a = False; break
                else: a = True
    else: a = False
    return a 

z = list(filter(prima, range(101)))
print(len(z))
    