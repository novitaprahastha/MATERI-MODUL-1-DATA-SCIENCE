x = 3
# panjAngka = str(len(x))

def cekRomawi (x):
    panjAngka = len(str(x))
    hasil = ''
    if panjAngka == 1 :
        hasil = cekSatuan(x)
    elif panjAngka == 2 :
        hasil = angkaPuluhan(x)
    elif panjAngka == 3:
        hasil = angkaRatusan (x)
    elif panjAngka == 4:
        hasil = angkaRibuan (x)
    else: 
        print('nonE')
    return hasil
    # elif panjAngka == 3 :
    #     cekRatusan ()
    # elif panjAngka == 4 :
    #     cekRibuan ()

def angkaPuluhan(x):
    sisAngka = x % 10
    satuanAngka = cekSatuan (sisAngka)
    selisihAngka = x - sisAngka
    hasil = cekPuluhan(selisihAngka)+ satuanAngka
    return hasil

def angkaRatusan (x): 
    sisAngka = x % 100
    satuanAngkaRat = angkaPuluhan (sisAngka)
    selisihAngka = x - sisAngka
    hasil = cekRatusan(selisihAngka)+ satuanAngkaRat
    return hasil

def angkaRibuan (x):
    sisAngka = x % 1000
    satuanAngkaRib = angkaRatusan(sisAngka)
    selisihAngka = x - sisAngka
    hasil = cekRibuan(selisihAngka)+ satuanAngkaRib
    return hasil

def cekSatuan (x): 
    if x <= 3:
        hasil = 'I' * x
    elif x == 4:
        hasil ='IV'
    elif x == 5:
       hasil = 'V'
    elif 6 <= x <= 8:
        hasil = 'V' + ('I' * (x-5))
    else: 
        hasil = ('IX')
    return hasil

def cekPuluhan (x):
    pangkat = x // 10
    if x <=  30:
       hasil = 'X' * pangkat
    elif x == 40:
        hasil = 'XL'
    elif x == 50:
        hasil = 'L'
    elif 60 <= x <= 80:
        hasil = 'L' + ('X' * ((x - 50) // 10))
    elif x == 90:
        hasil = 'XC'
    return hasil

def cekRatusan (x):
    pangkat = x // 100
    if x <=  300:
       hasil = 'C' * pangkat
    elif x == 400:
        hasil = 'CD'
    elif x == 500:
        hasil = 'D'
    elif 600 <= x <= 800:
        hasil = 'D' + ('C' * ((x - 500) // 100))
    elif x == 900: 
        hasil = 'CM'
    return hasil

def cekRibuan (x):
    pangkat = x // 1000
    if x < 4000:
       hasil = 'M' * pangkat
    return hasil

    
print(cekRomawi(987))
