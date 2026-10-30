

kimlik = input("T.C. kimlik no: ").strip()

if len(kimlik) != 11 or not kimlik.isdigit() or kimlik[0] == "0":
    print("GEÇERSİZ")
else:
    tek = 0
    cift = 0
    # İlk dokuz hanede sıfır tabanlı çift indisler 1., 3., 5., 7., 9. hanelerdir.
    for indis in range(9):
        if indis % 2 == 0:
            tek += int(kimlik[indis])
        else:
            cift += int(kimlik[indis])

    h10 = (7 * tek - cift) % 10
    h11 = (tek + cift + h10) % 10
    if h10 == int(kimlik[9]) and h11 == int(kimlik[10]):
        sonuc = "GEÇERLİ"
    else:
        sonuc = "GEÇERSİZ"
    print(f"Tek: {tek} Çift: {cift} 10. hane: {h10} 11. hane: {h11} → {sonuc}")
