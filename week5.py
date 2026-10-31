# =========================================================
# Program Pemesanan Tiket Bioskop
# Elemen: Percabangan, Perulangan, Array, dan Fungsi
# =========================================================

# Array Konstanta / Matriks Harga 2D
# Baris 0: Hari Kerja, Baris 1: Akhir Pekan
# Kolom 0: Reguler, Kolom 1: IMAX
MATRIKS_HARGA = [
    [40000, 60000],  # [Reguler, IMAX] Hari Kerja
    [60000, 80000]   # [Reguler, IMAX] Akhir Pekan
]

NAMA_HARI = ["Hari Kerja", "Akhir Pekan"]
NAMA_LAYAR = ["Reguler", "IMAX"]


# --- MODUL PROSES ---
def hitung_harga(idx_hari: int, idx_layar: int, jumlah: int) -> tuple:
    """Fungsi untuk menghitung total biaya berdasarkan input matriks array."""
    harga_satuan = MATRIKS_HARGA[idx_hari][idx_layar]
    subtotal = harga_satuan * jumlah
    return subtotal, harga_satuan


# --- MODUL INPUT (Dengan Validasi Perulangan) ---
def ambil_input_pilihan(pesan: str, batas_maksimal: int) -> int:
    """Fungsi utilitas untuk validasi input angka pilihan pengguna."""
    while True:
        try:
            val = int(input(pesan))
            if 1 <= val <= batas_maksimal:
                return val - 1  # Mengembalikan indeks 0-based
            print(f"Pilihan tidak valid. Masukkan angka 1-{batas_maksimal}.")
        except ValueError:
            print("Input harus berupa angka bulat!")


def ambil_input_jumlah() -> int:
    """Fungsi validasi input jumlah tiket."""
    while True:
        try:
            jumlah = int(input("Masukkan jumlah tiket: "))
            if jumlah > 0:
                return jumlah
            print("Jumlah tiket minimal 1.")
        except ValueError:
            print("Input harus berupa angka bulat!")


# --- MODUL OUTPUT ---
def tampilkan_rekapitulasi(daftar_transaksi: list) -> None:
    """Fungsi untuk menampilkan seluruh transaksi dari array/list."""
    print("\n" + "=" * 50)
    print("         REKAPITULASI PENJUALAN TIKET BIOSKOP         ")
    print("=" * 50)

    if not daftar_transaksi:
        print("Belum ada transaksi yang tercatat.")
        return

    total_pendapatan = 0
    # Perulangan untuk iterasi array transaksi
    for idx, item in enumerate(daftar_transaksi, start=1):
        print(f"{idx}. {item['hari']} | Studio {item['layar']} | "
              f"Qty: {item['jumlah']} pcs | Subtotal: Rp {item['total']:,}")
        total_pendapatan += item['total']

    print("-" * 50)
    print(f"TOTAL PENDAPATAN KESELURUHAN : Rp {total_pendapatan:,}")
    print("=" * 50)


# --- FUNGSI UTAMA ---
def main():
    riwayat_transaksi = []  # Array/List penampung data transaksi

    print("==================================================")
    print("     SISTEM MANAJEMEN TIKET BIOSKOP INTERAKTIF    ")
    print("==================================================")

    # Perulangan utama program
    while True:
        print("\n--- Input Transaksi Baru ---")
        print("Pilih Hari Penayangan:\n 1. Hari Kerja (Senin-Kamis)\n 2. Akhir Pekan (Jumat-Minggu)")
        idx_hari = ambil_input_pilihan("Pilihan Anda (1-2): ", 2)

        print("\nPilih Tipe Layar:\n 1. Reguler\n 2. IMAX")
        idx_layar = ambil_input_pilihan("Pilihan Anda (1-2): ", 2)

        jumlah = ambil_input_jumlah()

        # Pemanggilan Fungsi Proses
        subtotal, harga_satuan = hitung_harga(idx_hari, idx_layar, jumlah)

        # Penyimpanan ke Array List
        transaksi = {
            "hari": NAMA_HARI[idx_hari],
            "layar": NAMA_LAYAR[idx_layar],
            "jumlah": jumlah,
            "total": subtotal
        }
        riwayat_transaksi.append(transaksi)

        print(f"\n[SUKSES] Transaksi ditambahkan! Subtotal: Rp {subtotal:,}")

        # Konfirmasi perulangan transaksi
        lagi = input("\nTambah transaksi lagi? (y/n): ").strip().lower()
        if lagi != 'y':
            break

    # Pemanggilan Fungsi Output Rekapitulasi
    tampilkan_rekapitulasi(riwayat_transaksi)


if __name__ == "__main__":
    main()
