from uzay_oyunu.kayit import gorev_kaydi
 
BEKLENEN = (
    "[YÜKSEK] Kara deliğe atla\n"
    "  1. Kredi kazan\n"
    "  2. Pilot bul\n"
    "  3. Hiperdrive al\n"
    "  sorumlu: Ayşe"
)
 
 
def test_dogrudan_cagri():
    metin = gorev_kaydi(
        "Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al",
        oncelik="yüksek", sorumlu="Ayşe",
    )
    assert metin == BEKLENEN
 
 
def test_liste_ve_sozluk_acarak_ayni_sonuc():
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    metin = gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler)
    assert metin == BEKLENEN
 
 
def test_oncelik_yalnizca_adli():
    # "yüksek" konumsal verilirse öncelik olmaz, bir adım sayılır.
    metin = gorev_kaydi("Görev", "a", "yüksek")
    assert metin.startswith("[NORMAL]")
    assert "2. yüksek" in metin
 
