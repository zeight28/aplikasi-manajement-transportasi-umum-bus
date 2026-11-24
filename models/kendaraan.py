class Kendaraan:
    def __init__(self, id_kendaraan, plat_nomor,
                 kapasitas, tarif_per_km):
        self.id_kendaraan = id_kendaraan
        self.plat_nomor = plat_nomor
        self.kapasitas = kapasitas
        self.tarif_per_km = tarif_per_km

    def get_info(self):
        pass

    def hitung_tarif(self, jarak):
        pass

    def cek_kapasitas(self, jumlah):
        pass
