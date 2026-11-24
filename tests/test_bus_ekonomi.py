
import unittest
from models.bus_ekonomi import BusEkonomi


class TestBusEkonomi(unittest.TestCase):

    def setUp(self):
        self.bus = BusEkonomi(
            "BE001", "G 1234 AB", 40, 2000
        )

    def test_inheritance_kendaraan(self):
        self.assertEqual(self.bus.kapasitas, 40)

    def test_hitung_tarif(self):
        hasil = self.bus.hitung_tarif(100)
        self.assertEqual(hasil, 200000)

    def test_get_info(self):
        hasil = self.bus.get_info()
        self.assertIn("BE001", hasil)


if __name__ == "__main__":
    unittest.main()
