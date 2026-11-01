# Test Case
# Test Case Program Analisis Nilai Kelas

## Tujuan Pengujian

Memastikan program dapat:

- Membaca data dari file.
- Memvalidasi nilai.
- Menghitung statistik kelas.
- Menentukan status ketuntasan.
- Menangani kesalahan input.

---

## Daftar Test Case

| ID | Kategori | Input/Kondisi | Expected Result |
|----|----------|---------------|-----------------|
| TC01 | Normal | Data: 80, 70, 90 | Rata-rata = 80 |
| TC02 | Normal | Data: 85, 78, 92, 65, 100 | Minimum = 65, Maksimum = 100 |
| TC03 | Batas | Nilai = 0 | Nilai diterima sebagai valid |
| TC04 | Batas | Nilai = 100 | Nilai diterima sebagai valid |
| TC05 | Invalid | Nilai = -5 | Nilai ditolak |
| TC06 | Invalid | Nilai = 105 | Nilai ditolak |
| TC07 | Invalid | Nilai = abc | Muncul pesan kesalahan |
| TC08 | Invalid | File tidak ditemukan | Program menampilkan pesan error |
| TC09 | Normal | Semua nilai ≥ 75 | Semua siswa berstatus Tuntas |
| TC10 | Normal | Sebagian nilai < 75 | Jumlah tuntas dan belum tuntas dihitung dengan benar |

---

## Detail Pengujian

### TC01 - Menghitung Rata-rata

Input:

```text
Ayu,80
Budi,70
Citra,90
```

Expected Output:

```text
Rata-rata = 80
```

---

### TC02 - Nilai Minimum dan Maksimum

Input:

```text
Ayu,85
Budi,78
Citra,92
Deni,65
Eka,100
```

Expected Output:

```text
Minimum = 65
Maksimum = 100
```

---

### TC03 - Nilai Batas Bawah

Input:

```text
Ayu,0
```

Expected Output:

```text
Data diterima
```

---

### TC04 - Nilai Batas Atas

Input:

```text
Ayu,100
```

Expected Output:

```text
Data diterima
```

---

### TC05 - Nilai Negatif

Input:

```text
Ayu,-5
```

Expected Output:

```text
Data ditolak
```

---

### TC06 - Nilai Lebih dari 100

Input:

```text
Ayu,105
```

Expected Output:

```text
Data ditolak
```

---

### TC07 - Format Nilai Salah

Input:

```text
Ayu,abc
```

Expected Output:

```text
Data tidak valid
```

---

### TC08 - File Tidak Ditemukan

Input:

```text
baca_data("data_tidak_ada.txt")
```

Expected Output:

```text
Error: File tidak ditemukan
```

---

### TC09 - Semua Siswa Tuntas

Input:

```text
Ayu,80
Budi,85
Citra,90
```

KKM = 75

Expected Output:

```text
Jumlah Tuntas = 3
Jumlah Belum Tuntas = 0
```

---

### TC10 - Sebagian Siswa Belum Tuntas

Input:

```text
Ayu,80
Budi,60
Citra,90
Deni,70
```

KKM = 75

Expected Output:

```text
Jumlah Tuntas = 2
Jumlah Belum Tuntas = 2
```

---

## Kesimpulan Pengujian

Program dinyatakan berhasil apabila:

- Semua test case menghasilkan output sesuai expected result.
- Tidak terjadi crash saat file tidak ditemukan.
- Nilai di luar rentang 0–100 dapat ditangani.
- Statistik dan ketuntasan dihitung dengan benar.