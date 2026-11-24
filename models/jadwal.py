
class Jadwal:
    def __init__(self, id_jadwal, asal, tujuan,
                 tanggal, jam_berangkat, jarak_km):

        self.id_jadwal = id_jadwal
        self.asal = asal
        self.tujuan = tujuan
        self.tanggal = tanggal
        self.jam_berangkat = jam_berangkat
        self.jarak_km = jarak_km

    def get_info(self):
        return (
            f"ID Jadwal: {self.id_jadwal}\n"
            f"Asal: {self.asal}\n"
            f"Tujuan: {self.tujuan}\n"
            f"Tanggal: {self.tanggal}\n"
            f"Jam Berangkat: {self.jam_berangkat}\n"
            f"Jarak: {self.jarak_km} km"
        )

    def validasi_jadwal(self):
        if not self.id_jadwal:
            return False

        if not self.asal or not self.tujuan:
            return False

        if self.asal == self.tujuan:
            return False

        if not self.tanggal or not self.jam_berangkat:
            return False

        if self.jarak_km <= 0:
            return False

        return True
