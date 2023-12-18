# isim = input('İsminizi giriniz.')
# yas = int(input('Yaşınızı giriniz.'))
# egitimbilgileri = input('Eğitim bilgilerinizi giriniz.')

# if (yas >= 18) and (egitimbilgileri == 'lise' or egitimbilgileri == 'üniversite'):
#     print('Ehliyet alabilirsiniz.')
# else:
#     print('Ehliyet alamazsınız.')


# not1 = int(input('1. yazılı notunu giriniz'))
# not2 = int(input('2. yazılı notunu giriniz'))
# not3 = int(input('sözlü notunu giriniz'))

# ortalama = (not1 + not2 + not3) / 3

# if ortalama < 25:
#     print('0')
# elif ortalama < 45:
#     print('1')
# elif ortalama < 55:
#     print('2')
# elif ortalama < 70:
#     print('3')
# elif ortalama < 85:
#     print('4')
# else:
#     print('5')

import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/8/9): ')
tarih = tarih.split('/')

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days <= 365:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2:
    print('2. servis aralığı')
elif days > 365*2 and days <= 365*3:
    print('3. servis aralığı')
else:
    print('Hatalı süre')