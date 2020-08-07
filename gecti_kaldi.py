notes ={'ahmet': 58, 'mehmet': 76, 'ebru': 44, 'pinar': 59}

#50 ve üzeri notu olan ögrencileriler icin gecti yaz digerleri icin kaldi yaz.

for key, value in notes.items():
    if value >=50:
        print(f'{key} aldigi not {value}: GECTI')
    else:
        print(f'{key} aldigi not {value}: KALDI')  
