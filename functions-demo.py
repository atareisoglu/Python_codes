sayi = int(input('Tam bölenlerini görmek ist4ediğiniz sayı giriniz: '))
def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleriBul(sayi))