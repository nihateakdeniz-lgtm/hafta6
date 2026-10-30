

cumle = input("Cümle: ")
harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0
kelimenin_icinde = False
ters = ""
harfler = ""
sesliler = "aeıioöuü"

# Bu tek for turu sayma, ters çevirme ve harflerden arındırılmış metni oluşturur.
for karakter in cumle:
    ters = karakter + ters
    if karakter.isalpha():
        harf_sayisi += 1
        kucuk = karakter.lower()
        harfler += kucuk
        if kucuk in sesliler:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1
    if karakter.isdigit():
        rakam_sayisi += 1

    # PDF örneği kesme işaretli Adana'da sözcüğünü tek kelime sayıyor;
    # sözcük sınırı bu nedenle boşlukla belirlenir, noktalama sözcüğü bölmez.
    if not karakter.isspace():
        if not kelimenin_icinde:
            kelime_sayisi += 1
            kelimenin_icinde = True
    else:
        kelimenin_icinde = False

print(f"Harf: {harf_sayisi} Sesli: {sesli_sayisi} Sessiz: {sessiz_sayisi} Rakam: {rakam_sayisi} Kelime: {kelime_sayisi}")
print(f"Ters: {ters}")
if harfler == harfler[::-1]:
    print("Palindrom")
else:
    print("Palindrom değil")
