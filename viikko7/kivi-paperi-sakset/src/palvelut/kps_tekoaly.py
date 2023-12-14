from tekoaly.tekoaly import Tekoaly
from kivi_paperi_sakset import KiviPaperiSakset

class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = Tekoaly()
        tokan_siirto = tekoaly.anna_siirto()

        return f"Tietokone valitsi: {tokan_siirto}"