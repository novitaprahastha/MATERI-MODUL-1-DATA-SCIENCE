x = 'abcdefghijklmnopqrstuvwxyz'
print(x[: : 2])
print('g' in x) #mengetahui apakah ada g di x 
print(x.count('g')) #mengetahui berapa banyak ada huruf g 
#======================================================================

kalimat = 'Hari ini Andi tidak kuliah'
cari = 'h'
print(cari.lower() in kalimat.lower()) #di lower atau upper untuk diseragamkan terlebih dahulu agar bisa di baca o/python
print(kalimat.lower().count(cari.lower()))

print(cari.lower() in kalimat.lower())
print(kalimat.lower().count(cari.lower()))
#======================================================================

#list
x = ['Andi', 'Budi', 'Caca', 123, True]
print(x[len(x) - 1])
print(x[len(x) - 1])
print(type(x[-1]))

hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
# "Sekarang hari 'Rabu', hari apakah 100 hari lagi?"

now = 'rabu' ; brphari = 100
iNow = hari.index(now) #menghitung rabu itu hari keberapa
print(iNow)
sisahari = brphari % len(hari)
hariyangdicari = hari[(iNow + sisahari) % 7]
print(hariyangdicari)

hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']
hari.append ('senin2') #untuk menambahkan list ke dalam elemen
print(hari.append(senin2))
#======================================================================
#NOTES
# hari.insert(4, senin3) #menyisipkan list baru ke tengah2, tetapi bisa merubah index yang sudah ada
# hari.remove('senin2') #menghapus elemen di value 
# hari.pop(2) #menghapus elemen yang terakhir di index 2
# hari.clear() #menghapus semua elemen
# hari.sort() #mengurut abjad sesuai konten (kecil k besar)
# hari.sort(reverse = True) #mengurut abjad dg dibalik dari yang terakhir 
# hari.reverse() #mengurut sesuai index
# print(hari.index('senin')) #mengetahui senin itu hari ke berapa

# x = 123
# print(type(str(x)) #ngubah ke string 

# x = 'abcde'
# print(list(reversed(x) #membalik index

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = x([: : 2]).copy() #unutk mengcopy list

# a = [1, 2, 3, 4, 5, 6, 3]
#print(a.index(3, 3)