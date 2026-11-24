
import unittest
from models.bus_eksekutif import BusEksekutif


class TestBusEksekutif(unittest.TestCase):
    def setUp(self):
        self.bus = BusEksekutif(
            "BX001",
            "G 5678 CD",
            30,
            3000,
            ["AC", "WiFi", "Kursi Reclining"]
        )

    def test_inheritance_kendaraan(self):
        self.assertEqual(self.bus.kapasitas, 30)

    def test_fasilitas(self):
        self.assertEqual(
            self.bus.fasilitas,
            ["AC", "WiFi", "Kursi Reclining"]
        )

    def test_hitung_tarif(self):
        hasil = self.bus.hitung_tarif(100)
        self.assertEqual(hasil, 300000)


if __name__ == "__main__":
    unittest.main()
