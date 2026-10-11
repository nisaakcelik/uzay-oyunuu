from uzay_oyunu.araclar import en_bagli_gezegenler, hamle_sayaci, sure_olc
 
GALAKSI = {
    "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
    "baglantilar": {
        "dünya": ["centauri", "sirius", "orion"],
        "centauri": ["dünya", "sirius", "orion"],
        "sirius": ["dünya", "centauri", "orion", "kara_delik"],
        "orion": ["sirius", "centauri"],
        "kara_delik": ["sirius"],
    },
}
 
 
def test_sayac_birer_birer_artar():
    say = hamle_sayaci()
    assert [say(), say(), say()] == [1, 2, 3]
 
 
def test_sayaclar_birbirinden_bagimsiz():
    a, b = hamle_sayaci(), hamle_sayaci()
    a()
    a()
    assert b() == 1
 
 
def test_en_bagli_gezegenler_sirasi():
    assert en_bagli_gezegenler(GALAKSI) == [
        "sirius", "centauri", "dünya", "orion", "kara_delik",
    ]
 
 
def test_sure_olc_sonucu_degistirmez_ve_sure_yazar(capsys):
    olcumlu = sure_olc(en_bagli_gezegenler)
    assert olcumlu(GALAKSI) == en_bagli_gezegenler(GALAKSI)
    assert "sn sürdü" in capsys.readouterr().out
 
