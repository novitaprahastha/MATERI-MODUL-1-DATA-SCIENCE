#FUNCTION

# def namaFunction () :
#     program: 
# namaFunction()  #untuk mengeluarkan functionnya

# #contoh: 

f(x) = x ^ 2

def kuadrat (x) :
    print (x ** 2)
kuadrat (3)

def pangkat (angka1, angka2) :
    print(angka1 ** angka2)
pangkat (float(input('Ketik angka 1 : ')), float(input('Ketik angka 2 :')))
#======================================================================

#contoh soal:
#sebuah function dngan 1 parameter
#function => menentukan value parameter: ganjil/ genap 

def gangen (x):
    if x % 2 == 0 :
        print(x, 'tergolong GENAP')
    else: 
        print(x, 'tergolong GANJIL')
gangen (5)
#======================================================================

#sebuah function calculator:

def calc (): 
    x = float(input('Masukan angka pertama : '))
    op = (input('Masukan operator (+-*/) : '))
    y = float(input('Masukan angka kedua : '))
    if op == '+' : 
        print(x + y)
    elif op == '-' :
        print(x - y )
    elif op == '*' :
        print(x * y)
    elif op == '/' :
        print (x / y)
    else: 
        print('operator tidak tersedia. ')
calc() #memanggil functionnya 
#======================================================================

students = ['Andi', 'Budi', 'Caca']

def tes (x): 
    print(x[0])
    print('Caca' in x)
#======================================================================

#FUNCTION UBAH HURUF VOKAL

def vocal (kalimat): 
    kalimat = kalimat.lower()
    kalimat = kalimat.replace ('a', 'o')
    kalimat = kalimat.replace ('i', 'o')
    kalimat = kalimat.replace ('u', 'o')
    kalimat = kalimat.replace ('e', 'o')
    kalimat = kalimat.replace ('e', 'o')
    print(kalimat)
vocal ('lama')
#======================================================================

#Return Function (bisa di print karena ada return valuenya. value dari functionnya bisa diolah)


def LuasPersegi (sisi):
    print('Luas =', sisi * sisi)
def LuasPersegiReturn (sisi) :
    return sisi * sisi
#x = 4
#LuasPersegiReturn(5) = return? 

LuasPersegi (4)
print(LuasPersegiReturn(5))
#======================================================================

#WHILE LOOP

#selama kondisinya true, program ini akan terus berjalan. 
#ex:

i = 1
while i < 20 :
    print(i)
    i += 1

i = 20
while i >= 1 :
    print(i)
    i -= 2

students = ['Andi', 'Budi', 'Caca']
index = 0 
while index <= len(students) - 1 :
    print(students[index])
    index += 1
#======================================================================

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []
index = 0 

while index <= len(x) - 1:
    y.append(x[index] ** 2)
    index += 1 
print(y)
#======================================================================
 #BREAK AND CONTINUE    
i = 1
while i < 20 :
    print(i)
    if i == 5 :
        break
    i += 1

i = 0
while i < 20 :
    i += 1
    if i == 5 :
        continue
    print(i)
#======================================================================
#LATIHAN SOAL
#apabila salah akan terus keluar pass salah, ketik pasword
password = '12345'
inputuser = ''
while inputuser != password :
    inputuser = input ('Ketik password : ')
    if inputuser != password: 
        print('Password Salah!')
    else:
        print('Password Benar!')

# pass salah 5 kali 
password = '12345'
inputuser = ''
jumlahInput = 0 
batasInput = 5
lebih = False

while inputuser != password and not lebih:
    if jumlahInput < batasInput:
        inputuser = input(f'Input ke - {jumlahInput + 1 } ketik password : ')
        jumlahInput += 1 
    else: 
        lebih = True

if lebih:
    print('Kesempatan habis, tunggu 24 jam')
else:
    print('Password benar!')

