

n_girdi = input("n: ").strip()
if not n_girdi.isdigit() or int(n_girdi) < 1:
    print("Uyarı: n pozitif bir tam sayı olmalıdır.")
else:
    n = int(n_girdi)
    adim = 0
    en_yuksek = n
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        adim += 1
        if n > en_yuksek:
            en_yuksek = n
    print(f"{int(n_girdi)} → 1: {adim} adım, en yüksek değer {en_yuksek}")

sinir_girdi = input("Üst sınır: ").strip()
if not sinir_girdi.isdigit() or int(sinir_girdi) < 1:
    print("Uyarı: Üst sınır pozitif bir tam sayı olmalıdır.")
else:
    sinir = int(sinir_girdi)
    en_uzun_baslangic = 1
    en_uzun_adim = 0
    baslangic = 1
    while baslangic <= sinir:
        deger = baslangic
        sayac = 0
        # Her başlangıç için Collatz dizisini üreten iç içe while döngüsü.
        while deger != 1:
            deger = deger // 2 if deger % 2 == 0 else 3 * deger + 1
            sayac += 1
        if sayac > en_uzun_adim:
            en_uzun_adim = sayac
            en_uzun_baslangic = baslangic
        baslangic += 1
    print(f"1–{sinir} arasında en uzun zincir: {en_uzun_baslangic} ({en_uzun_adim} adım)")
