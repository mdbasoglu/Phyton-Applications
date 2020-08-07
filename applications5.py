'''
#kullanicidan gelen bir sayinin tek mi cift mi oldugunu gösteriniz

nummer=int(input('Schreiben Sie bitte Ihre Nummer!'))

if nummer % 2==0:
    print('Cif Sayidir') # yada print(f'{nummer} cift sayidir')
else:
    print('tek sayidir')
'''






'''
#kullanicidan gelen herhangi bi sayinin arti eksi sifir bak

num1=int(input('Lütfen bir sayi giriniz'))

if num1 ==0:
    print(f'{num1} sayisi 0 dir.')

elif num1>0:
    print(f'{num1} sayisi poziftir.')

else:
    print(f'{num1} sayisi negatiftir.')
'''






'''
x=10
y=5
if x>y: print(f'{x} sayisi {y}\'den büyüktür!')
'''

#sayinin faktöriyelini bulmak:

number= int(input('Schreib ein Zahl!'))
faktöriyel=1
if number < 0:
    print(f'{number} sayisi negatiftir')

elif number==0:
    print(f'{number} sayisinin faktöriyeli{faktöriyel}')

else:
    for x in range(1, number+1):
        faktöriyel=faktöriyel*x
    print(f'{number} sayisinin faktöriyeli  {faktöriyel}')

notes ={'ahmet': 58, 'mehmet': 76, 'ebru': 44, 'pinar': 59}
#50 ve üzeri notu olan ögrencileriler icin gecti yaz digerleri icin kaldi yaz.

for key, value in notes.items():
    if value >=50:
        print(f'{key} aldigi not {value}: GECTI')
    else:
        print(f'{key} aldigi not {value}: KALDI')    

print('hello world')







































