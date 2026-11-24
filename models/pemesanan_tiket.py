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
        pass

    def hitung_total(self):
        pass

    def batalkan(self):
        pass

    def cetak_tiket(self):
        pass
