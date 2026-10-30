
import math

girdi_gecerli = True
try:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
except ValueError:
    # Sayısal olmayan girişlerde program hata vermek yerine açıklayıcı uyarı gösterir.
    a = b = c = 0.0
    girdi_gecerli = False

if not girdi_gecerli:
    print("Uyarı: Kenarlar sayı olarak girilmelidir.")
elif not math.isfinite(a) or not math.isfinite(b) or not math.isfinite(c):
    print("Uyarı: Kenarlar sonlu pozitif sayılar olmalıdır.")
elif a <= 0 or b <= 0 or c <= 0:
    print("Uyarı: Kenar uzunlukları pozitif olmalıdır.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Uyarı: Bu kenarlarla üçgen oluşturulamaz.")
else:
    # a en uzun kenar olmalı; açı formülünü ve çıktı sırasını böylece tutarlı kullanırız.
    if b > a:
        a, b = b, a
    if c > a:
        a, c = c, a
    if c > b:
        b, c = c, b

    if a == b == c:
        kenar_turu = "Eşkenar"
    elif a == b or a == c or b == c:
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"

    kosinus = (b * b + c * c - a * a) / (2 * b * c)
    # Yuvarlama hataları kosinüsü çok az [-1, 1] dışına çıkarabilir.
    kosinus = max(-1.0, min(1.0, kosinus))
    aci = math.degrees(math.acos(kosinus))
    if math.isclose(aci, 90):
        aci_turu = "Dik açılı"
    elif aci > 90:
        aci_turu = "Geniş açılı"
    else:
        aci_turu = "Dar açılı"

    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

    print(f"Tür: {kenar_turu}, {aci_turu}")
    print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {aci:.2f}°")
