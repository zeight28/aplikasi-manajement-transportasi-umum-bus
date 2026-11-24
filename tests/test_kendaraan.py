
import unittest
from models.kendaraan import Kendaraan


class TestKendaraan(unittest.TestCase):

    def setUp(self):
        self.kendaraan = Kendaraan(
            "K001", "G 1234 AB", 40, 2000
        )

    def test_hitung_tarif(self):
        hasil = self.kendaraan.hitung_tarif(100)
        self.assertEqual(hasil, 200000)

    def test_kapasitas_cukup(self):
        self.assertTrue(
            self.kendaraan.cek_kapasitas(30)
        )

    def test_kapasitas_penuh(self):
        self.assertTrue(
            self.kendaraan.cek_kapasitas(40)
        )

    def test_kapasitas_melebihi(self):
        self.assertFalse(
            self.kendaraan.cek_kapasitas(45)
        )


if __name__ == "__main__":
    unittest.main()
