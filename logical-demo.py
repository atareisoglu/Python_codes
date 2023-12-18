isim = (input('İsminizi yazınız: '))
boy = float(input('boyunuzu yazınız: '))
kilo = float(input('kilonuzu yazınız: ')) # metre ile cm arasına nokta koyarak

index = (kilo / (boy ** 2))
zayif = (index >= 0) and (index <=18.4)
normal = (index > 18.4) and (index <=24.9)
kilolu = (index > 24.9) and (index <=29.9)
obez = (index > 29.9) and (index <=34.9)

print(f'{isim} kilo indeksin {index} ve kilo değerlendirtmen zayıf: {zayif}')
print(f'{isim} kilo indeksin {index} ve kilo değerlendirtmen normal: {normal}')
print(f'{isim} kilo indeksin {index} ve kilo değerlendirtmen kilolu: {kilolu}')
print(f'{isim} kilo indeksin {index} ve kilo değerlendirtmen obez: {obez}')
