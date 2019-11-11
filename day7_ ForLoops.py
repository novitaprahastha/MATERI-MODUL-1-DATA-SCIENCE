#FOR LOOP
kota = ['Jakarta', 'Bandung', 'Surabaya']
i = 0 
while i < len(kota):
    print(kota[i])
    i += 1
#atau dengan FOR 
for i in range (len(kota)):
    print(kota[i])

for namaKota in kota:
    print(namaKota)
#======================================================================
x = 'purwadhika'
x = [1, 2, 3, 4, 5]
for i in x: 
    print(i)

for i in range (2, 5): #start dan stop 
    print(i)
else: 
    print('OK')
#======================================================================
##BREAK DAN CONTINUE
for i in range (2, 10):
    print(i)
    if i == 7:
        break #atau continue 
    # print(i) #hasilnya beda dengan print diatas. 
else: 
    print('OK')
#======================================================================

#contoh soal: 

#1 - 10 kalau angka genap keluar adalah 'WOW

for i in range (1, 11):
    if i%2 == 0:
        print('WOW')
    else: 
        print(i)
#======================================================================
# #FizzBuzz
# bikin 1 function 1 param => FizzBuzz
# bilangan kelipatan 3 => Fizz
# bilangan kelipatan 5 => Buzz
# bilangan kelipatan 3 dan 5 => FizzBuzz
def  FizzBuzz (x):
    for i in range (1, x+1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0: 
            print('Fizz')
        elif i % 5 == 0: 
            print('Buzz')
        else: 
            print(i)

FizzBuzz (15)
#======================================================================

#REVERSE LIST 
x = [1, 2, 3, 4, 5, 6, 7]
y = ['Andi', 'Budi', 'Caca']
#buat menjadi [7, 6, 5, 4, 3, 2, 1]


#1. reverse
x.reverse()
print(x)

#2
print(x[: : -1])

#3 reversed
print(list(reversed(x)))

#4 
def balikPosisi (mylist): 
    hasil = []
    for i in range (len(mylist)): 
        hasil.insert(0, mylist[i])
    return hasil
print(balikPosisi(x))
print(balikPosisi(y))
#======================================================================
x = ['Andi', 'Budi', 'Caca']
y = [3, 5, 7, 9]

def balikPosisi (mylist):
    for e in range (round(len(mylist) / 2)):
        asli = mylist[e]
        mylist[e] = mylist[len(mylist)-1-e]
        mylist[len(mylist)-1-e] = asli
    return mylist
print(balikPosisi(x))
print(balikPosisi(y))
#======================================================================

#mengubah huruf vokal 

def ubahVokal (kata): 
    output = ''
    for huruf in kata: 
        if huruf in 'aiueo':
            output = output + 'o'
        else: 
            output = output + huruf 
    return output

print(ubahVokal('nananananana'))
#======================================================================
#PALINDROME
#palindrome (string yang di balik mirip)
# ex: 
# katak = katak True
# malam = malam True 
#bantal != latnab False 

x = 'malam'
y = ''.join(list(x[: : -1])) ## gausah dipakai

def palindrome (kata): 
    if kata == kata[: : -1]:
        return True
    else: 
        return False
print(palindrome(x))

##atau 

def palindrome2 (kata): 
    for i in range(round(len(kata)/2)): 
        palindromekah = False 
        if kata[i] == kata[len(kata)-1 - i]: 
            palindromekah = True 
        else: 
            palindromekah = False 
            break 
    return palindromekah
print(palindrome2('malam'))

#======================================================================
#MEMBALIK KATA 

kalimat = 'Hai aku Novita'
'iaH uka ativoN'

def reverse (s): 
    str = ''
    for i in s: 
        str = i + str
    return str
s = 'Hai Aku Novita Prahastha Dewi'
print('String awal :',  end = ' ')
print(s)
print ('String yang sudah di balik: ',  end = '')
print(reverse(s))