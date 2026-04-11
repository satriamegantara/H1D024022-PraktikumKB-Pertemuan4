import tkinter as tk
from tkinter import messagebox

database_jurusan = {
    "Informatika": {"kriteria": ["matematika", "logika", "pemrograman", "algoritma"], "saran": "Perbanyak latihan coding dan pemecahan masalah berbasis algoritma."
    },
    "Sistem Informasi": {"kriteria": ["manajemen", "komunikasi", "pemrograman", "basis_data"],"saran": "Perkuat analisis bisnis, komunikasi tim, dan pemodelan data."
    },
    "Teknik Komputer": {"kriteria": ["elektronika", "pemrograman", "jaringan", "sistem_operasi"], "saran": "Fokus pada praktik perangkat keras, jaringan, dan sistem embedded."
    },
    "Ilmu Komputer": {"kriteria": ["matematika", "logika", "teori_komputasi", "pemrograman"], "saran": "Dalami teori komputasi, struktur data, dan analisis matematika."
    },
    "Teknologi Informasi": {"kriteria": ["manajemen", "komunikasi", "pemrograman", "basis_data"], "saran": "Kembangkan kemampuan implementasi sistem dan layanan TI di organisasi."
    }
}

semua_kriteria = [
    ("matematika", "Apakah Anda suka matematika?"),
    ("logika", "Apakah Anda suka logika?"),
    ("pemrograman", "Apakah Anda suka pemrograman?"),
    ("algoritma", "Apakah Anda suka algoritma?"),
    ("manajemen", "Apakah Anda suka manajemen?"),
    ("komunikasi", "Apakah Anda suka komunikasi?"),
    ("basis_data", "Apakah Anda suka basis data?"),
    ("elektronika", "Apakah Anda suka elektronika?"),
    ("jaringan", "Apakah Anda suka jaringan?"),
    ("sistem_operasi", "Apakah Anda suka sistem operasi?"),
    ("teori_komputasi", "Apakah Anda suka teori komputasi?")
]

class AplikasiPakar:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Rekomendasi Jurusan")
        self.kriteria_terpilih = []
        self.index_pertanyaan = 0

        self.label_tanya=tk.Label(root, text="Selamat datang di Sistem Pakar Rekomendasi Jurusan", font=("Arial", 14))
        self.label_tanya.pack(pady=10)

        self.btn_mulai=tk.Button(root, text="Mulai Rekomendasi", command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        self.frame_jawaban=tk.Frame(root)
        self.btn_ya=tk.Button(self.frame_jawaban, text="Ya", width=10, command=lambda: self.jawab("y"))
        self.btn_tidak=tk.Button(self.frame_jawaban, text="Tidak", width=10, command=lambda: self.jawab("t"))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.kriteria_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_kriteria):
            _, teks = semua_kriteria[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == "y":
            kode=semua_kriteria[self.index_pertanyaan][0]
            self.kriteria_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()
    
    def proses_hasil(self):
        hasil = []
        for jurusan, data in database_jurusan.items():
            syarat = data["kriteria"]
            cocok = sum(1 for k in syarat if k in self.kriteria_terpilih)
            skor = cocok / len(syarat)
            if skor > 0:
                hasil.append((jurusan, skor, data["saran"]))

        if hasil:
            hasil.sort(key=lambda x: x[1], reverse=True)
            top_hasil = hasil[:3]

            baris = []
            for jurusan, skor, saran in top_hasil:
                persen = int(skor * 100)
                baris.append(f"Jurusan: {jurusan}\nKecocokan: {persen}%\nSaran: {saran}")
            kesimpulan = "\n\n".join(baris)
        else:
            kesimpulan = "Tidak ada jurusan yang cocok dengan kriteria Anda."
        
        messagebox.showinfo("Hasil Rekomendasi", kesimpulan)

        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Selamat datang di Sistem Pakar Rekomendasi Jurusan")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = AplikasiPakar(root)
    root.mainloop()