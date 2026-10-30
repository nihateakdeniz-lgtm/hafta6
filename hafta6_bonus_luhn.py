
govde = "453914880343646"
aday = 0
bulundu = False

while aday <= 9:
    numara = govde + str(aday)
    toplam = 0
    # Sağdan başlayınca kontrol hanesinin hemen solundaki her ikinci rakam iki katına çıkar.
    for indis in range(len(numara) - 2, -1, -1):
        rakam = int(numara[indis])
        if (len(numara) - 1 - indis) % 2 == 1:
            rakam *= 2
            if rakam > 9:
                rakam -= 9
        toplam += rakam
    toplam += aday
    if toplam % 10 == 0:
        bulundu = True
        break
    aday += 1

if bulundu:
    print(f"Kontrol hanesi: {aday}")
else:
    print("Kontrol hanesi bulunamadı.")
