import unittest
from models.jadwal import Jadwal


class TestJadwal(unittest.TestCase):

    def test_jadwal_dibuat(self):
        jadwal = Jadwal(
            "J001",
            "Pekalongan",
            "Jakarta",
            "25-11-2026",
            "08:00",
            350.0
        )

        self.assertEqual(jadwal.id_jadwal, "J001")
        self.assertEqual(jadwal.asal, "Pekalongan")
        self.assertEqual(jadwal.tujuan, "Jakarta")


if __name__ == "__main__":
    unittest.main()
