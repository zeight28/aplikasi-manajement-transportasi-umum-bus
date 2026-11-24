
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
        pass

    def validasi_jadwal(self):
        pass
