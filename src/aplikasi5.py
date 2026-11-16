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
    cari_terkecil,
    hitung_total_kategori,
    hapus_transaksi,
)

# APLIKASI 5
# Nama Aplikasi: Pelacak Jam Belajar
#
# Fungsi yang dipakai:
# - Function 1 (validasi_angka): validasi durasi belajar, data yang tidak valid dibuang
# - Function 2 (hitung_total): menghitung total waktu belajar
# - Function 3 (hitung_persen): menghitung persentase waktu per mata kuliah dan persentase sesi fokus
# - Function 4 (filter_kategori): memfilter sesi belajar berdasarkan mata kuliah
# - Function 5 (ambil_kolom): mengambil kolom durasi dari data sesi
# - Function 6 (hitung_rata_rata): menghitung rata-rata durasi per sesi
# - Function 7 (cari_terbesar): mencari sesi belajar terlama
# - Function 8 (cari_terkecil): mencari sesi belajar tersingkat
# - Function 9 (hitung_total_kategori): menghitung total menit belajar per mata kuliah
# - Function 10 (hapus_transaksi): membuang sesi yang dibatalkan berdasarkan ID

data_mentah = [
    {"id": 1, "nama": "Baca modul",               "kategori": "Pemfung",        "durasi": "90"},
    {"id": 2, "nama": "Latihan soal",             "kategori": "Pemfung",        "durasi": "60"},
    {"id": 3, "nama": "Ngerjain laporan",         "kategori": "Piranti Cerdas", "durasi": "120"},
    {"id": 4, "nama": "Praktik ESP32",            "kategori": "Piranti Cerdas", "durasi": "150"},
    {"id": 5, "nama": "Baca paper jurnal",        "kategori": "Metpen",         "durasi": "75"},
    {"id": 6, "nama": "Diskusi kelompok",         "kategori": "Metpen",         "durasi": "sebentar"},
    {"id": 7, "nama": "Nonton tutorial",          "kategori": "Pemfung",        "durasi": "45"},
    {"id": 8, "nama": "Belajar sambil ketiduran", "kategori": "Metpen",         "durasi": "30"},
]

# 1. Validasi durasi (pakai Function 1), buang yang tidak valid
def ubah_durasi(item):
    return {**item, "durasi": validasi_angka(item["durasi"])}

def durasi_valid(item):
    return item["durasi"] is not None and item["durasi"] > 0

data = list(filter(durasi_valid, map(ubah_durasi, data_mentah)))
print("Sesi valid:", len(data), "dari", len(data_mentah))

# 2. Total waktu belajar (Function 5 + Function 2)
semua_durasi = ambil_kolom(data, "durasi")
total = hitung_total(semua_durasi)
print("Total waktu belajar:", f"{total:,.0f}", "menit", f"({total / 60:.1f} jam)")

# 3. Rekap per mata kuliah (Function 9 + 3 + 4 + 5 + 6)
def rekap_kategori(kategori):
    subtotal = hitung_total_kategori(data, kategori, "durasi")
    persen = hitung_persen(subtotal, total)
    rata = hitung_rata_rata(ambil_kolom(filter_kategori(data, kategori), "durasi"))
    return kategori, subtotal, persen, rata

daftar_kategori = ["Pemfung", "Piranti Cerdas", "Metpen"]

print("\nRekap per mata kuliah")
for kategori, subtotal, persen, rata in map(rekap_kategori, daftar_kategori):
    print(f"- {kategori}: {subtotal:,.0f} menit ({persen:.2f}%), rata-rata {rata:.2f} menit/sesi")

# 4. Rata-rata durasi per sesi (Function 6)
print("\nRata-rata per sesi:", f"{hitung_rata_rata(semua_durasi):.2f}", "menit")

# 5. Persentase sesi fokus, durasi >= 60 menit (Function 3)
def sesi_fokus(item):
    return item["durasi"] >= 60

jumlah_fokus = len(list(filter(sesi_fokus, data)))
print("Persentase sesi fokus (>= 60 menit):", f"{hitung_persen(jumlah_fokus, len(data)):.2f}%")

# 6. Sesi terlama dan tersingkat (Function 7 + Function 8)
terlama = cari_terbesar(data, "durasi")
tersingkat = cari_terkecil(data, "durasi")
print("Sesi terlama:", terlama["nama"], "-", f"{terlama['durasi']:.0f}", "menit")
print("Sesi tersingkat:", tersingkat["nama"], "-", f"{tersingkat['durasi']:.0f}", "menit")

# 7. Batalkan sesi ID 8 karena tidak efektif (Function 10), lalu hitung ulang
data = hapus_transaksi(data, 8)
durasi_baru = ambil_kolom(data, "durasi")
print("\nSetelah sesi 'Belajar sambil ketiduran' dibatalkan:")
print("Total waktu belajar:", f"{hitung_total(durasi_baru):,.0f}", "menit")
print("Rata-rata per sesi:", f"{hitung_rata_rata(durasi_baru):.2f}", "menit")
print("Sesi tersingkat sekarang:", cari_terkecil(data, "durasi")["nama"])