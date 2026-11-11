# aplikasi-manajement-transportasi-umum-bus

```mermaid
classDiagram
    class Produk {
        - nama: str
        - harga: float
        + get_info(): str
    }

    class Kategori {
        - nama: str
        - daftar_produk: list
        + tambah_produk(produk): void
    }

    class Pelanggan {
        - nama: str
        + lihat_produk(): list
    }

    class Pesanan {
        - nomor: str
        - detail: list
        + tambah_produk(produk, jumlah): DetailPesanan
    }

    class DetailPesanan {
        - produk: Produk
        - jumlah: int
        + get_total(): float
    }

    Kategori o-- Produk : Aggregation
    Pelanggan -- Produk : Association
    Pesanan *-- DetailPesanan : Composition
    DetailPesanan --> Produk : Refers
```
