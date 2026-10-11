import json
from pathlib import Path
 
import pytest
 
from uzay_oyunu.oyun import galaksi_kur
 
YOL = Path(__file__).parent.parent / "uzay_oyunu" / "galaksi.json"
 
 
def veri_yukle() -> dict:
    with open(YOL, encoding="utf-8") as dosya:
        return json.load(dosya)
 
 
def test_json_ile_kurulum():
    g = galaksi_kur(**veri_yukle())
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100
 
 
def test_varsayilan_yakit_50():
    assert galaksi_kur(["mars"], {"mars": []}, "mars")["yakit"] == 50
 
 
def test_gecersiz_baslangic_value_error():
    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "venüs")
 
 
def test_her_baglanti_gecerli_gezegene_gider():
    veri = veri_yukle()
    for hedefler in veri["baglantilar"].values():
        assert set(hedefler) <= set(veri["gezegenler"])
 
