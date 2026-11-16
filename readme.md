# Tugas 2 - Pemrograman Fungsional

Library fungsi Python dengan gaya pemrograman fungsional (`map`, `filter`, `reduce`) beserta 5 aplikasi yang memakainya.

# Tugas 2 - Pemrograman Fungsional

Library fungsi Python dengan gaya pemrograman fungsional (`map`, `filter`, `reduce`) beserta 5 aplikasi yang memakainya.

## Anggota Kelompok

| No | Nama                    | NIM             |
|----|-------------------------|-----------------|
| 1  | Jenita Oktaviana Ramadhani | 202410370110338 |
| 2  | Athallah Rasyad Zaidan  | 202410370110361 |
| 3  | Muhammad Radya Iftikhar | 202410370110370 |

## Struktur Folder

```
tugas_2/
├── readme.md
├── lib/
│   └── index.py        # library berisi 10 function
└── src/
    ├── aplikasi1.py    # Pencatat Pengeluaran Harian
    ├── aplikasi2.py    # Kasir Toko Sederhana
    ├── aplikasi3.py    # Rekap Nilai Mahasiswa
    ├── aplikasi4.py    # Inventory Management System
    └── aplikasi5.py    # Pelacak Jam Belajar
```

## Isi Library (`lib/index.py`)

| No | Function | Kegunaan |
|----|----------|----------|
| 1 | `validasi_angka` | Cek teks bisa jadi angka, kalau tidak valid return `None` |
| 2 | `hitung_total` | Menjumlahkan semua angka dalam list |
| 3 | `hitung_persen` | Menghitung persentase bagian dari total |
| 4 | `filter_kategori` | Mengambil data berdasarkan kategori |
| 5 | `ambil_kolom` | Mengambil satu kolom dari list of dict |
| 6 | `hitung_rata_rata` | Menghitung rata-rata list angka |
| 7 | `cari_terbesar` | Mencari item dengan nilai terbesar pada suatu kolom |
| 8 | `cari_terkecil` | Mencari item dengan nilai terkecil pada suatu kolom |
| 9 | `hitung_total_kategori` | Menghitung total suatu kolom untuk kategori tertentu |
| 10 | `hapus_transaksi` | Menghapus data berdasarkan ID |

Catatan: tidak ada function login, sesuai ketentuan tugas.

## Daftar Aplikasi

| Aplikasi | Nama | Function yang dipakai |
|----------|------|-----------------------|
| 1 | Pencatat Pengeluaran Harian | 1, 2, 3, 4, 5, 6, 7 |
| 2 | Kasir Toko Sederhana | 1, 2, 5, 8, 9, 10 |
| 3 | Rekap Nilai Mahasiswa | 1, 3, 4, 5, 6, 7, 8, 9 |
| 4 | Inventory Management System | 1, 2, 3, 4, 5, 7, 8 |
| 5 | Pelacak Jam Belajar | 1 sampai 10 (semua) |

Setiap aplikasi memvalidasi data mentah dulu (data yang tidak valid dibuang), lalu diolah dan hasilnya dicetak ke terminal.

## Cara Menjalankan

Butuh Python 3.8 ke atas, tanpa library tambahan. Jalankan dari folder `tugas_2`:

```bash
python src/aplikasi1.py
python src/aplikasi2.py
python src/aplikasi3.py
python src/aplikasi4.py
python src/aplikasi5.py
```

Atau lewat module:

```bash
python -m src.aplikasi1
```

`lib/index.py` tidak perlu dijalankan sendiri karena hanya berisi function yang di-import oleh aplikasi.

## Anggota Kelompok

- Nama 1 - NIM
- Nama 2 - NIM
- Nama 3 - NIM