import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı: ')
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