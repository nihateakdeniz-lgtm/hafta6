

kelime = "KOŞUL"
tahminler = ""
hata = 0
tamamlandi = False

while hata < 6:
    gorunen = ""
    for harf in kelime:
        if harf in tahminler:
            gorunen += harf + " "
        else:
            gorunen += "_ "
    print(f"{gorunen.strip()} (hata: {hata}/6)")

    if "_" not in gorunen:
        tamamlandi = True
        break

    giris = input("Harf: ").strip()
    if len(giris) != 1 or not giris.isalpha():
        print("Tek bir harf girin.")
        continue

    # Türkçe büyük harf dönüşümü: i→İ, ı→I; Python upper() tek başına i→I yapar.
    harf = giris.replace("i", "İ").replace("ı", "I").upper()
    if harf in tahminler:
        print("Bu harfi zaten denediniz.")
        continue

    tahminler += harf
    if harf not in kelime:
        hata += 1
else:
    print(f"Kelime: {kelime}")

if tamamlandi:
    print("Kazandınız!")
