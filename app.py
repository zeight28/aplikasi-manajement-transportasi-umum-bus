
import streamlit as st
from datetime import date, time, datetime

def buat_id_jadwal(tanggal, jam, asal, tujuan):
    daftar_hari = [
        "SEN", "SEL", "RAB", "KAM",
        "JUM", "SAB", "MIN"
    ]

    hari = daftar_hari[tanggal.weekday()]

    asal_id = asal.upper()[:3]
    tujuan_id = tujuan.upper()[:3]

    return (
        f"JAD-{hari}-{tanggal.strftime('%Y%m%d')}-"
        f"{jam.strftime('%H%M')}-{asal_id}-{tujuan_id}"
    )

from models.jadwal import Jadwal
from models.kendaraan import Kendaraan
from models.bus_ekonomi import BusEkonomi
from models.bus_eksekutif import BusEksekutif

st.set_page_config(
    page_title="Sistem Pemesanan Tiket Bus",
    page_icon="🚌",
    layout="wide"
)
st.write("VERSI APP: ID OTOMATIS")

st.title("🚌 Sistem Pemesanan Tiket Bus")

menu = st.sidebar.radio(
    "Menu",
    [
        "Beranda",
        "Jadwal Bus",
        "Data Kendaraan",
        "Pemesanan Tiket",
        "Riwayat Pemesanan"
    ]
)

if "jadwal_awal_dimuat" not in st.session_state:
    st.session_state.daftar_jadwal = [
        Jadwal(
            buat_id_jadwal(
                date(2026, 11, 26),
                time(8, 0),
                "Pekalongan",
                "Semarang"
            ),
            "Pekalongan",
            "Semarang",
            "26-11-2026",
            "08:00",
            100
        ),
        Jadwal(
            buat_id_jadwal(
                date(2026, 11, 26),
                time(9, 0),
                "Tegal",
                "Purwokerto"
            ),
            "Tegal",
            "Purwokerto",
            "26-11-2026",
            "09:00",
            110
        ),
        Jadwal(
            buat_id_jadwal(
                date(2026, 11, 26),
                time(10, 0),
                "Semarang",
                "Solo"
            ),
            "Semarang",
            "Solo",
            "26-11-2026",
            "10:00",
            105
        )
    ]

    st.session_state.jadwal_awal_dimuat = True

if "daftar_kendaraan" not in st.session_state:
    st.session_state.daftar_kendaraan = []

for jadwal in st.session_state.daftar_jadwal[:3]:
    tanggal_obj = datetime.strptime(
        jadwal.tanggal, "%d-%m-%Y"
    ).date()

    jam_obj = datetime.strptime(
        jadwal.jam_berangkat, "%H:%M"
    ).time()

    jadwal.id_jadwal = buat_id_jadwal(
        tanggal_obj,
        jam_obj,
        jadwal.asal,
        jadwal.tujuan
    )

if menu == "Beranda":
    st.header("Selamat Datang!")
    st.write("Aplikasi Sistem Pemesanan Tiket Bus.")

elif menu == "Data Kendaraan":
    st.header("Data Kendaraan")

    with st.form("form_kendaraan"):
        jenis_bus = st.selectbox(
            "Jenis Bus",
            ["Ekonomi", "Eksekutif"]
        )

        id_kendaraan = st.text_input("ID Kendaraan")
        plat_nomor = st.text_input("Plat Nomor")

        kapasitas = st.number_input(
            "Kapasitas",
            min_value=1,
            step=1
        )

        tarif = st.number_input(
            "Tarif per KM",
            min_value=0,
            step=1000
        )

        fasilitas = ""

        if jenis_bus == "Eksekutif":
            fasilitas = st.text_input("Fasilitas Bus")

        submit = st.form_submit_button("Tambah Kendaraan")

        if submit:
            if jenis_bus == "Ekonomi":
                kendaraan = BusEkonomi(
                    id_kendaraan,
                    plat_nomor,
                    kapasitas,
                    tarif
                )
            else:
                kendaraan = BusEksekutif(
                    id_kendaraan,
                    plat_nomor,
                    kapasitas,
                    tarif,
                    fasilitas
                )

            st.session_state.daftar_kendaraan.append(kendaraan)
            st.success("Kendaraan berhasil ditambahkan!")

    st.subheader("Daftar Kendaraan")

    for kendaraan in st.session_state.daftar_kendaraan:
        st.text(kendaraan.get_info())

        if isinstance(kendaraan, BusEksekutif):
            st.write("Fasilitas:", kendaraan.fasilitas)

        st.divider()

elif menu == "Jadwal Bus":
    st.header("Jadwal Bus")

    with st.form("form_jadwal"):
        asal = st.text_input("Kota Asal")
        tujuan = st.text_input("Kota Tujuan")

        tanggal = st.date_input("Tanggal Keberangkatan")
        jam = st.time_input("Jam Keberangkatan")

        jarak = st.number_input(
            "Jarak (KM)",
            min_value=0.0
        )

        submit = st.form_submit_button("Tambah Jadwal")

        if submit:
            id_jadwal = buat_id_jadwal(
                tanggal, jam, asal, tujuan
            )

            jadwal = Jadwal(
                id_jadwal,
                asal,
                tujuan,
                tanggal.strftime("%d-%m-%Y"),
                jam.strftime("%H:%M"),
                jarak
            )

            if jadwal.validasi_jadwal():
                st.session_state.daftar_jadwal.append(jadwal)
                st.success(
                    f"Jadwal berhasil ditambahkan! ID: {id_jadwal}"
                )
            else:
                st.error("Data jadwal tidak valid.")

    st.subheader("Daftar Jadwal")

    st.write("Jumlah jadwal:", len(st.session_state.daftar_jadwal))

    for jadwal in st.session_state.daftar_jadwal:
        st.text(jadwal.get_info())
        st.divider()

elif menu == "Pemesanan Tiket":
    st.header("Pemesanan Tiket")
    st.info("Fitur pemesanan tiket akan diintegrasikan berikutnya.")

elif menu == "Riwayat Pemesanan":
    st.header("Riwayat Pemesanan")
    st.info("Fitur riwayat pemesanan akan diintegrasikan berikutnya.")
