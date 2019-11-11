days = { 
    'senin' : 'monday', 'selasa' : 'tuesday', 'rabu' : 'wednesday', 'kamis' : 'thursday', 
    'jumat' : 'friday', 'sabtu' : 'saturday', 'minggu' : 'sunday' }

# hari = list(days) 
# print(hari)
day = list(days.values())
print(day)

x = input('Ketik nama hari (ENG/ID): ')

if x.lower() in hari:
    engHari = day[hari.index(x.lower())]
    print(f'Bhs Inggrisnya {x.lower()} adalah {engHari}')

else: 
    idDay = hari[day.index(x.lower())]
    print(f'Bhs Indonesianya {x.lower()} adalah {idDay}')

##======================================================================
numbers = {
    'satu' : 'one', 'dua' : 'two', 'tiga' : 'three', 'empat' : 'four',
    'lima' : 'five', 'enam' : 'six', 'tujuh' : 'seven', 'delapan' : 'eight'}

nomor = list(numbers)
number = list(numbers.values())

x = input('Input the numbers (ENG/ID) : ')

if x.lower() in number: 
    numberID = nomor[number.index(x.lower())]
    print(f'The translation for {x.lower()} is {numberID}')
else: 
    nomoreNG = number[nomor.index(x.lower())]
    print(f'Bahasa inggrisnya {x.lower()} adalah {nomoreNG}')
#======================================================================
fruits = {'banana' : 'pisang', 'apple' : 'apel', 'orange' : 'jeruk', 'watermelon' : 'semangka'}

fruit = list(fruits.values())
# print(fruit)
buah = list(fruits)
# print(buah)

x = input('masukkan nama buah : ')

if x.lower in fruit: 
    fruitID = fruit[buah.index(x.lower())]
    print(f'translate for {x.lower()} is {fruitID}')
else: 
    buahENG = buah[fruit.index(x.lower())]
    print(f'bahasa inggrisnya {x.lower()} adalah {buahENG} ')


if x.lower in buah: 
    buahENG = fruit[buah.index(x.lower())]
    print(f'Bahasa Inggrisnya {x.lower()} adalah {buahENG}')
else:
    fruitID = buah[fruit.index(x.lower())]
    print(f'Indonesian for {x.lower()} is {fruitID}')
