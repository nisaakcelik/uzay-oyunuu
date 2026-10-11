def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Sahip olunan esyalari metin olarak dondurur."""
    esyalar = []

    if credits:
        esyalar.append("bol kredi")

    if engines:
        esyalar.append("guclu motorlar")

    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Hedefleri numaralandirilmis menu olarak dondurur."""
    sonuc = ["Nereye gitmek istersin?"]

    for numara, hedef in enumerate(hedefler, start=1):
        sonuc.append(f"[{numara}] {hedef}")

    return "\n".join(sonuc)
