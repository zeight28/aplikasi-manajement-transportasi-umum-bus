
import unittest
from models.pelanggan import Pelanggan


class TestPelanggan(unittest.TestCase):
    def setUp(self):
        self.pelanggan = Pelanggan(
            "P001",
            "Nibras",
            "081234567890",
            []
        )

    def test_tambah_riwayat(self):
        self.pelanggan.tambah_riwayat("Tiket001")
        self.assertEqual(
            self.pelanggan.lihat_riwayat(),
            ["Tiket001"]
        )

    def test_lihat_riwayat(self):
        self.assertEqual(
            self.pelanggan.lihat_riwayat(),
            []
        )

    def test_get_info(self):
        hasil = self.pelanggan.get_info()
        self.assertIn("P001", hasil)
        self.assertIn("Nibras", hasil)
        self.assertIn("081234567890", hasil)


if __name__ == "__main__":
    unittest.main()
