KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti is not None and \
            isinstance(kapasiteetti, int) and kapasiteetti >= 0 else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None and \
            isinstance(kasvatuskoko, int) and kasvatuskoko >= 0 else OLETUSKASVATUS
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if self.alkioiden_lkm == 0 or not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.ljono = self._kasvata_lista()

            return True

        return False

    def _kasvata_lista(self):
        taulukko_old = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.ljono)
        return self.ljono

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]

    def alkioiden_maara(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return [self.ljono[i] for i in range(self.alkioiden_lkm)]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        x.lisaa_multiple(*a.to_int_list(), *b.to_int_list())
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        z.lisaa_multiple(*a.to_int_list())
        z.poista_multiple(*b.to_int_list())
        return z

    def poista_multiple(self, *values):
        for value in values:
            self.poista(value)

    def lisaa_multiple(self, *values):
        for value in values:
            self.lisaa(value)

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            elements = [str(self.ljono[i]) for i in range(self.alkioiden_lkm)]
            return "{" + ", ".join(elements) + "}"