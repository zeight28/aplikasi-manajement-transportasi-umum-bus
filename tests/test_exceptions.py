
import unittest
from exceptions.exceptions import (
    KursiPenuhError,
    PelangganTidakTerdaftarError
)


class TestCustomExceptions(unittest.TestCase):

    def test_kursi_penuh_error(self):
        with self.assertRaises(KursiPenuhError):
            raise KursiPenuhError("Kursi sudah penuh")

    def test_pelanggan_tidak_terdaftar_error(self):
        with self.assertRaises(PelangganTidakTerdaftarError):
            raise PelangganTidakTerdaftarError(
                "Pelanggan tidak terdaftar"
            )


if __name__ == "__main__":
    unittest.main()
