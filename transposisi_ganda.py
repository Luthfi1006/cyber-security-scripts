# -*- coding: utf-8 -*-
"""
Aplikasi Kriptografi - Transposisi Ganda (Double Columnar Transposition)
Dilengkapi visualisasi proses pembuatan dan penguraian cipher tahap demi tahap.
"""
import tkinter as tk
from tkinter import messagebox
import math

# --- LOGIKA KRIPTOGRAFI DENGAN DETAIL LANGKAH ---

def get_key_order(key):
    """
    Menentukan urutan prioritas kolom berdasarkan urutan abjad karakter kunci.
    Contoh: Kunci 'KUNCI' -> Abjad ['C','I','K','N','U'] -> Urutan [2, 4, 3, 0, 1]
    """
    key = key.upper()
    sorted_key = sorted(list(key))
    order = []
    for char in key:
        idx = sorted_key.index(char)
        order.append(idx)
        sorted_key[idx] = None  # Menangani karakter duplikat pada kunci
    return order

def lcm(a, b):
    """Menghitung Kelipatan Persekutuan Terkecil (KPK) dari dua bilangan."""
    return abs(a * b) // math.gcd(a, b)

def format_grid(key, order, grid):
    """Memformat matriks grid transposisi ke dalam bentuk teks tabel yang rapi."""
    ranks = [o + 1 for o in order]
    lines = []
    header_k = "Kunci   :  " + "  ".join(f"{char:>3}" for char in key)
    header_u = "Urutan  :  " + "  ".join(f"[{r}]" for r in ranks)
    sep_len = max(len(header_k), len(header_u), 38)
    sep = "-" * sep_len
    
    lines.append(header_k)
    lines.append(header_u)
    lines.append(sep)
    for r_idx, row in enumerate(grid, 1):
        lines.append(f"Baris {r_idx:<2}:  " + "  ".join(f"{ch:>3}" for ch in row))
    lines.append(sep)
    return "\n".join(lines)

def encrypt_single_process(text, key, stage_num):
    """Enkripsi transposisi kolom tunggal dengan pencatatan log detail."""
    key = key.upper()
    order = get_key_order(key)
    col_count = len(key)
    row_count = math.ceil(len(text) / col_count)
    pad_len = (col_count * row_count) - len(text)
    padded_text = text + ("X" * pad_len)
    
    grid = [list(padded_text[i:i+col_count]) for i in range(0, len(padded_text), col_count)]
    
    log = []
    log.append(f"[*] TAHAP {stage_num}: ENKRIPSI DENGAN KUNCI \"{key}\"")
    log.append(f"    - Teks Masukan       : {text}")
    log.append(f"    - Dimensi Grid       : {row_count} Baris x {col_count} Kolom (Kapasitas = {row_count * col_count})")
    if pad_len > 0:
        log.append(f"    - Penambahan Padding : Ditambah {pad_len} huruf 'X' -> {padded_text}")
    else:
        log.append("    - Penambahan Padding : Tidak ada (panjang teks pas dengan kapasitas grid)")
        
    log.append("    - Matriks Transposisi:")
    for line in format_grid(key, order, grid).split("\n"):
        log.append("      " + line)
        
    log.append("    - Pembacaan Kolom demi Kolom (Berdasarkan nomor urut abjad [1..N]):")
    cipher_chunks = []
    for rank in range(col_count):
        curr_col = order.index(rank)
        chars = "".join(grid[row][curr_col] for row in range(row_count))
        cipher_chunks.append(chars)
        log.append(f"      * Urutan [{rank+1}] -> Huruf '{key[curr_col]}' (Kolom ke-{curr_col+1}) membaca : {chars}")
        
    stage_cipher = "".join(cipher_chunks)
    log.append(f"    -> Hasil Cipher Tahap {stage_num} : {stage_cipher}\n")
    return stage_cipher, "\n".join(log)

def decrypt_single_process(cipher, key, stage_num):
    """Dekripsi transposisi kolom tunggal dengan pencatatan log detail."""
    key = key.upper()
    order = get_key_order(key)
    col_count = len(key)
    row_count = math.ceil(len(cipher) / col_count)
    
    grid = [[""] * col_count for _ in range(row_count)]
    log = []
    log.append(f"[*] TAHAP {stage_num}: DEKRIPSI DENGAN KUNCI \"{key}\"")
    log.append(f"    - Cipher Masukan     : {cipher}")
    log.append(f"    - Dimensi Grid       : {row_count} Baris x {col_count} Kolom")
    log.append("    - Rekonstruksi Kolom (Mengisikan cipher ke kolom sesuai urutan kunci):")
    
    idx = 0
    for rank in range(col_count):
        curr_col = order.index(rank)
        chunk = cipher[idx : idx + row_count]
        for row in range(row_count):
            grid[row][curr_col] = cipher[idx]
            idx += 1
        log.append(f"      * Urutan [{rank+1}] -> Huruf '{key[curr_col]}' (Kolom ke-{curr_col+1}) diisi teks : {chunk}")
        
    log.append("    - Hasil Rekonstruksi Matriks Grid:")
    for line in format_grid(key, order, grid).split("\n"):
        log.append("      " + line)
        
    recovered_text = "".join("".join(row) for row in grid)
    log.append("    - Pembacaan Teks Secara Baris per Baris (Horizontal):")
    log.append(f"    -> Hasil Penguraian Tahap {stage_num} : {recovered_text}\n")
    return recovered_text, "\n".join(log)

def encrypt_double_detail(text, key1, key2):
    """Enkripsi ganda: Plaintext -> Kunci 1 -> Kunci 2 dengan rincian proses."""
    clean_text = "".join(ch for ch in text if ch.isalpha()).upper()
    k1 = "".join(ch for ch in key1 if ch.isalpha()).upper()
    k2 = "".join(ch for ch in key2 if ch.isalpha()).upper()
    
    if not clean_text:
        raise ValueError("Teks masukan harus memiliki setidaknya satu karakter alfabet!")
    if not k1 or not k2:
        raise ValueError("Kunci 1 dan Kunci 2 harus berupa karakter alfabet!")

    # Penyesuaian panjang awal menggunakan KPK panjang kedua kunci
    target_lcm = lcm(len(k1), len(k2))
    pad_initial = (target_lcm - (len(clean_text) % target_lcm)) % target_lcm
    prepared_text = clean_text + ("X" * pad_initial)
    
    log = []
    log.append("=" * 74)
    log.append("         PROSES ENKRIPSI TRANSPOSISI GANDA (DOUBLE COLUMNAR)")
    log.append("=" * 74)
    log.append(f"[-] Teks Asli            : {text}")
    log.append(f"[-] Teks Bersih          : {clean_text} (Panjang = {len(clean_text)} karakter)")
    log.append(f"[-] Kunci 1              : {k1} (Panjang = {len(k1)})")
    log.append(f"[-] Kunci 2              : {k2} (Panjang = {len(k2)})")
    log.append(f"[-] Kelipatan Grid (KPK) : KPK({len(k1)}, {len(k2)}) = {target_lcm}")
    if pad_initial > 0:
        log.append(f"[-] Padding Awal         : Ditambah {pad_initial} huruf 'X' -> {prepared_text}")
    else:
        log.append("[-] Padding Awal         : Tidak diperlukan (panjang pas dengan kelipatan KPK)")
    log.append("-" * 74 + "\n")
    
    # Eksekusi Tahap 1
    c1, log1 = encrypt_single_process(prepared_text, k1, 1)
    log.append(log1)
    
    # Eksekusi Tahap 2
    c2, log2 = encrypt_single_process(c1, k2, 2)
    log.append(log2)
    
    log.append("=" * 74)
    log.append(f"HASIL CIPHERTEXT AKHIR : {c2}")
    log.append("=" * 74)
    
    return c2, "\n".join(log)

def decrypt_double_detail(cipher, key1, key2):
    """Dekripsi ganda: Ciphertext -> Kunci 2 -> Kunci 1 dengan rincian proses."""
    clean_cipher = "".join(ch for ch in cipher if ch.isalpha()).upper()
    k1 = "".join(ch for ch in key1 if ch.isalpha()).upper()
    k2 = "".join(ch for ch in key2 if ch.isalpha()).upper()
    
    if not clean_cipher:
        raise ValueError("Ciphertext harus memiliki karakter alfabet!")
    if not k1 or not k2:
        raise ValueError("Kunci 1 dan Kunci 2 harus berupa karakter alfabet!")

    # Validasi panjang ciphertext harus kelipatan panjang kunci 2
    if len(clean_cipher) % len(k2) != 0:
        raise ValueError(f"Panjang ciphertext ({len(clean_cipher)}) bukan kelipatan dari panjang Kunci 2 ({len(k2)}).")

    log = []
    log.append("=" * 74)
    log.append("         PROSES DEKRIPSI TRANSPOSISI GANDA (DOUBLE COLUMNAR)")
    log.append("=" * 74)
    log.append(f"[-] Ciphertext Input     : {clean_cipher} (Panjang = {len(clean_cipher)} karakter)")
    log.append(f"[-] Kunci 1              : {k1} (Panjang = {len(k1)})")
    log.append(f"[-] Kunci 2              : {k2} (Panjang = {len(k2)})")
    log.append("[-] Urutan Dekripsi      : Ciphertext -> Dekripsi Kunci 2 -> Dekripsi Kunci 1")
    log.append("-" * 74 + "\n")
    
    # Eksekusi Dekripsi Tahap 1 (Kunci 2)
    d1, log1 = decrypt_single_process(clean_cipher, k2, 1)
    log.append(log1)
    
    # Validasi panjang hasil tahap 1 harus kelipatan panjang kunci 1
    if len(d1) % len(k1) != 0:
        raise ValueError(f"Panjang hasil penguraian Kunci 2 ({len(d1)}) bukan kelipatan Kunci 1 ({len(k1)}).")

    # Eksekusi Dekripsi Tahap 2 (Kunci 1)
    d2, log2 = decrypt_single_process(d1, k1, 2)
    log.append(log2)
    
    # Analisis padding 'X'
    trimmed_d2 = d2.rstrip("X")
    removed_x_count = len(d2) - len(trimmed_d2)

    log.append("=" * 74)
    log.append(f"HASIL PLAINTEXT REKONSTRUKSI : {d2}")
    if removed_x_count > 0:
        log.append(f"Plaintext Bersih (Tanpa Padding 'X') : {trimmed_d2} (Dihapus {removed_x_count} huruf 'X')")
    log.append("=" * 74)
    
    return d2, "\n".join(log)

# --- ANTARMUKA GRAFIS (GUI) DENGAN TKINTER ---

def process_encryption():
    text = txt_input.get("1.0", tk.END).strip()
    k1 = entry_key1.get().strip()
    k2 = entry_key2.get().strip()
    
    if not text or not k1 or not k2:
        messagebox.showwarning("Peringatan", "Teks dan kedua kunci tidak boleh kosong!")
        return

    try:
        cipher_result, log_process = encrypt_double_detail(text, k1, k2)
    except Exception as e:
        messagebox.showerror("Kesalahan", str(e))
        return
        
    txt_output.config(state=tk.NORMAL)
    txt_output.delete("1.0", tk.END)
    txt_output.insert(tk.END, cipher_result)
    txt_output.config(state=tk.DISABLED)
    
    txt_detail.config(state=tk.NORMAL)
    txt_detail.delete("1.0", tk.END)
    txt_detail.insert(tk.END, log_process)
    txt_detail.config(state=tk.DISABLED)
    
    messagebox.showinfo("Berhasil", "Enkripsi Transposisi Ganda berhasil diproses!")

def process_decryption():
    text = txt_input.get("1.0", tk.END).strip()
    k1 = entry_key1.get().strip()
    k2 = entry_key2.get().strip()
    
    if not text or not k1 or not k2:
        messagebox.showwarning("Peringatan", "Teks dan kedua kunci tidak boleh kosong!")
        return

    try:
        plain_result, log_process = decrypt_double_detail(text, k1, k2)
    except Exception as e:
        messagebox.showerror("Kesalahan Dekripsi", str(e))
        return
        
    txt_output.config(state=tk.NORMAL)
    txt_output.delete("1.0", tk.END)
    txt_output.insert(tk.END, plain_result)
    txt_output.config(state=tk.DISABLED)
    
    txt_detail.config(state=tk.NORMAL)
    txt_detail.delete("1.0", tk.END)
    txt_detail.insert(tk.END, log_process)
    txt_detail.config(state=tk.DISABLED)
    
    messagebox.showinfo("Berhasil", "Dekripsi Transposisi Ganda berhasil diproses!")

def salin_hasil():
    hasil = txt_output.get("1.0", tk.END).strip()
    if hasil:
        root.clipboard_clear()
        root.clipboard_append(hasil)
        messagebox.showinfo("Tersalin", "Hasil akhir berhasil disalin ke clipboard!")
    else:
        messagebox.showwarning("Kosong", "Belum ada hasil untuk disalin!")

# Setup Window Utama
root = tk.Tk()
root.title("Aplikasi Kriptografi - Transposisi Ganda")
root.geometry("680x750")
root.minsize(620, 680)
root.configure(bg="#f8f9fa")

# Container Utama
main_frame = tk.Frame(root, bg="#f8f9fa", padx=15, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Judul
lbl_title = tk.Label(main_frame, text="🔒 TRANSPOSISI KOLOM GANDA", font=("Arial", 16, "bold"), bg="#f8f9fa", fg="#2c3e50")
lbl_title.pack(pady=(0, 2))
lbl_sub = tk.Label(main_frame, text="Double Columnar Transposition Cipher dengan Visualisasi Matriks",
                    font=("Arial", 9), bg="#f8f9fa", fg="#7f8c8d")
lbl_sub.pack(pady=(0, 10))

# Area Input Teks
tk.Label(main_frame, text="Masukkan Teks (Plaintext / Ciphertext):", font=("Arial", 10, "bold"), bg="#f8f9fa", fg="#34495e").pack(anchor="w")
txt_input = tk.Text(main_frame, height=3, font=("Consolas", 10), wrap=tk.WORD, bd=1, relief=tk.SOLID)
txt_input.pack(fill=tk.X, pady=(3, 10))

# Frame Input Kunci
frame_keys = tk.Frame(main_frame, bg="#ecf0f1", padx=12, pady=8, bd=1, relief=tk.SOLID)
frame_keys.pack(fill=tk.X, pady=(0, 10))

tk.Label(frame_keys, text="Kunci 1:", font=("Arial", 10, "bold"), bg="#ecf0f1", fg="#2c3e50").grid(row=0, column=0, sticky="w", padx=(0, 6))
entry_key1 = tk.Entry(frame_keys, width=18, font=("Consolas", 11, "bold"))
entry_key1.grid(row=0, column=1, padx=(0, 25))
entry_key1.insert(0, "KUNCI")

tk.Label(frame_keys, text="Kunci 2:", font=("Arial", 10, "bold"), bg="#ecf0f1", fg="#2c3e50").grid(row=0, column=2, sticky="w", padx=(0, 6))
entry_key2 = tk.Entry(frame_keys, width=18, font=("Consolas", 11, "bold"))
entry_key2.grid(row=0, column=3)
entry_key2.insert(0, "BATU")

# Tombol Eksekusi
frame_buttons = tk.Frame(main_frame, bg="#f8f9fa")
frame_buttons.pack(fill=tk.X, pady=(0, 10))

btn_encrypt = tk.Button(frame_buttons, text="🔒 ENKRIPSI GANDA", bg="#27ae60", fg="white",
                        font=("Arial", 10, "bold"), pady=6, cursor="hand2", bd=0, relief=tk.RAISED,
                        command=process_encryption)
btn_encrypt.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

btn_decrypt = tk.Button(frame_buttons, text="🔓 DEKRIPSI GANDA", bg="#2980b9", fg="white",
                        font=("Arial", 10, "bold"), pady=6, cursor="hand2", bd=0, relief=tk.RAISED,
                        command=process_decryption)
btn_decrypt.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

# Area Output Hasil Akhir
frame_out_head = tk.Frame(main_frame, bg="#f8f9fa")
frame_out_head.pack(fill=tk.X)
tk.Label(frame_out_head, text="Hasil Akhir:", font=("Arial", 10, "bold"), bg="#f8f9fa", fg="#34495e").pack(side=tk.LEFT)
btn_copy = tk.Button(frame_out_head, text="📋 Salin", command=salin_hasil,
                     bg="#7f8c8d", fg="white", font=("Arial", 8, "bold"), padx=6, pady=1, bd=0, cursor="hand2")
btn_copy.pack(side=tk.RIGHT)

txt_output = tk.Text(main_frame, height=2, font=("Consolas", 10, "bold"), bg="#ffffff", fg="#2c3e50",
                     bd=1, relief=tk.SOLID, wrap=tk.WORD, state=tk.DISABLED)
txt_output.pack(fill=tk.X, pady=(3, 10))

# Area Log Detail Proses Kriptografi
tk.Label(main_frame, text="Detail Proses Pembuatan / Penguraian Matriks (Step-by-Step):",
         font=("Arial", 10, "bold"), bg="#f8f9fa", fg="#34495e").pack(anchor="w")

frame_detail = tk.Frame(main_frame, bg="#f8f9fa")
frame_detail.pack(fill=tk.BOTH, expand=True, pady=(3, 5))

scroll_y = tk.Scrollbar(frame_detail, orient=tk.VERTICAL)
txt_detail = tk.Text(frame_detail, height=12, font=("Consolas", 9), bg="#1e272e", fg="#00d2d3",
                     padx=8, pady=8, wrap=tk.NONE, yscrollcommand=scroll_y.set, state=tk.DISABLED)
scroll_x = tk.Scrollbar(frame_detail, orient=tk.HORIZONTAL, command=txt_detail.xview)
scroll_y.config(command=txt_detail.yview)
txt_detail.config(xscrollcommand=scroll_x.set)

scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
txt_detail.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root.mainloop()
