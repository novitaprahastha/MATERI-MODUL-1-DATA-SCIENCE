# x = [
#     (1, ['a', 'b', 'c'], 3), (4, 5, 6)
# ]
# x [0] [1] [2] = 'Andi'
# print(x)

#NOTES:
#set/ himpunan: 
# 1. (tidak ada index nya jadi tidak bisa di panggil satu satu)
# 2. duplicate elements not allowed
# 3. set mutable, tetapi elemennya immutable atau tidak bisa diubah, ex: list 
#======================================================================

# print(list(set(z)))

# z.add('') #untuk menambahkan elemen dalam set tetapi elemennya harus imumtable. elemenya hanya dapat ditambah satu elemen
#======================================================================

#mengambil index pada set 

z = {1,2,3,1,2,3}
z = list(z) #diubah jadi list

a = []
for i in z :
    a.append(i)
    print(a)
#======================================================================
# z.update('Andi)') #menambahkan elemen sekaligus ke dalam set
# z.remove('') #menghapus elemen
# z.discard(;) menghapus ekemen yang tidak ada tanpa error. 
# z.pop() #menghilangkan elemen terakhir 
# print(z)
# z.clear() #menghapus elemen set
#======================================================================

#contoh soal himpunan: 
a = list ('abcde')
b = list ('bcfgh')

# # a irisan b ???

a = set(a) #diubah dulu dari list menjadi set
b = set(b)

#mencari irisan/intersection
print(a.intersection(b))
print(b.intersection(a))
print(a & b) #mencari irisan bisa menggunakan '&'
print(b & a)

#mencari gabungan/union
print(a.union(b))
print(b.union(a))
print(a | b) #mencari irisan bisa menggunakan '|'
print(b | a)

#mencari selisih/difference
print(a.difference(b))
print(b.difference(a))
print(a - b) 
print(b - a)

#mencari symmetric diff
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a ^ b) 
print(b ^ a)
#======================================================================
#contoh soal 2:

p = list ('1 2 4 7 8 19')
q = list ('7 9 5 12 16 17 19 6')
r = list ('19 6 3 8')

p = set (p)
q = set (q)
r = set (r)

#p irisan q 

# note: list yang dua angka akan menjadi beda hasil karena tidak pakai koma 

p = {1, 2, 4, 7, 8, 19}
q = {7, 9, 5, 12, 16, 17, 19, 6}
r = {19, 6, 3, 8}

print(p.intersection(q))
print(p & q &r)

p = {-4, -3, -2, -1, 0, 1, 2, 3, 4}
q = {-7, -6, -5, -4, -3, -2, -1, 0, 1}
r = {-1, 0, 1, 2, 3, 4, 5, 6, 7}
s = {-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(p.union(q))
print(p.union(r))
print(q.union(r))

print(list(p.union(q)))
#======================================================================

a = {2, 3, 5, 9}
b = {5, 7, 9}

print(a.intersection(b))
print(a.union(b))
print(a & (a | b))
print(b & (a | b))
print((a | b) & (a | b))
print((a & b) | (a | b))