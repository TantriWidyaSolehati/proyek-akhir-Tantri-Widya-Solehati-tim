# PROPOSAL PROYEK

## 1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Kelas

---

## 2. Latar Belakang

Guru matematika sering mengelola data nilai siswa secara manual sehingga membutuhkan waktu lebih lama untuk menghitung rata-rata, nilai tertinggi, nilai terendah, dan menentukan ketuntasan belajar siswa.

Untuk membantu proses tersebut, diperlukan program sederhana berbasis Python yang dapat membaca data nilai dari file, memvalidasi data, menghitung statistik kelas, menentukan status ketuntasan berdasarkan KKM, serta menghasilkan laporan secara otomatis.

---

## 3. Pengguna dan Tujuan

### Pengguna

Guru Matematika

### Tujuan

Membantu guru dalam:

- Membaca data nilai siswa dari file.
- Menghitung statistik nilai kelas.
- Menentukan status ketuntasan siswa.
- Membuat laporan rekap nilai secara otomatis.

---

## 4. Ruang Lingkup Proyek

### Fitur Wajib

1. Membaca data nilai dari file teks.
2. Memvalidasi nilai agar berada pada rentang 0–100.
3. Menghitung rata-rata nilai kelas.
4. Menentukan nilai maksimum dan minimum.
5. Menghitung jumlah siswa tuntas dan belum tuntas.
6. Menyimpan laporan hasil analisis ke file.

### Batasan Proyek

- Program berjalan melalui terminal/console.
- Data disimpan dalam file teks (.txt).
- Tidak menggunakan database.
- Tidak menggunakan antarmuka GUI atau web.

---

## 5. Kebutuhan Sistem

### Kebutuhan Fungsional

| ID | Kebutuhan | Prioritas |
|----|-----------|------------|
| F01 | Program membaca data nilai dari file | Wajib |
| F02 | Program memvalidasi nilai 0–100 | Wajib |
| F03 | Program menghitung rata-rata nilai | Wajib |
| F04 | Program menghitung nilai minimum dan maksimum | Wajib |
| F05 | Program menentukan ketuntasan berdasarkan KKM | Wajib |
| F06 | Program menyimpan laporan ke file | Wajib |

### Kebutuhan Non Fungsional

- Program mudah digunakan melalui VS Code.
- Pesan error mudah dipahami.
- Struktur kode modular.
- Program dapat diuji menggunakan test case yang sudah dibuat.

---

## 6. IPO (Input - Process - Output)

| Input | Process | Output |
|---------|-----------|-----------|
| File nilai siswa | Membaca file | Data nilai siswa |
| Data nilai | Validasi | Data valid |
| Data valid | Perhitungan statistik | Rata-rata, minimum, maksimum |
| Data valid | Analisis ketuntasan | Jumlah tuntas dan belum tuntas |
| Hasil analisis | Penyimpanan laporan | File laporan |

### Contoh Data Input

```text
Ayu,85
Budi,78
Citra,92
Deni,65
Eka,100
```

---

## 7. Algoritma (Pseudocode)

```text
MULAI

Baca data dari file

Jika file tidak ditemukan:
    tampilkan pesan error
    selesai

Untuk setiap data:
    validasi nilai
    jika valid:
        simpan ke daftar data

Jika tidak ada data valid:
    tampilkan pesan
    selesai

Hitung rata-rata
Hitung nilai maksimum
Hitung nilai minimum

Hitung jumlah siswa tuntas
Hitung jumlah siswa belum tuntas

Tampilkan hasil analisis

Simpan laporan ke file

SELESAI
```

---

## 8. Struktur Program

### Modul dan Fungsi

### data_io.py

- baca_data()
- simpan_laporan()

### utilitas.py

- validasi_nilai()
- tentukan_status()

### analisis.py

- hitung_statistik()
- hitung_ketuntasan()

### main.py

- main()

---

## 9. Struktur Folder

```text
proyek-akhir-nama-tim/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── nilai_contoh.txt
│
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    └── .gitkeep
```

---

## 10. Struktur Data

### List of Dictionary

```python
[
    {"nama": "Ayu", "nilai": 85},
    {"nama": "Budi", "nilai": 78},
    {"nama": "Citra", "nilai": 92}
]
```

### Alasan Pemilihan

- List digunakan untuk menyimpan banyak data siswa.
- Dictionary digunakan untuk menyimpan atribut setiap siswa.
- Mudah diproses menggunakan perulangan.

---

## 11. Test Case

| ID | Kategori | Input/Kondisi | Expected Result |
|----|-----------|----------------|----------------|
| TC01 | Normal | 80,70,90 | Rata-rata = 80 |
| TC02 | Batas | Nilai 0 | Diterima |
| TC03 | Batas | Nilai 100 | Diterima |
| TC04 | Invalid | Nilai 105 | Ditolak |
| TC05 | Invalid | File tidak ditemukan | Error ditangani |
| TC06 | Normal | Semua nilai ≥ KKM | Semua siswa tuntas |

---

## 12. Pembagian Tugas

| Anggota | Tugas |
|----------|---------|
| Anggota 1 | Menyusun proposal dan README |
| Anggota 2 | Membuat modul data_io.py |
| Anggota 3 | Membuat modul analisis.py |
| Anggota 4 | Membuat testing dan dokumentasi |

---

## 13. Jadwal Pelaksanaan

| Minggu | Kegiatan |
|----------|-----------|
| Pertemuan 14 | Penyusunan proposal |
| Antara P14-P15 | Implementasi program |
| Pertemuan 15 | Testing dan debugging |
| Pertemuan 16 | Presentasi proyek |

---

## 14. Repository GitHub

URL Repository:

```text
https://github.com/TantriWidyaSolehati/proyek-akhir-Tantri-Widya-Solehati-tim.git
```
---

## Kesimpulan

Program Rekap dan Analisis Nilai Matematika Kelas dirancang untuk membantu guru dalam mengolah data nilai siswa secara cepat, akurat, dan otomatis. Program ini memanfaatkan konsep Python yang telah dipelajari seperti fungsi, list, dictionary, percabangan, perulangan, dan file handling.