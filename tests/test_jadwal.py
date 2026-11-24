
import unittest
from models.jadwal import Jadwal


class TestJadwal(unittest.TestCase):

    def test_jadwal_valid(self):
        jadwal = Jadwal(
            "J001",
            "Pekalongan",
            "Jakarta",
            "25-11-2026",
            "08:00",
            350.0
        )

        self.assertTrue(jadwal.validasi_jadwal())

    def test_asal_dan_tujuan_sama(self):
        jadwal = Jadwal(
            "J002",
            "Pekalongan",
            "Pekalongan",
            "25-11-2026",
            "08:00",
            350.0
        )

        self.assertFalse(jadwal.validasi_jadwal())

    def test_jarak_nol(self):
        jadwal = Jadwal(
            "J003",
            "Pekalongan",
            "Jakarta",
            "25-11-2026",
            "08:00",
            0
        )

        self.assertFalse(jadwal.validasi_jadwal())


if __name__ == "__main__":
    unittest.main()
