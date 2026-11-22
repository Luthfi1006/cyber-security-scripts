# -*- coding: utf-8 -*-
"""
Aplikasi Kriptografi - Caesar Cipher dengan Tampilan Detail Proses
"""
import tkinter as tk
from tkinter import messagebox

# --- LOGIKA KRIPTOGRAFI DENGAN DETAIL LANGKAH ---

def caesar_cipher_detail(text, shift, mode):
    effective_shift = shift if mode == 'Enkripsi' else -shift
    shift_pos = shift % 26
    steps = []
    result_chars = []
    
    steps.append("=" * 74)
    steps.append(f"            DETAIL PROSES CAESAR CIPHER ({mode.upper()})")
    steps.append("=" * 74)
    steps.append(f"[-] Teks Masukan       : {text}")
    steps.append(f"[-] Nilai Shift (Kunci): {shift}")
    
    if mode == 'Enkripsi':
        steps.append(f"[-] Arah Pergeseran    : Maju (+{shift_pos} posisi alfabet)")
        steps.append(f"[-] Rumus Matematis    : C = (P + {shift_pos}) mod 26")
        calc_op = "+"
    else:
        equiv_forward = (26 - shift_pos) % 26
        steps.append(f"[-] Arah Pergeseran    : Mundur (-{shift_pos} posisi, setara maju +{equiv_forward})")
        steps.append(f"[-] Rumus Matematis    : P = (C - {shift_pos}) mod 26  atau  (C + {equiv_forward}) mod 26")
        calc_op = "-"

    steps.append("-" * 74)
    steps.append(f"{'No':<4} | {'Karakter':<8} | {'Tipe':<12} | {'Posisi':<6} | {'Perhitungan':<22} | {'Hasil'}")
    steps.append("-" * 74)

    for i, char in enumerate(text, start=1):
        if char.isalpha():
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            orig_idx = ord(char) - base
            new_idx = (orig_idx + effective_shift) % 26
            new_char = chr(base + new_idx)
            result_chars.append(new_char)
            tipe = "Kapital" if is_upper else "Kecil"
            calc = f"({orig_idx} {calc_op} {shift_pos}) mod 26 = {new_idx}"
            steps.append(f"{i:<4} | {repr(char):<8} | {tipe:<12} | {orig_idx:<6} | {calc:<22} | {repr(new_char)}")
        else:
            result_chars.append(char)
            steps.append(f"{i:<4} | {repr(char):<8} | Non-Huruf    | {'-':<6} | (Karakter tidak berubah) | {repr(char)}")

    final_result = "".join(result_chars)
    steps.append("-" * 74)
    steps.append(f"HASIL AKHIR : {final_result}")
    steps.append("=" * 74)

    return final_result, "\n".join(steps)

# --- FUNGSI KONTROL GUI ---

def proses():
    pesan = txt_input.get("1.0", tk.END).rstrip("\r\n")
    
    # Validasi input pesan
    if not pesan:
        messagebox.showwarning("Peringatan", "Pesan tidak boleh kosong!")
        return

    # Validasi input shift harus bilangan bulat
    try:
        geser = int(entry_shift.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Jumlah geser (shift) harus berupa angka bilangan bulat!")
        return
        
    mode = var_mode.get()
    hasil, log_proses = caesar_cipher_detail(pesan, geser, mode)
    
    # Tampilkan ke kotak Hasil Akhir
    txt_output.config(state=tk.NORMAL)
    txt_output.delete("1.0", tk.END)
    txt_output.insert(tk.END, hasil)
    txt_output.config(state=tk.DISABLED)
    
    # Tampilkan ke kotak Detail Proses
    txt_detail.config(state=tk.NORMAL)
    txt_detail.delete("1.0", tk.END)
    txt_detail.insert(tk.END, log_proses)
    txt_detail.config(state=tk.DISABLED)
    
    messagebox.showinfo("Berhasil", f"Pesan berhasil di-{mode.lower()}!")

def salin_hasil():
    hasil = txt_output.get("1.0", tk.END).strip()
    if hasil:
        window.clipboard_clear()
        window.clipboard_append(hasil)
        messagebox.showinfo("Tersalin", "Hasil akhir berhasil disalin ke clipboard!")
    else:
        messagebox.showwarning("Kosong", "Belum ada hasil untuk disalin!")

# --- SETUP GUI TKINTER ---

window = tk.Tk()
window.title("Caesar Cipher - Keamanan Siber")
window.geometry("640x720")
window.minsize(580, 650)
window.configure(bg="#2c3e50")

# Header
lbl_title = tk.Label(window, text="[🔒] CAESAR CIPHER", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
lbl_title.pack(pady=(15, 3))
lbl_subtitle = tk.Label(window, text="Kriptografi Substitusi Klasik dengan Visualisasi Proses",
                        font=("Helvetica", 9), bg="#2c3e50", fg="#bdc3c7")
lbl_subtitle.pack(pady=(0, 10))

# Container Utama
main_frame = tk.Frame(window, bg="#2c3e50", padx=15)
main_frame.pack(fill=tk.BOTH, expand=True)

# Area Input Pesan
lbl_input = tk.Label(main_frame, text="Pesan Masukan (Plaintext / Ciphertext):", font=("Helvetica", 10, "bold"), bg="#2c3e50", fg="#ecf0f1")
lbl_input.pack(anchor="w")
txt_input = tk.Text(main_frame, height=4, font=("Consolas", 10), padx=8, pady=8, wrap=tk.WORD)
txt_input.pack(fill=tk.X, pady=(4, 10))

# Kontrol Parameter (Shift & Mode)
frame_params = tk.Frame(main_frame, bg="#34495e", padx=12, pady=8, bd=1, relief=tk.SOLID)
frame_params.pack(fill=tk.X, pady=(0, 10))

# Shift
lbl_shift = tk.Label(frame_params, text="Nilai Shift (Geser):", font=("Helvetica", 10, "bold"), bg="#34495e", fg="#ecf0f1")
lbl_shift.pack(side=tk.LEFT, padx=(0, 6))
entry_shift = tk.Entry(frame_params, width=6, font=("Consolas", 11, "bold"), justify="center")
entry_shift.pack(side=tk.LEFT, padx=(0, 20))
entry_shift.insert(0, "3")

# Mode Radio
lbl_mode = tk.Label(frame_params, text="Mode:", font=("Helvetica", 10, "bold"), bg="#34495e", fg="#ecf0f1")
lbl_mode.pack(side=tk.LEFT, padx=(0, 6))
var_mode = tk.StringVar(value="Enkripsi")
rb_enkrip = tk.Radiobutton(frame_params, text="Enkripsi", variable=var_mode, value="Enkripsi",
                           bg="#34495e", fg="white", selectcolor="#2c3e50", font=("Helvetica", 10))
rb_enkrip.pack(side=tk.LEFT, padx=5)
rb_dekrip = tk.Radiobutton(frame_params, text="Dekripsi", variable=var_mode, value="Dekripsi",
                           bg="#34495e", fg="white", selectcolor="#2c3e50", font=("Helvetica", 10))
rb_dekrip.pack(side=tk.LEFT, padx=5)

# Tombol Proses
btn_proses = tk.Button(main_frame, text="⚡ PROSES PESAN", command=proses,
                       bg="#27ae60", fg="white", font=("Helvetica", 11, "bold"),
                       pady=6, cursor="hand2", bd=0, relief=tk.RAISED)
btn_proses.pack(fill=tk.X, pady=(0, 10))

# Output Teks Hasil Akhir
frame_out_header = tk.Frame(main_frame, bg="#2c3e50")
frame_out_header.pack(fill=tk.X)
lbl_out = tk.Label(frame_out_header, text="Hasil Akhir:", font=("Helvetica", 10, "bold"), bg="#2c3e50", fg="#ecf0f1")
lbl_out.pack(side=tk.LEFT)
btn_copy = tk.Button(frame_out_header, text="📋 Salin", command=salin_hasil,
                     bg="#2980b9", fg="white", font=("Helvetica", 8, "bold"), padx=6, pady=1, bd=0, cursor="hand2")
btn_copy.pack(side=tk.RIGHT)

txt_output = tk.Text(main_frame, height=3, font=("Consolas", 10, "bold"), bg="#ecf0f1", fg="#2c3e50",
                     padx=8, pady=6, wrap=tk.WORD, state=tk.DISABLED)
txt_output.pack(fill=tk.X, pady=(4, 10))

# Area Log Proses Detail dengan Scrollbar
lbl_detail = tk.Label(main_frame, text="Detail Proses Pembuatan / Penguraian Cipher (Step-by-Step):",
                      font=("Helvetica", 10, "bold"), bg="#2c3e50", fg="#ecf0f1")
lbl_detail.pack(anchor="w")

frame_detail = tk.Frame(main_frame, bg="#2c3e50")
frame_detail.pack(fill=tk.BOTH, expand=True, pady=(4, 15))

scroll_y = tk.Scrollbar(frame_detail, orient=tk.VERTICAL)
txt_detail = tk.Text(frame_detail, height=10, font=("Consolas", 9), bg="#1e272e", fg="#00d2d3",
                     padx=8, pady=8, wrap=tk.NONE, yscrollcommand=scroll_y.set, state=tk.DISABLED)
scroll_x = tk.Scrollbar(frame_detail, orient=tk.HORIZONTAL, command=txt_detail.xview)
scroll_y.config(command=txt_detail.yview)
txt_detail.config(xscrollcommand=scroll_x.set)

scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
txt_detail.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    window.mainloop()
