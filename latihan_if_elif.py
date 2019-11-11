name = 'kadek ayu novita prahastha dewi'
print(len(name))

if len(name) <= 3 :
    print('name must be at least the 3 characters ')
elif len(name) >= 50 :
    print('name can be a maximum of 50  characters')
else:
    print('name looks good!')
#======================================================================
weight = int(input('Weight: '))
unit = input('L(bs) or K(g):')

if unit.upper() == 'L': 
   converted = weight * 0.45
   print(f'You are {converted} kilos')
else: 
    converted = weight / 0.45
    print(f'You are {converted} pounds')
#======================================================================
birth_year = input('Birth Year: ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)
#======================================================================
weight = input('Your weight (in pounds): ')
converted = int(weight) * 0.45
print(converted)
#======================================================================

#while loops 
i = 1
while i <= 5 :
    print(i) #akan dituliskan angka 1 terus menerus atau infinite loops
    i = i + 1
print('Done')


print('satu', 'dua', 'tiga', sep = '*') #hasilnya : satu*dua*tiga*
#======================================================================
#membuat bilangan ganjil genap 

genap : n % 2 = 0 
ganjil : n % 2 > 0 

bilangan = int(input('Masukan bilangan : '))

if bilangan % 2 == 0 : 
    print('Tergolong bilangan genap! ')
else: 
    (print ('Tergolong bilangan ganjil!'))

#======================================================================
#   Membuat program dengan berat badan

IMT = masa (kg) / tinggi (m) ^ 2

weight = int(input('Masukan masa (kg) : '))
height = int(input('Masukan tinggi (cm) : '))
IMT = weight / ((height/100) ** 2)


if IMT  < 18.5 : 
    print('Berat badan kurang.')
elif 18.5 <= IMT <= 24.9 :
    print('Berat badan ideal.')
elif 25.0 <= IMT <= 29.9 :
    print('Berat badan berlebih')
elif 30 <= IMT <= 39.9 : 
    print('Berat badan sangat berlebih')
else: 
    print('obesitas!')
