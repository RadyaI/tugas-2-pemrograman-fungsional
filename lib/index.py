from functools import reduce
from operator import add, itemgetter

# LIB
# Isinya 10 function yang dipakai di aplikasi 1-5
# Notes: tidak ada function login


# Function 1
def validasi_angka(teks):
    """Cek apakah teks bisa jadi angka. Return angkanya, atau None kalau tidak valid."""
    try:
        return float(teks)
    except ValueError:
        return None


# Function 2
def hitung_total(daftar_angka):
    """Jumlahkan semua angka dalam list."""
    total = 0
    for angka in daftar_angka:
        total += angka
    return total


# Function 3
def hitung_persen(bagian, total):
    """Hitung persentase bagian dari total."""
    if total == 0:
        return 0
    return (bagian / total) * 100


# Function 4
def filter_kategori(data, kategori):
    """Ambil data pengeluaran yang kategorinya sesuai."""
    def cocok(item):
        return item["kategori"] == kategori
    return list(filter(cocok, data))


# Function 5
def ambil_kolom(data, kolom):
    """Ambil satu kolom dari list dict, hasilnya list nilai."""
    return list(map(itemgetter(kolom), data))


# Function 6
def hitung_rata_rata(daftar_angka):
    """Hitung rata-rata list angka. Kalau kosong, return 0."""
    if not daftar_angka:
        return 0
    return reduce(add, daftar_angka, 0) / len(daftar_angka)


# Function 7
def cari_terbesar(data, kolom):
    """Cari item (dict) dengan nilai terbesar pada kolom tertentu."""
    if not data:
        return None

    def pilih(terbesar, item):
        return item if item[kolom] > terbesar[kolom] else terbesar

    return reduce(pilih, data)


# Function 8
def cari_terkecil(data, kolom):
    """Cari item (dict) dengan nilai terkecil pada kolom tertentu."""
    if not data:
        return None

    def pilih(terkecil, item):
        return item if item[kolom] < terkecil[kolom] else terkecil

    return reduce(pilih, data)


# Function 9
def hitung_total_kategori(data, kategori, kolom):
    """Hitung total nilai pada kolom tertentu untuk kategori tertentu."""
    total = 0

    for item in data:
        if item["kategori"] == kategori:
            total += item[kolom]

    return total


# Function 10
def hapus_transaksi(data, id_transaksi):
    """Menghapus transaksi berdasarkan ID transaksi."""
    data_baru = []

    for item in data:
        if item["id"] != id_transaksi:
            data_baru.append(item)

    return data_baru