
class PemesananTiket:
    def __init__(self, id_pemesanan, tanggal_pesan,
                 jumlah_kursi, daftar_kursi,
                 total_harga, status):
        self.id_pemesanan = id_pemesanan
        self.tanggal_pesan = tanggal_pesan
        self.jumlah_kursi = jumlah_kursi
        self.daftar_kursi = daftar_kursi
        self.total_harga = total_harga
        self.status = status

    def pilih_kursi(self, nomor):
        self.daftar_kursi.append(nomor)

    def hitung_total(self):
        return self.total_harga

    def batalkan(self):
        self.status = "Dibatalkan"

    def cetak_tiket(self):
        return (
            f"ID Pemesanan: {self.id_pemesanan}\n"
            f"Tanggal Pesan: {self.tanggal_pesan}\n"
            f"Jumlah Kursi: {self.jumlah_kursi}\n"
            f"Daftar Kursi: {self.daftar_kursi}\n"
            f"Total Harga: Rp{self.total_harga}\n"
            f"Status: {self.status}"
        )
