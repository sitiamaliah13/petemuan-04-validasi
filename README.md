# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Siti Amaliah  
NIM: 2225250223  
Kelas: 3E  

## Tujuan

Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Struktur Program

Program pada Pertemuan 04 terdiri dari latihan dan praktik:

- `latihan/01_predikat_nilai.py`
- `latihan/02_kategori_bilangan.py`
- `latihan/03_validasi_rentang.py`
- `latihan/04_validasi_tipe.py`
- `latihan/05_klasifikasi_segitiga_sudut.py`
- `praktik/validasi_klasifikasi_nilai.py`

## Tabel Keputusan

| Kondisi | Keputusan |
|---|---|
| Nilai akhir >= 85 | Predikat A |
| Nilai akhir >= 70 | Predikat B |
| Nilai akhir >= 60 | Predikat C |
| Nilai akhir >= 50 | Predikat D |
| Nilai akhir < 50 | Predikat E |
| Kehadiran < 80% | Tidak memenuhi syarat kehadiran |
| Predikat A, B, atau C | Lulus |
| Predikat D atau E | Belum lulus |

## Perhitungan Nilai Akhir

Nilai akhir dihitung dengan rumus:

`Nilai akhir = 0.6 × nilai ujian + 0.4 × nilai tugas`

Kehadiran minimal yang harus dipenuhi adalah 80%.

## Tabel Pengujian Praktik

| Masukan | Keluaran Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| 90, 80, 95 | Nilai akhir 86.00, Predikat A, Lulus | Nilai akhir 86.00, Predikat A, Lulus | Sesuai |
| 75, 70, 85 | Nilai akhir 73.00, Predikat B, Lulus | Nilai akhir 73.00, Predikat B, Lulus | Sesuai |
| 60, 60, 80 | Nilai akhir 60.00, Predikat C, Lulus | Nilai akhir 60.00, Predikat C, Lulus | Sesuai |
| 55, 50, 90 | Nilai akhir 53.00, Predikat D, Belum lulus | Nilai akhir 53.00, Predikat D, Belum lulus | Sesuai |
| 40, 30, 100 | Nilai akhir 36.00, Predikat E, Belum lulus | Nilai akhir 36.00, Predikat E, Belum lulus | Sesuai |
| 90, 90, 75 | Nilai akhir 90.00, Tidak memenuhi syarat kehadiran | Nilai akhir 90.00, Tidak memenuhi syarat kehadiran | Sesuai |
| 105, 80, 90 | Penolakan rentang nilai ujian | Penolakan rentang nilai ujian | Sesuai |
| 80, -5, 90 | Penolakan rentang nilai tugas | Penolakan rentang nilai tugas | Sesuai |
| 80, 80, abc | Penolakan tipe | Penolakan tipe | Sesuai |

## Kesimpulan

Program berhasil menerapkan seleksi multi-kondisi menggunakan if-elif-else serta validasi tipe dan rentang input. Program juga dapat menghitung nilai akhir, menentukan predikat, dan menentukan status berdasarkan nilai akhir serta persyaratan kehadiran.