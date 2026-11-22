<div align="center">

# ?? Cryptography Toolkit

**Implementasi algoritma kriptografi klasik dengan GUI interaktif dan visualisasi proses langkah demi langkah.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FF6F00?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## ?? Deskripsi

Repository ini berisi implementasi dua algoritma kriptografi klasik yang dilengkapi dengan **antarmuka grafis (GUI)** dan **visualisasi detail proses** enkripsi & dekripsi. Cocok untuk keperluan pembelajaran, tugas kuliah, maupun referensi studi kriptografi.

## ? Fitur Utama

| Fitur | Keterangan |
|-------|------------|
| ?? **Caesar Cipher** | Enkripsi & dekripsi dengan pergeseran alfabet (shift cipher) |
| ?? **Transposisi Ganda** | Double Columnar Transposition dengan dua kunci |
| ??? **GUI Interaktif** | Antarmuka grafis berbasis Tkinter yang user-friendly |
| ?? **Visualisasi Proses** | Detail langkah-langkah perhitungan ditampilkan secara rinci |
| ?? **Rumus Matematis** | Menampilkan rumus yang digunakan pada setiap operasi |

## ??? Struktur Project

```
Cryptography-Toolkit/
+-- caesar.py               # Implementasi Caesar Cipher + GUI
+-- transposisi_ganda.py    # Implementasi Transposisi Ganda + GUI
+-- requirements.txt        # Dependency project
+-- LICENSE                 # Lisensi MIT
+-- README.md               # Dokumentasi project
```

## ?? Cara Menjalankan

### Prasyarat

- Python 3.8 atau lebih baru
- Library `tkinter` (sudah bawaan Python)

### Instalasi & Penggunaan

```bash
# Clone repository
git clone https://github.com/Luthfi1006/Cryptography-Toolkit.git
cd Cryptography-Toolkit

# Jalankan Caesar Cipher
python caesar.py

# Jalankan Transposisi Ganda
python transposisi_ganda.py
```

## ?? Penjelasan Algoritma

### 1. Caesar Cipher
Algoritma substitusi paling sederhana, di mana setiap huruf dalam plaintext digeser sejumlah posisi tertentu dalam alfabet.

**Rumus:**
- Enkripsi: `C = (P + K) mod 26`
- Dekripsi: `P = (C - K) mod 26`

### 2. Transposisi Ganda (Double Columnar Transposition)
Teknik enkripsi yang menyusun plaintext ke dalam matriks berdasarkan kunci, lalu membaca kolom-kolomnya sesuai urutan alfabet kunci — dilakukan dua kali untuk keamanan lebih tinggi.

## ??? Screenshot

> Jalankan aplikasi untuk melihat GUI interaktif dengan visualisasi proses enkripsi/dekripsi secara real-time.

## ?? Kontribusi

Kontribusi sangat diterima! Silakan:

1. **Fork** repository ini
2. Buat **branch** fitur baru (`git checkout -b fitur-baru`)
3. **Commit** perubahan (`git commit -m "Tambah fitur baru"`)
4. **Push** ke branch (`git push origin fitur-baru`)
5. Buat **Pull Request**

## ?? Lisensi

Project ini dilisensikan di bawah [MIT License](LICENSE).

## ?? Author

**Muhamad Luthfi Abdullah**

[![GitHub](https://img.shields.io/badge/GitHub-Luthfi1006-181717?style=flat-square&logo=github)](https://github.com/Luthfi1006)

---

<div align="center">

? **Jangan lupa kasih star kalau project ini bermanfaat!** ?

</div>
