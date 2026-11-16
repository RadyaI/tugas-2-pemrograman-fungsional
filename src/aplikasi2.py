import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.index import (
    validasi_angka,
    hitung_total,
    ambil_kolom,
    cari_terkecil,
    hitung_total_kategori,
    hapus_transaksi,
)

# APLIKASI 2
# Nama Aplikasi: Kasir Toko Sederhana
#
# Fungsi yang dipakai:
# - Function 1 (validasi_angka): validasi harga, data yang tidak valid dibuang
# - Function 2 (hitung_total): menghitung total belanja
# - Function 5 (ambil_kolom): mengambil kolom harga dari data belanja
# - Function 8 (cari_terkecil): mencari barang termurah
# - Function 9 (hitung_total_kategori): menghitung total belanja per kategori
# - Function 10 (hapus_transaksi): membatalkan barang berdasarkan ID

data_mentah = [
    {"id": 1, "nama": "Beras 5kg",   "kategori": "Sembako",    "harga": "65000"},
    {"id": 2, "nama": "Minyak",      "kategori": "Sembako",    "harga": "18000"},
    {"id": 3, "nama": "Sabun mandi", "kategori": "Kebersihan", "harga": "7000"},
    {"id": 4, "nama": "Teh botol",   "kategori": "Minuman",    "harga": "5000"},
    {"id": 5, "nama": "Air mineral", "kategori": "Minuman",    "harga": "gratis"},
    {"id": 6, "nama": "Shampo",      "kategori": "Kebersihan", "harga": "15000"},
]

# 1. Validasi harga (pakai Function 1), buang yang tidak valid
def ubah_harga(item):
    return {**item, "harga": validasi_angka(item["harga"])}

def harga_valid(item):
    return item["harga"] is not None

data = list(filter(harga_valid, map(ubah_harga, data_mentah)))
print("Barang valid:", len(data), "dari", len(data_mentah))

# 2. Total belanja (Function 5 + Function 2)
total = hitung_total(ambil_kolom(data, "harga"))
print("Total belanja: Rp", f"{total:,.0f}")

# 3. Total per kategori (Function 9)
print("\nTotal per kategori")
for kategori in ["Sembako", "Kebersihan", "Minuman"]:
    subtotal = hitung_total_kategori(data, kategori, "harga")
    print(f"- {kategori}: Rp {subtotal:,.0f}")

# 4. Batalkan barang ID 3 (Function 10), lalu hitung ulang
data = hapus_transaksi(data, 3)
total_baru = hitung_total(ambil_kolom(data, "harga"))
print("\nSetelah batal 'Sabun mandi', total: Rp", f"{total_baru:,.0f}")

# 5. Barang termurah (Function 8)
termurah = cari_terkecil(data, "harga")
print("Barang termurah:", termurah["nama"], "- Rp", f"{termurah['harga']:,.0f}")