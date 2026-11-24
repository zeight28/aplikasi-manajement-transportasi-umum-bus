from kendaraan import Kendaraan

class BusEksekutif(Kendaraan):
    def __init__(self, id_kendaraan, plat_nomor,
                 kapasitas, tarif_per_km, fasilitas):
        super().__init__(
            id_kendaraan, plat_nomor,
            kapasitas, tarif_per_km
        )
        self.fasilitas = fasilitas

    def hitung_tarif(self, jarak):
        pass
