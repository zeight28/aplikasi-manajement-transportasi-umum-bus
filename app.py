
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Pemesanan Tiket Bus",
    page_icon="🚌",
    layout="wide"
)

# Judul aplikasi
st.title("🚌 Sistem Pemesanan Tiket Bus")

# Deskripsi
st.write(
    "Selamat datang di aplikasi pemesanan tiket bus."
)

# Menu utama
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Beranda",
        "Jadwal Bus",
        "Pemesanan Tiket",
        "Riwayat Pemesanan"
    ]
)

# Tampilan berdasarkan menu
if menu == "Beranda":
    st.header("Beranda")
    st.write("Selamat datang di Sistem Pemesanan Tiket Bus!")

elif menu == "Jadwal Bus":
    st.header("Jadwal Bus")
    st.info("Fitur jadwal bus akan dikembangkan.")

elif menu == "Pemesanan Tiket":
    st.header("Pemesanan Tiket")
    st.info("Fitur pemesanan tiket akan dikembangkan.")

elif menu == "Riwayat Pemesanan":
    st.header("Riwayat Pemesanan")
    st.info("Fitur riwayat pemesanan akan dikembangkan.")
