import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.index import (
    validasi_angka,
    hitung_persen,
    filter_kategori,
    ambil_kolom,
    hitung_rata_rata,
    cari_terbesar,
    cari_terkecil,
    hitung_total_kategori,
)

# APLIKASI 3
# Nama Aplikasi: Rekap Nilai Mahasiswa
#
# Fungsi yang dipakai:
# - Function 1 (validasi_angka): validasi nilai, data yang tidak valid dibuang
# - Function 3 (hitung_persen): menghitung persentase nilai yang lulus
# - Function 4 (filter_kategori): memfilter nilai berdasarkan jenis penilaian
# - Function 5 (ambil_kolom): mengambil kolom nilai
# - Function 6 (hitung_rata_rata): menghitung rata-rata nilai
# - Function 7 (cari_terbesar): mencari nilai tertinggi
# - Function 8 (cari_terkecil): mencari nilai terendah
# - Function 9 (hitung_total_kategori): menghitung total nilai per jenis penilaian

data_mentah = [
    {"nama": "Tugas 1", "kategori": "Tugas", "nilai": "80"},
    {"nama": "Tugas 2", "kategori": "Tugas", "nilai": "90"},
    {"nama": "Tugas 3", "kategori": "Tugas", "nilai": "tidak ada"},
    {"nama": "Kuis 1",  "kategori": "Kuis",  "nilai": "65"},
    {"nama": "Kuis 2",  "kategori": "Kuis",  "nilai": "75"},
    {"nama": "UTS",     "kategori": "Ujian", "nilai": "70"},
    {"nama": "UAS",     "kategori": "Ujian", "nilai": "85"},
]

# 1. Validasi nilai (pakai Function 1), buang yang tidak valid
def ubah_nilai(item):
    return {**item, "nilai": validasi_angka(item["nilai"])}

def nilai_valid(item):
    return item["nilai"] is not None

data = list(filter(nilai_valid, map(ubah_nilai, data_mentah)))
print("Nilai valid:", len(data), "dari", len(data_mentah))

# 2. Rata-rata keseluruhan (Function 5 + Function 6)
semua_nilai = ambil_kolom(data, "nilai")
print("Rata-rata keseluruhan:", f"{hitung_rata_rata(semua_nilai):.2f}")

# 3. Rekap per jenis penilaian (Function 4 + 5 + 6 + 9)
def rekap_kategori(kategori):
    item = filter_kategori(data, kategori)
    rata = hitung_rata_rata(ambil_kolom(item, "nilai"))
    total_poin = hitung_total_kategori(data, kategori, "nilai")
    return kategori, rata, total_poin

print("\nRekap per jenis penilaian")
for kategori, rata, total_poin in map(rekap_kategori, ["Tugas", "Kuis", "Ujian"]):
    print(f"- {kategori}: rata-rata {rata:.2f}, total poin {total_poin:,.0f}")

# 4. Persentase yang lulus, nilai >= 70 (Function 3)
def lulus(item):
    return item["nilai"] >= 70

jumlah_lulus = len(list(filter(lulus, data)))
print("\nPersentase lulus:", f"{hitung_persen(jumlah_lulus, len(data)):.2f}%")

# 5. Nilai tertinggi dan terendah (Function 7 + Function 8)
tertinggi = cari_terbesar(data, "nilai")
terendah = cari_terkecil(data, "nilai")
print("Nilai tertinggi:", tertinggi["nama"], "-", tertinggi["nilai"])
print("Nilai terendah:", terendah["nama"], "-", terendah["nilai"])