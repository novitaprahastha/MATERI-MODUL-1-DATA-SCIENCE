data = open ('data.txt', 'r')

print(data.readable())
print(data.read())
print(data.readlines())

# r = read
# w = write
# a = append
# \n = enter newline 

#di folder tes harus klik kanan open in terminal dulu
data = open('data.txt', 'w')
data = open('./../data1/data.txt', 'w') (.. untuk keluar dari folder)
data = open('./data1/data.txt', 'w')(dalam folder data 1/ kalau berbeda folder)
data.write('Test 123')
# data.write ('\nCoding Python')
data = open('data.py', 'a')
data.write('\tprint(x)')

data = open('data.mp4', 'w')
data.write ('my video')
data = open ('data.txt', 'r')
print(data.readable()) #True False data dpt dibaca atau tidak
print(data.read()) #print data.txt
print(data.readlines())
print(data.readline(5))

data = open('data.txt', 'r')
x = data.read()
print()

data = open('data.py', 'w')
data.write(x)

data = open('data.txt', 'r')
x = data.read().split(', ')[::-1]
print()

output = open ('x.txt', 'a')
for i in x :
    output.write (i + '\n')

data = open('file.csv', 'w')

file = open('file.csv', 'r')
x = file.read()

for row in x: 
    print(x)
    break

#=====================================

import csv

with open ('file.csv', 'r') as x:
    baca = csv.reader(x)
    print(list(baca))

x = ['no', 'nama']
y = [12, 'Andi']
print(dict(zip(x,y)))


import csv

with open ('data.csv', 'r') as x:
    baca = csv.DictReader(x)
    for i in baca:
        print(dict(i))

data = [
    {'nama' : 'Andi', 'usia' : 22, 'kota' : 'jakarta'},
    {'nama' : 'Budi', 'usia' : 22, 'kota' : 'jakarta'},
    {'nama' : 'Caca', 'usia' : 22, 'kota' : 'jakarta'},
]
 
with open('data.csv', 'w', newline= '') as x :
    kolom = ['nama', 'usia', 'kota']
    a = csv.DictWriter(x, fieldnames = kolom, delimiter= '!')
    a.writeheader()
    a.writerows(data)

#===================================================

import csv

with open ('file.csv', 'r') as x:
    baca = csv.reader(x)
    print(list(baca))

x = ['no', 'nama']
y = [12, 'Andi']
print(dict(zip(x,y)))


import csv

with open ('data.csv', 'r') as x:
    baca = csv.DictReader(x)
    for i in baca:
        print(dict(i))

data = [
    {'nama' : 'Andi', 'usia' : 22, 'kota' : 'jakarta'},
    {'nama' : 'Budi', 'usia' : 22, 'kota' : 'jakarta'},
    {'nama' : 'Caca', 'usia' : 22, 'kota' : 'jakarta'},
]
 
with open('data.csv', 'w', newline= '') as x :
    kolom = ['nama', 'usia', 'kota']
    a = csv.DictWriter(x, fieldnames = kolom, delimiter= '!')
    a.writeheader()
    a.writerows(data)

#=================================================
#JSON FILE
import json

with open ('1.json', 'r') as x : 
    out = json.load(x) # kl baca = load

print(type(out))
print(type(out[0]))
print(out)

with open ('haha.json', 'w') as y : 
    json.dump(out, y) #untuk nulis = dump