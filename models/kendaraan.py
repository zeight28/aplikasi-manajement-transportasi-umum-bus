
class Kendaraan:
    def __init__(self, id_kendaraan, plat_nomor,
                 kapasitas, tarif_per_km):

        self.id_kendaraan = id_kendaraan
        self.plat_nomor = plat_nomor
        self.kapasitas = kapasitas
        self.tarif_per_km = tarif_per_km

    def get_info(self):
        return (
            f"ID Kendaraan: {self.id_kendaraan}\n"
            f"Plat Nomor: {self.plat_nomor}\n"
            f"Kapasitas: {self.kapasitas} orang\n"
            f"Tarif per KM: Rp{self.tarif_per_km}"
        )

    def hitung_tarif(self, jarak):
        return self.tarif_per_km * jarak

    def cek_kapasitas(self, jumlah):
        return jumlah <= self.kapasitas
