import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.index import (
    validasi_angka,
    hitung_total,
    hitung_persen,
    filter_kategori,
    ambil_kolom,
    hitung_rata_rata,
    cari_terbesar,
)

# APLIKASI 1
# Nama Aplikasi: Pencatat Pengeluaran Harian
#
# Fungsi yang dipakai:
# - Function 1 (validasi_angka): validasi input jumlah, data yang tidak valid dibuang
# - Function 2 (hitung_total): menghitung total pengeluaran dan subtotal per kategori
# - Function 3 (hitung_persen): menghitung persentase tiap kategori dari total
# - Function 4 (filter_kategori): memfilter pengeluaran berdasarkan kategori
# - Function 5 (ambil_kolom): mengambil kolom jumlah dari data pengeluaran
# - Function 6 (hitung_rata_rata): menghitung rata-rata per transaksi
# - Function 7 (cari_terbesar): mencari pengeluaran terbesar

data_mentah = [
    {"nama": "Makan siang",    "kategori": "Makanan",      "jumlah": "25000"},
    {"nama": "Ojek online",    "kategori": "Transportasi", "jumlah": "18000"},
    {"nama": "Kopi",           "kategori": "Makanan",      "jumlah": "22000"},
    {"nama": "Bensin",         "kategori": "Transportasi", "jumlah": "50000"},
    {"nama": "Nonton bioskop", "kategori": "Hiburan",      "jumlah": "45000"},
    {"nama": "Makan malam",    "kategori": "Makanan",      "jumlah": "30000"},
    {"nama": "Buku catatan",   "kategori": "Pendidikan",   "jumlah": "abc"},
    {"nama": "Fotokopi",       "kategori": "Pendidikan",   "jumlah": "5000"},
]

# 1. Validasi input (pakai Function 1), buang yang tidak valid
def ubah_jumlah(item):
    return {**item, "jumlah": validasi_angka(item["jumlah"])}

def jumlah_valid(item):
    return item["jumlah"] is not None

data = list(filter(jumlah_valid, map(ubah_jumlah, data_mentah)))
print("Data valid:", len(data), "dari", len(data_mentah))

# 2. Total pengeluaran (Function 5 + Function 2)
semua_jumlah = ambil_kolom(data, "jumlah")
total = hitung_total(semua_jumlah)
print("Total pengeluaran: Rp", f"{total:,.0f}")

# 3. Rekap per kategori (Function 4 + 5 + 2 + 3)
def rekap_kategori(kategori):
    item = filter_kategori(data, kategori)
    subtotal = hitung_total(ambil_kolom(item, "jumlah"))
    persen = hitung_persen(subtotal, total)
    return kategori, subtotal, persen

daftar_kategori = ["Makanan", "Transportasi", "Hiburan", "Pendidikan"]

print("\nRekap per kategori")
for kategori, subtotal, persen in map(rekap_kategori, daftar_kategori):
    print(f"- {kategori}: Rp {subtotal:,.0f} ({persen:.2f}%)")

# 4. Rata-rata (Function 6)
print("\nRata-rata per transaksi: Rp", f"{hitung_rata_rata(semua_jumlah):,.2f}")

# 5. Pengeluaran terbesar (Function 7)
terbesar = cari_terbesar(data, "jumlah")
print("Pengeluaran terbesar:", terbesar["nama"], "- Rp", f"{terbesar['jumlah']:,.0f}")