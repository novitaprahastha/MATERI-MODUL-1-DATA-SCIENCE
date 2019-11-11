#CLASS = cetakan object

# class Mobil:  #object nya akan sama 
#     warna = 'merah'
#     tahun = 2010
#====================================
#create object mobil1 

mobil1 = Mobil()
print(mobil1)
print(mobil1.warna)
print(mobil1.tahun)
#====================================
#MEMBUAT CLASS YANG BISA DIGUNAKAN OLEH BEBERAPA OBJECT
class MobilCustom () : 
    def __init__ (self, warna, tahun, model): #warna dan tahun adalah property nya. 
        self.color = warna #self digunakan ketika buat property supaya bisa nempel di object
        self.year = tahun
        self.model = model

mobil1 = MobilCustom ('pink', 2018, 'X')
mobil2 = MobilCustom ('blue', 2010, ['A', 'B'])

print(mobil1.color) #=> yang digunakan adalah property dalam self (self.color)
print(mobil2.year)

#NOTE: jumlah property dan atribut harus sama => warna, tahun, model = pink, 2018, X. 
#==============================================
#MEMBUAT CLASS DENGAN METOD
class MobilCustom ():
    def __init__ (self, warna, tahun, model): 
        self.color = warna
        self.year = tahun
        self.model = model
# method
    def jadul (self): 
        if self.year < 2010:
            return True
        else: 
            return False

# atau dengan fungsi:

    def tes (self): 
        print(self.color, self.year, self.model, self.jadul())

mobilA = MobilCustom ('merah', 1998, 'X')
print(mobilA.tes())
#====================================

class Mobil ():
    def __init__ (self, warna, seat): 
        self.color = seat
        self.seat = seat

class Car (Mobil):
    pass #inheritance property nya sama persis dengan class mobil
mobil1 = Mobil ('pink', 4)
car1 = Car ('black', 8)
print(mobil1.color, mobil1.seat)
print(car1.color, car1.seat)
#======================================================

class Mobil ():
    def __init__ (self, warna, seat): 
        self.color = seat
        self.seat = seat

class Car (Mobil):
    gps = True #gps adalah property dari car, jadi tidak akan bisa di print di mobil 1. class car = class mobil ttp ditambah gps

mobil1 = Mobil (['pink', 'black'], 4)
car1 = Car ('black', 8)
print(mobil1.color, mobil1.seat)
print(car1.color, car1.seat, car1.gps)
#=====================================================
class Mobil ():
    def __init__ (self, warna, seat): 
        self.color = warna 
        self.seat = seat

class Car (Mobil):
    def __init__ (self, soundSys): 
        self.soundSys = soundSys

mobil1 = Mobil ('pink', 4)
car1 = Car ('dolbi')
print(mobil1.color, mobil1.seat)
print(car1.soundSys)
#==========================================

class X: 
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar

# cara membuat inherit yang sama persis: 

class Y(X):
    def __init__(self, nama, gelar):
        X.__init__(self, nama, gelar)

class Y(X):
    pass

# class Y(X): 
#     super().__init__(nama, gelar)       => supper(untuk ngembaliin property ke induk)
objX = x ('andi', 'prof')
objY = Y ('budi', 'Dr.')
print(objX.nama)
#==============================================================

#MENAMBAHKAN PROPERTI
class X: 
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar
class Y(X): 
    def __init__(self, nama, gelar, univ):
        super().__init__(nama, gelar)
        self.kampus = univ 
objX = X('Andi', 'M.Sc')
objY = Y ('Budi', 'Dr', 'UNPAD')
print(objY.kampus)
print(getattr(objY, 'nama'))
print(hasattr(objY, 'warna')) #untuk ngecek apakah warna ada di atrbut objy, hasilnya true atau false

#UNTUK PRINT SEMUA 
from pprint import pprint
pprint(vars(objY))
#ATAU
print(vars(objY))
#==============================================

#untuk menambahkan atribut di objek nya langsung (objek yang sudah jadi) tanpa mengubah class nya 
objY.warna = 'merah'
print(vars(objY))
# atau
setattr(objY, 'alamat', 'BSD')
print(vars(objY))
#======================================================================

#DELETE ATRIBUT 

# delattr(objY, 'alamat')
# print(vars(objY))
#==============================================================

#MENGHAPUS ATRIBUT PADA CLASS
class Z:
    nama = 'Z'
    usia = 21
objZ = Z()
print(objZ.nama)
print(objZ.usia)

del Z.nama
print(objZ.usia)
#=======================================================================

#MENGUBAH VALUE MENJADI NAMA VARIABEL 
nama = 'ultraman'
vars()[nama] = 12345
print(ultraman)
#====================================
#CONTOH SOAL: MENGUBAH DICT JADI OBJEK 

class student: 
    def __init__ (self, nama, usia):
        self.nama = nama
        self.usia = usia 

data = [
    {'nama' : 'Andi', 'usia' : 21}, 
    {'nama' : 'Budi', 'usia' : 22},
    {'nama' : 'Caca', 'usia' : 23},
    {'nama' : 'Deni', 'usia' : 24}
]

#CARA 1 
def createObj (x):
    nama = x ['nama']
    vars()[nama] = student(x['nama'], x['usia'])
    return vars () [nama]
#CARA 2
def createObj (x):
    return student(x['nama'], x['usia'])
#CARA 3 
dataNew = list(map(lambda x : student(x['nama'], x['usia']), data))
print(dataNew[0].nama)
print(dataNew[0].usia)
#====================================================

#untuk persegi, Luas persegi => sisi

class persegi: 
    def __init__ (self, sisi): 
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2 

persegiA = persegi(4)
persegiB = persegi(16)
persegiC = persegi(27)

print(vars(persegiA)); print(vars(persegiB)); print(vars(persegiC))
#============================================

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
print(vars(objA))
print(objB.nama)
print(vars(objC))
