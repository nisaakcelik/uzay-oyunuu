from uzay_oyunu.oyun import yakit_ekle
 
 
def test_yakit_ekle_depo_cagrilar_arasinda_paylasilmaz():
    # Hatalı sürümde (depo=[]) liste fonksiyon tanımlanırken bir kez oluşur
    # ve çağrılar arasında paylaşılır; ikinci çağrı [5, 7] döndürür.
    yakit_ekle(5)
    assert yakit_ekle(7) == [7]
 
 
def test_yakit_ekle_verilen_depoyu_kullanir():
    depo = [1]
    assert yakit_ekle(2, depo) == [1, 2]
 
