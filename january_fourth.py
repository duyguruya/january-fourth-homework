def bul_en_buyuk_en_kucuk(liste):
    """Verilen listedeki en büyük ve en küçük sayıları bulur."""
    en_buyuk = max(liste)
    en_kucuk = min(liste)
    return en_buyuk, en_kucuk

sayilar = []
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)

en_buyuk, en_kucuk = bul_en_buyuk_en_kucuk(sayilar)

print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")