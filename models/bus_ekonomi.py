
from .kendaraan import Kendaraan


class BusEkonomi(Kendaraan):

    def hitung_tarif(self, jarak):
        return super().hitung_tarif(jarak)
