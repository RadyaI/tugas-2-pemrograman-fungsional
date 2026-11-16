import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.index import (
    validasi_angka,
    hitung_total,
    hitung_persen,
    filter_kategori,
    ambil_kolom,
    cari_terbesar,
    cari_terkecil,
)

# APLIKASI 4
# Nama Aplikasi: Inventory Management System (Manajemen Persediaan Barang)
#
# Fungsi yang dipakai:
# - Function 1 (validasi_angka): memvalidasi input harga dan stok barang agar data yang tidak valid dibuang
# - Function 2 (hitung_total): menghitung total nilai persediaan seluruh barang
# - Function 3 (hitung_persen): menghitung persentase jumlah stok berdasarkan kategori barang
# - Function 4 (filter_kategori): memfilter data barang berdasarkan kategori (Elektronik, Alat Tulis, Aksesoris)
# - Function 5 (ambil_kolom): mengambil kolom harga dan stok dari data barang
# - Function 7 (cari_terbesar): mencari barang dengan harga tertinggi
# - Function 8 (cari_terkecil): mencari barang dengan stok paling sedikit

data_mentah = [
    {"nama": "Laptop",     "kategori": "Elektronik", "harga": "7500000", "stok": "5"},
    {"nama": "Mouse",      "kategori": "Elektronik", "harga": "150000",  "stok": "20"},
    {"nama": "Keyboard",   "kategori": "Elektronik", "harga": "250000",  "stok": "15"},
    {"nama": "Buku Tulis", "kategori": "Alat Tulis", "harga": "5000",    "stok": "100"},
    {"nama": "Pulpen",     "kategori": "Alat Tulis", "harga": "3000",    "stok": "abc"},
    {"nama": "Tas",        "kategori": "Aksesoris",  "harga": "175000",  "stok": "10"},
    {"nama": "Jam Tangan", "kategori": "Aksesoris",  "harga": "350000",  "stok": "8"},
]

# 1. Validasi data barang (pakai Function 1), buang data yang tidak valid
def ubah_data(item):
    return {
        **item,
        "harga": validasi_angka(item["harga"]),
        "stok": validasi_angka(item["stok"])
    }

def data_valid(item):
    return (
        item["harga"] is not None
        and item["stok"] is not None
        and item["harga"] >= 0
        and item["stok"] >= 0
    )

data = list(filter(data_valid, map(ubah_data, data_mentah)))
print("Data valid:", len(data), "dari", len(data_mentah))

# 2. Total nilai persediaan (Function 5 + Function 2)
semua_harga = ambil_kolom(data, "harga")
semua_stok = ambil_kolom(data, "stok")

nilai_persediaan = list(map(
    lambda harga, stok: harga * stok,
    semua_harga, semua_stok
))

total = hitung_total(nilai_persediaan)
print("\nTotal nilai persediaan: Rp", f"{total:,.0f}")

# 3. Rekap stok per kategori (Function 4 + 5 + 2 + 3)
total_stok = hitung_total(semua_stok)

def rekap_kategori(kategori):
    item = filter_kategori(data, kategori)
    subtotal = hitung_total(ambil_kolom(item, "stok"))
    persen = hitung_persen(subtotal, total_stok)
    return kategori, subtotal, persen

daftar_kategori = ["Elektronik", "Alat Tulis", "Aksesoris"]

print("\nRekap stok per kategori")
for kategori, subtotal, persen in map(rekap_kategori, daftar_kategori):
    print(f"- {kategori}: {subtotal:.0f} unit ({persen:.2f}%)")

# 4. Barang termahal (Function 7)
terbesar = cari_terbesar(data, "harga")

if terbesar:
    print(
        "\nBarang termahal:",
        terbesar["nama"],
        "- Rp",
        f"{terbesar['harga']:,.0f}"
    )

# 5. Barang termurah (Function 8)
terkecil = cari_terkecil(data, "harga")

if terkecil:
    print(
        "Barang termurah:",
        terkecil["nama"],
        "- Rp",
        f"{terkecil['harga']:,.0f}"
    )

# 6. Stok terbanyak (Function 7)
stok_terbanyak = cari_terbesar(data, "stok")

if stok_terbanyak:
    print(
        "\nStok terbanyak:",
        stok_terbanyak["nama"],
        "-",
        f"{stok_terbanyak['stok']:.0f}",
        "unit"
    )

# 7. Stok paling sedikit (Function 8)
stok_tersedikit = cari_terkecil(data, "stok")

if stok_tersedikit:
    print(
        "Stok paling sedikit:",
        stok_tersedikit["nama"],
        "-",
        f"{stok_tersedikit['stok']:.0f}",
        "unit"
    )