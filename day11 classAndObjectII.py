class Orang: 
    nama = 'Andi'

class Manusia: 
    def __init__(self, nama):
        self.nama = nama 

class Pria (Manusia):
    def __init__ (self, nama):
        Manusia. __init__ (self, nama)
        self.gender = 'laki laki'

class Wanita (Manusia):
    def __init__ (self, nama):
        Manusia. __init__ (self, nama)
        self.gender = 'perempuan'

    
objA = Manusia ('Budi')
objB = Orang ()
objC = Pria ('Doni')
objD = Wanita ('Lili')
print(vars(objA))
print(objB.nama)
print(vars(objC))
print(vars(objD))
#================================================

#MULTI LEVEL INHERITANCE

class X ():
    def __init__ (self, x):
        self. x = x 

class Y(X):
    def __init__ (self, x, y):
        X. __init__ (self, x)
        self.y = y 
class Z(Y):
    def __init__ (self, x, y, z):
        Y. __init__ (self, x, y)
        self.z = z 

objZ = Z ('Novita', 'Data Science', 'Oke Banget')
print(vars(objZ))
#=============================================

#MULTIPLE INHERITANCE 

class Karnivora:
    def __init__ (self):
        self.daging = True
        self.nama = 'Karnivora'

class Herbivora: 
    def __init__ (self):
        self.tumbuhan = True 
        self.nama = 'Herbivora'

class Omnivora (Karnivora, Herbivora): 
    def __init__ (self):
        Karnivora. __init__ (self)
        Herbivora. __init__ (self) #keluarnya hanya herbivora krn properti nya bergantung pada urutan. dalam kasus ini
        # herbivora ada di bawah karnivora atau terakhir
        self.mcD = True 
        self.nama = 'Omnivora'
objA = Omnivora ()
print(vars(objA))
print(Omnivora.__mro__) # metod resolution order: untuk melihat urutannya
#===============================================
#UNTUK MELIHAT WAKTU SEKARANG
import datetime as dt
x = dt.datetime.now()

print(x.strftime('%d')) #TGL
print(x.strftime('%A')) #HARI
print(x.strftime('%m')) #BULAN
print(x.strftime('%B'))#NAMA BULAN
print(x.strftime('%Y')) #TAHUN

print(x.strftime('%H')) #24 JAM
print(x.strftime('%I')) #12 JAM
print(x.strftime('%p')) #AM.PM
print(x.strftime('%M'))#MIN
print(x.strftime('%S')) #SEC

print(x.strftime('%c'))
print(x.strftime('%x'))

print(x.strftime ('Hari ini adalah hari %A'))
#==============================================
#TUGAS => 
# File .py => class/object (di file katihan Class)

# from latihanClass import waktu

# print(waktu.tanggal)
# print(waktu.hari)
# print(waktu.jam)

