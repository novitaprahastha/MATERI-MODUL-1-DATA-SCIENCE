#membalik kalimat 

def getReversed (x): 
    kalimatRev = ''
    listKata = x.split(' ')
    for kata in listKata: 
        kalimatRev += kata[: : -1] + ' '
    return kalimatRev
    
x = input('masukan kalimat : ')
hasilRev = getReversed(x)
print(f'{x} kebalikannya adalah {hasilRev}')

    