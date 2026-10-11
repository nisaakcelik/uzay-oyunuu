def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str) -> str:
    """Bir görev kaydını metin olarak döndürür.
 
    adimlar: istenen sayıda adım metni (konumsal).
    oncelik: yalnızca adlı argüman olarak verilebilir.
    ekler: sorumlu gibi ek bilgiler (adlı argümanlar).
    """
    satirlar = [f"[{oncelik.upper()}] {baslik}"]
    for sira, adim in enumerate(adimlar, start=1):
        satirlar.append(f"  {sira}. {adim}")
    for anahtar, deger in ekler.items():
        satirlar.append(f"  {anahtar}: {deger}")
    return "\n".join(satirlar)
 
 
if __name__ == "__main__":
    # 1) Argümanları tek tek vererek
    print(
        gorev_kaydi(
            "Kara deliğe atla",
            "Kredi kazan",
            "Pilot bul",
            "Hiperdrive al",
            oncelik="yüksek",
            sorumlu="Ayşe",
        )
    )
 
    # 2) Liste (*) ve sözlük (**) açarak
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    print(gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler))
 
