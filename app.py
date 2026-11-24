
import streamlit as st

import re

def buat_id_jadwal(tanggal, jam, asal, tujuan):
    daftar_hari = [
        "SEN", "SEL", "RAB", "KAM",
        "JUM", "SAB", "MIN"
    ]

    hari = daftar_hari[tanggal.weekday()]

    asal_id = re.sub(r"[^A-Z0-9]+", "-", asal.upper()).strip("-")
    tujuan_id = re.sub(r"[^A-Z0-9]+", "-", tujuan.upper()).strip("-")

    return (
        f"JAD-{hari}-{tanggal.strftime('%Y%m%d')}-"
        f"{jam.strftime('%H%M')}-{asal_id}-{tujuan_id}"
    )

from models.jadwal import Jadwal

st.set_page_config(
    page_title="Sistem Pemesanan Tiket Bus",
    page_icon="🚌",
    layout="wide"
)

st.title("🚌 Sistem Pemesanan Tiket Bus")

menu = st.sidebar.radio(
    "Menu",
    [
        "Beranda",
        "Jadwal Bus",
        "Pemesanan Tiket",
        "Riwayat Pemesanan"
    ]
)

if "daftar_jadwal" not in st.session_state:
    st.session_state.daftar_jadwal = []


if menu == "Beranda":
    st.header("Selamat Datang!")
    st.write("Aplikasi Sistem Pemesanan Tiket Bus.")


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

    for jadwal in st.session_state.daftar_jadwal:
        st.text(jadwal.get_info())
        st.divider()

elif menu == "Pemesanan Tiket":
    st.header("Pemesanan Tiket")
    st.info("Fitur pemesanan tiket akan diintegrasikan berikutnya.")

elif menu == "Riwayat Pemesanan":
    st.header("Riwayat Pemesanan")
    st.info("Fitur riwayat pemesanan akan diintegrasikan berikutnya.")
