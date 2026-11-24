
class Pelanggan:
    def __init__(self, id_pelanggan, nama,
                 no_hp, riwayat_tiket):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.no_hp = no_hp
        self.riwayat_tiket = riwayat_tiket

    def tambah_riwayat(self, pesanan):
        self.riwayat_tiket.append(pesanan)

    def lihat_riwayat(self):
        return self.riwayat_tiket

    def get_info(self):
        return (
            f"ID Pelanggan: {self.id_pelanggan}\n"
            f"Nama: {self.nama}\n"
            f"No. HP: {self.no_hp}"
        )
