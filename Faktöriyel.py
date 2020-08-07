number= int(input('Schreib eine Nummer!'))
faktöriyel=1
if number < 0:
    print(f'{number} ist negativ.')

elif number==0:
    print(f'{number} sayisinin faktöriyeli{faktöriyel}')

else:
    for x in range(1, number+1):
        faktöriyel=faktöriyel*x
    print(f'{number} sayisinin faktöriyeli  {faktöriyel}')
