nama= 'Hari ini Hari tidak masuk sekolah'
# # jumlah huruf h?

cari='h'
x=nama.upper().replace(cari.upper(), '')
print(x)
jmlcari=len(nama)-len(x)
print(f'Jumlah huruf\'{cari}\'ada={jmlcari}')
#======================================================================

nama='Hari ini Hari tidak masuk sekolah karena hari Minggu'
#jumlah kata 'hari'
cari='hari'
x=nama.upper().replace(cari.upper(), '')
print(x)
jmlcari=int((len(nama)-len(x))/len(cari))
print(f'Jumlah kata\'{cari}\'ada={jmlcari}')
#======================================================================

# #latihan (24/10/2019)
nama = 'Hari ini adalah hari Kamis hari ke empat belajar koding'
#jumlah huruf h? 

cari = 'h'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlcari = len (nama) - len(x)
print(f'Jumlah huruf\'{cari}\'ada = {jmlcari}') #jangan ada spasi setelah \
#======================================================================

nama = 'aku adalah novita'
cari = 'a'
x = nama.upper().replace(cari.upper(), '')
jmlcari = len (nama) -len(x)
print(jmlcari)
#======================================================================
nama = 'Hari ini adalah hari yang sangat berbahagia hari Hari Hari'
#jumlah kata hari?
cari = 'hari'
x = nama.upper().replace(cari.upper(), '')
jmlcari = int((len(nama) - len(x))/len(cari)) #pakai int karena ada pembagian
print(jmlcari)
#======================================================================
nama = 'Aku aku aku aku'
cari = 'Aku'
x = nama.upper().replace(cari.upper(), '')
jmlcari = int((len(nama) - len(x)) / len(cari))
print(jmlcari)
jmlcari = int((len(nama) - len(x)) / len(cari))