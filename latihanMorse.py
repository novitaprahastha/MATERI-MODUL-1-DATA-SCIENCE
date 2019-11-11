morse = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'P' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..'
}

# abjad = list(morse)
# # print(abjad)
# sandi = list(morse.values())
# print(sandi)

x = list(morse.keys())
y = list(morse.values())
# print(x)
# print(y)
#=====================================

def ubahKemorse (teks): 
    kalimat = teks.lower(). replace ('', '')
    hasil = ' '
    for i in kalimat: 
        hasil = hasil + morse[i]
    print(hasil)

def ubahDarimorse (teks): 
    kalimat = teks.split('/')
    hasil = ' '
    for i in kalimat: 
        hasil = hasil + list(morse.keys())[list(morse.values()).index(i)]

# ubahKemorse('novita')
# ubahDarimorse('--. --')

