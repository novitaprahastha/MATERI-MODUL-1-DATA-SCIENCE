#CLASS AND OBJECT

# class X: 
#     def __init__(self, name, age):
#         self.nama = name #self.nama merujuk ke name 
#         self.usia = age
#     def pensiun(self):
#         return 55 - self.usia

# objX = X('Andi', 22)
# objY = X('Budi', 23)

# print(objX.pensiun())
# print(objY.pensiun())

#===================================================
# class X: 
#     def __init__(self, name, age):
#         self.nama = name #self.nama merujuk ke name 
#         self.usia = age
#     def pensiun(self):
#         return 55 - self.usia

# class Y(X):
#     def __init__(self, name, age, city):
#         X.__init__(self, name, age)
#         self.kota = city


# objB = X('Banu', 19)
# objA = Y('Ali', 12, 'Jakarta')

# print(objA.kota)
#================================================

# FIBONACI
# def fibo(urutan): 
#     if urutan < 2:
#         return urutan
#     else: 
#         return fibo(urutan - 1) + fibo(urutan - 2)

#DIUBAH KE DALAM CLASS 
class Fibo:
    def fibo(self, urut):
        if urut < 2 :
            return urut
        else: 
            return self.fibo(urut - 1) + self.fibo(urut - 2)
Fibo = Fibo()
print(Fibo.fibo(1))
print(Fibo.fibo(6))
print(Fibo.fibo(10))

#==================================================

# x = 'AbcdEFgHi'
# return function => x = 'aBCDefGhI'

# def cekHuruf(x):
#     hasil = ''
#     for i in x :
#         if i.islower():
#             hasil += i.upper()
#         else: 
#             hasil += i.lower()
#     return hasil


# x = input('ketik kata : ')
# print(cekHuruf(x))

#==========================================================

# list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(len([list]))