# README - Sistem Pakar Rekomendasi Jurusan

## 1. Fungsi Program (Singkat)

Program `tugaspraktikumsistempakar.py` adalah aplikasi GUI sederhana berbasis Tkinter untuk **merekomendasikan jurusan** berdasarkan minat pengguna.

Alur utamanya:
1. Pengguna menekan tombol **Mulai Rekomendasi**.
2. Program menampilkan pertanyaan minat satu per satu (Ya/Tidak).
3. Jawaban **Ya** disimpan sebagai kriteria yang dipilih pengguna.
4. Setelah semua pertanyaan selesai, program membandingkan kriteria pengguna dengan syarat tiap jurusan.
5. Program menampilkan jurusan yang cocok (atau pesan jika tidak ada yang cocok).

---

## 2. Penjelasan Program per Baris (Ringkas)

Berikut penjelasan berdasarkan isi file `tugaspraktikumsistempakar.py`.

### Import
- Baris 1: `import tkinter as tk` -> memanggil pustaka Tkinter untuk membuat tampilan GUI.
- Baris 2: `from tkinter import messagebox` -> memanggil kotak dialog pop-up untuk menampilkan hasil.

### Basis Pengetahuan Jurusan
- Baris 4-10: `database_jurusan` berisi pasangan:
	- kunci: nama jurusan,
	- nilai: daftar kriteria wajib untuk jurusan tersebut.

Contoh:
- Informatika membutuhkan minat: matematika, logika, pemrograman, algoritma.
- Sistem Informasi membutuhkan minat: manajemen, komunikasi, pemrograman, basis_data.

### Daftar Pertanyaan
- Baris 12-24: `semua_kriteria` berisi daftar tuple `(kode_kriteria, teks_pertanyaan)`.
- Daftar ini digunakan sebagai urutan pertanyaan yang ditampilkan ke pengguna.

### Kelas Utama Aplikasi
- Baris 26: deklarasi kelas `AplikasiPakar`.

#### Method `__init__`
- Baris 27: konstruktor kelas menerima objek jendela `root`.
- Baris 28: menyimpan root ke `self.root`.
- Baris 29: memberi judul jendela.
- Baris 30: inisialisasi list `kriteria_terpilih` untuk menyimpan jawaban Ya.
- Baris 31: inisialisasi indeks pertanyaan dimulai dari 0.
- Baris 33-34: membuat label awal selamat datang.
- Baris 36-37: membuat tombol mulai yang memanggil `mulai_tanya`.
- Baris 39-44: membuat frame jawaban berisi tombol Ya dan Tidak, masing-masing memanggil `jawab("y")` dan `jawab("t")`.

#### Method `mulai_tanya`
- Baris 46-51:
	- reset daftar kriteria dan indeks pertanyaan,
	- sembunyikan tombol mulai,
	- tampilkan tombol jawaban,
	- panggil `tampilkan_pertanyaan()`.

#### Method `tampilkan_pertanyaan`
- Baris 53-58:
	- jika pertanyaan masih ada, ambil teks pertanyaan sesuai indeks dan tampilkan di label,
	- jika sudah habis, lanjut ke `proses_hasil()`.

#### Method `jawab`
- Baris 60-67:
	- jika jawaban Ya (`"y"`), ambil kode kriteria dari pertanyaan saat ini lalu simpan ke `kriteria_terpilih`,
	- naikkan indeks pertanyaan,
	- tampilkan pertanyaan berikutnya.

#### Method `proses_hasil`
- Baris 69-85:
	- siapkan list `hasil`,
	- cek setiap jurusan di `database_jurusan`,
	- gunakan `all(...)` untuk memastikan semua syarat jurusan ada di `kriteria_terpilih`,
	- jika cocok, jurusan ditambahkan ke `hasil`.
- Baris 76-79: jika ada hasil, gabungkan nama jurusan; jika tidak, tampilkan pesan tidak cocok.
- Baris 81: menampilkan hasil dengan `messagebox.showinfo`.
- Baris 83-85: reset tampilan ke kondisi awal (frame jawaban disembunyikan, tombol mulai muncul lagi, label kembali ke teks awal).

### Titik Masuk Program
- Baris 87: memastikan kode di bawah berjalan hanya saat file dijalankan langsung.
- Baris 88: membuat jendela Tkinter.
- Baris 89: mengatur ukuran jendela 600x400.
- Baris 90: membuat objek aplikasi dari kelas `AplikasiPakar`.
- Baris 91: menjalankan loop utama GUI.

---

## 3. Cara Menjalankan Program

### Prasyarat
- Sudah terpasang Python 3.
- Tkinter tersedia (umumnya sudah termasuk instalasi Python standar di Windows).

### Langkah Menjalankan (Windows)
1. Buka terminal di folder proyek.
2. Jalankan perintah berikut:

```bash
python tugaspraktikumsistempakar.py
```

Jika perintah `python` tidak dikenali, coba:

```bash
py tugaspraktikumsistempakar.py
```

### Cara Pakai Singkat
1. Klik **Mulai Rekomendasi**.
2. Jawab semua pertanyaan dengan **Ya** atau **Tidak**.
3. Tunggu pop-up hasil rekomendasi jurusan.

---

## 4. Catatan Logika Rekomendasi

Logika saat ini memakai pendekatan **aturan ketat (strict matching)**:
- Satu jurusan akan direkomendasikan hanya jika **semua** kriterianya terpenuhi.
- Jika ada satu syarat jurusan yang tidak dipilih, jurusan tersebut tidak masuk hasil.

Pendekatan ini cocok untuk latihan sistem pakar berbasis aturan sederhana.
