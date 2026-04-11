# README - Sistem Pakar Rekomendasi Jurusan

## 1. Ringkasan Program

Program `tugaspraktikumsistempakar.py` adalah aplikasi GUI berbasis Tkinter untuk merekomendasikan jurusan berdasarkan minat pengguna.

Alur program:

1. Pengguna menekan tombol **Mulai Rekomendasi**.
2. Program menampilkan pertanyaan minat satu per satu (jawaban **Ya/Tidak**).
3. Jawaban **Ya** disimpan sebagai kriteria terpilih.
4. Program menghitung skor kecocokan tiap jurusan dari basis pengetahuan.
5. Program menampilkan maksimal 3 jurusan terbaik beserta persentase kecocokan dan saran.

---

## 2. Struktur Basis Pengetahuan

Basis pengetahuan disimpan dalam `database_jurusan` (tipe dictionary) dengan format:

- key: nama jurusan
- value:
  - `kriteria`: daftar minat untuk jurusan tersebut
  - `saran`: saran singkat untuk pengembangan diri

Contoh data:

- **Informatika**: matematika, logika, pemrograman, algoritma
- **Sistem Informasi**: manajemen, komunikasi, pemrograman, basis data
- **Teknik Komputer**: elektronika, pemrograman, jaringan, sistem operasi
- **Ilmu Komputer**: matematika, logika, teori komputasi, pemrograman
- **Teknologi Informasi**: manajemen, komunikasi, pemrograman, basis data

Daftar pertanyaan disimpan pada `semua_kriteria` dalam bentuk tuple `(kode_kriteria, teks_pertanyaan)`.

---

## 3. Mekanisme Inferensi (Skor Kecocokan)

Inferensi dilakukan pada method `proses_hasil` dengan langkah berikut:

1. Untuk setiap jurusan, hitung jumlah kriteria yang cocok:
   - `cocok = jumlah(kriteria_jurusan yang dijawab Ya)`
2. Hitung skor kecocokan:
   - `skor = cocok / jumlah_kriteria_jurusan`
3. Simpan jurusan jika `skor > 0`.
4. Urutkan hasil dari skor tertinggi.
5. Ambil 3 jurusan teratas (`top_hasil = hasil[:3]`).
6. Tampilkan hasil dalam format:
   - Nama jurusan
   - Persentase kecocokan (`int(skor * 100)`)
   - Saran singkat jurusan

Jika tidak ada jurusan dengan skor di atas 0, program menampilkan pesan:
**"Tidak ada jurusan yang cocok dengan kriteria Anda."**

---

## 4. Penjelasan Komponen Program

### Import

- `import tkinter as tk`: untuk komponen GUI.
- `from tkinter import messagebox`: untuk menampilkan pop-up hasil.

### Kelas Utama: `AplikasiPakar`

- `__init__(self, root)`: inisialisasi window, label pertanyaan, tombol mulai, dan tombol jawaban Ya/Tidak.
- `mulai_tanya(self)`: reset state (kriteria terpilih dan indeks pertanyaan), lalu mulai sesi tanya jawab.
- `tampilkan_pertanyaan(self)`: menampilkan pertanyaan berdasarkan indeks aktif.
- `jawab(self, respon)`: menyimpan jawaban Ya ke `kriteria_terpilih`, lalu lanjut ke pertanyaan berikutnya.
- `proses_hasil(self)`: menjalankan inferensi skor, mengurutkan hasil, menyiapkan teks keluaran, dan menampilkan pop-up.

### Entry Point

Bagian `if __name__ == "__main__":` membuat jendela utama, mengatur ukuran `600x400`, dan menjalankan loop Tkinter.

---

## 5. Cara Menjalankan

### Prasyarat

- Python 3 sudah terpasang.
- Tkinter tersedia (umumnya bawaan instalasi Python di Windows).

### Menjalankan Program

Di terminal pada folder proyek:

```bash
python tugaspraktikumsistempakar.py
```

Jika `python` tidak dikenali:

```bash
py tugaspraktikumsistempakar.py
```

### Cara Menggunakan

1. Klik **Mulai Rekomendasi**.
2. Jawab seluruh pertanyaan minat dengan **Ya** atau **Tidak**.
3. Lihat hasil rekomendasi pada pop-up (maksimal 3 jurusan teratas).

---

## 6. Catatan

- Model ini menggunakan pendekatan rule-based dengan skor sederhana.
- Hasil bukan keputusan mutlak, melainkan rekomendasi awal berdasarkan minat yang dipilih pengguna.
