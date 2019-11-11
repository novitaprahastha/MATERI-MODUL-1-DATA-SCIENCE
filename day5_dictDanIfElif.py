#dictionary (ada key dan value)

andi = {
    'nama' : 'Andi',
    'age' : 22,
    'is_married' : False
    'cars' : ['Alphard', 'Xpander', 'Innova ']
}

print(andi['nama'])
print(andi['age'])
print(andi['is_married'])

#atau

print(andi.get('nama')) #untuk memanggil valuenya 
print(andi.get('job)')) #tidak ada dalam property 

#kalau merubah value nya:

andi ['nama'] = 'Budi'
print(andi)
print(andi['adress')['geo'] = untuk melihat value andi 
andi.['salary'] = 2500000000 #untuk nambahin ke dalam property
andi.update({'no_ktp' : 1234567262626}) #untuk nambahin ke dalam property
print(andi)
print(list(andi)) #untuk mindahin ke list, tetapi hanya bisa keys nya saja.
print(andi.keys()) #untuk dapet list dari key nya saja.
print(andi.values()) #untuk nengetahui values dari dictionary
print(andi.items()) #untuk mengeluarkan values dari dict 
#======================================================================
#LATIHAN

days = { 
    'senin' : 'monday', 'selasa' : 'tuesday', 'rabu' : 'wednesday', 'kamis' : 'thursday', 
    'jumat' : 'friday', 'sabtu' : 'saturday', 'minggu' : 'sunday' }

#id = eng/ eng = id 

hari = input('Ketik nama hari : ')
print(f'{hari.lower()} = {days.get(hari.lower(), )}')
print(f'{hari.upper()} = {days.get(hari.lower(), "Ga ada!")}')
print(f'{hari.upper()} = {days.get(hari.lower(), )}')
print(f'{hari.upper()} = {days.items(hari.lower(), "Ga ada!")}')
#======================================================================


#if, else, elseif
nilai = 60
if nilai > 80:
    print('Anda Lulus') #atau print(f'nilai anda {nilai}, anda lulus)
elif nilai < 40:
    print ('Anda tidak lulus')
else:
    print ('Anda remedial')

#comparison

jomblo = True
if jomblo == True: #jangan lupa :
    print('Anda Jomblo')
else:
    print('Anda taken')

jomblo = True; nganggur = True
if jomblo == True and nganggur == True:
    print('Anda jomblo pengangguran')
elif jomblo == True and not nganggur:
    print('Anda jomblo kurang piknik')
elif not jomblo and nganggur:
    print('Anda cuy')
else:
    print('anda OK!')
#======================================================================
#AND, OR 
and : kondisinya harus terpenuhi semua
or : kondisinya boleh salah satu saja yang terpenuhi

nilai = 98
'''
nilai >= 82 : A
nilai 72 - 81 : B 
nilai 62 - 71 : C
nilai 52 - 61 : D
nilai < 52 : E 
'''

if nilai >= 82:
    print('Anda mendapatkan nilai A')
elif 72 <= nilai <= 81:
    print('Anda mendapatkan nilai B')
elif 62 <=  nilai <= 71:
    print ('Anda mendapatkan nilai C')
elif 52 <= nilai <= 61:
    print ('Anda mendapatkan nilai D')
else: 
    print('Anda tidak lulus')

    ###pakai >= <=

