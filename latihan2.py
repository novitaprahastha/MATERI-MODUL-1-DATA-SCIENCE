# z = ''
# for i in range (0, 5): 
#     for i1 in range (0, 5):
#         z += '*'
#     z += '\n'
# print(z)


# z = ''
# for i in reversed(range (0, 5)):
#     for i1 in range (0, i +1):
#         z += '*'
#     z += '\n'
# print(z)

# for i in range (10, 0, -1): 
#     print('*' )

# for i in  range (1, 11):
#     print ('*' * i)

# spaces = ' ' * 25
# print('%s 12 Butts Wind' % spaces)
# print ('%s twinklebuttom heath' % spaces)
# print('%s west snoring' % spaces)
# print ()
# print()
# print()

#=================
#hapus item di list
# del variabelnya [index yang mau di hapus]

# x = ['huge', 'hairy', 'pants']
# for i in x: 
#     print(i)
#     print(i)

# x = 45
# y = 80

# while x < 50 and y < 100: 
#     print(x, y)
#     x += 1 
#     y += 1 

# for x in range (0, 20):
#     print('hello %s' % x)
#     if x > 9:
#         break

# weight = 65

# for year in range (1, 16):
#     weight += 1
#     moonWeight = weight * 0.165
#     print( year, moonWeight)

# def moon_weight (weight, increase):
#     for year in range (1, 16):
#         weight = weight + increase
#         moon_weight = weight * 0.165
#         print('Year %s is %s' %(year, moon_weight))

# moon_weight(65, 2.5)

# class Animal: 
#     def __init__ (self, species, number_of_legs, color):
#         self.species = species
#         self.number_of_legs = number_of_legs
#         self.color = color 
# harry = Animal ('hippogriff', '6', 'pink')


# import copy 
# harry = Animal ('hippogriff', '6', 'pink')
# harriet = copy.copy(harry)
# print(harry.species)    
# print(harriet.species)
   
# angka = [1, 2, 3, 4, 5, 6, 9, 8, 10]
# mobil = ['Avanza', 'Inova', 'Xenia']

# mobil.extend(angka) #menambahkan/menggabungkan variabel angka
# # print(mobil)

# mobil.append('brio')
# # print(mobil)

# mobil.insert(1, 'Pajero')
# print(mobil)
    
# mobil.clear()

# angka.pop(3) #menghapus value sesuai index
# print(angka)

# angka.sort()
# angka.sort(reverse = False) #true: mengurutkan dari besar ke kecil , false: kecil ke besar
# # print(angka)

# angka.reverse()
# # print(angka)

# angka2 = angka.copy()
# angka2 = angka[::2].copy()
# # print (angka2)

# angka2 [0,2] = [12, 13]
# print(angka2)

# angka = [72, 45, 98, 65, 45, 67, 89]
# jumlahyangdisortir = 3
# x = angka[0:jumlahyangdisortir]
# x.sort()
# print(x)

# def Konversi (nilai, konversi):
#     if konversi == 'USD-IDR':
#         kurs = 14000
#         print('USD', nilai,  'setara = IDR', nilai * kurs)
#     elif konversi == 'IDR-USD':
#         kurs = 0.00007
#         print('IDR', nilai, 'setara = USD', nilai * kurs)
#     else: 
#         print('tidak tersedia')
# Konversi(14000, 'USD-IDR')

# i = 0 
# while i < 6:
    # print(i)
    # i += 1
    # if i == 3:
        # continue
    # i += 1 

    # print(i)

# inputuser = ''
# pasword = '123456'
# tebakanke = 1
# batastebakan = 5
# melebihibatas = False 

# while inputuser != pasword and not melebihibatas:
#     if tebakanke <= batastebakan:
#         inputuser = input('ketikan pass: ')
#         if inputuser != pasword and tebakanke < 5:
#             tebakanke += 1 
#             print('pass salah! silahkan percobaan ke', tebakanke)
#         elif inputuser != pasword and tebakanke == 5:
#             tebakanke += 1 
#             print('kesempatan sudah habis!')
#         else: 
#             print('pass benar')
#     else: 
#         melebihibatas = True 
#         print('Mohon maaf, coba lain kali')

# katatebakan = 'bakpao'
# tebakan = ''
# jumlahTebakan = 1
# batastebakan = 5
# overtebakan = False

# while tebakan != katatebakan and not overtebakan:
#     if jumlahTebakan <= batastebakan: 
#         inputuser = input('ketikan kata : ')
#         if inputuser != katatebakan and jumlahTebakan < 5:
#             jumlahTebakan += 1 
#             print('kata yang anda masukan salah! silahkan percobaan ke', jumlahTebakan)
#         elif inputuser != katatebakan and jumlahTebakan == 5:
#             jumlahTebakan += 1 
#             print('kesempatan sudah habis')
#         else: 
#             print('benar!')
#     else: 
#         overtebakan = True 
#         print('mohon maaf coba lain kali')
