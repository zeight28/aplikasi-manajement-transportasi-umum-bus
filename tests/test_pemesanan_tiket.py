
import unittest
from models.pemesanan_tiket import PemesananTiket


class TestPemesananTiket(unittest.TestCase):
    def setUp(self):
        self.pesanan = PemesananTiket(
            "PS001",
            "24-11-2026",
            2,
            ["A1", "A2"],
            100000,
            "Berhasil"
        )

    def test_pilih_kursi(self):
        self.pesanan.pilih_kursi("A3")
        self.assertIn("A3", self.pesanan.daftar_kursi)

    def test_hitung_total(self):
        hasil = self.pesanan.hitung_total()
        self.assertEqual(hasil, 100000)

    def test_batalkan(self):
        self.pesanan.batalkan()
        self.assertEqual(self.pesanan.status, "Dibatalkan")

    def test_cetak_tiket(self):
        hasil = self.pesanan.cetak_tiket()
        self.assertIn("PS001", hasil)
        self.assertIn("A1", hasil)
        self.assertIn("100000", hasil)


if __name__ == "__main__":
    unittest.main()
