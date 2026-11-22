# Classical Cryptography Visualizer & Educational Suite

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-brightgreen?style=flat-square)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=flat-square)](https://github.com/Luthfi1006/cyber-security-scripts)

An educational cryptography suite built in Python featuring interactive desktop interfaces and exhaustive, step-by-step mathematical breakdowns of classical cipher algorithms. Designed for computer science students, security researchers, and cryptography enthusiasts.

---

## ?? Overview

Understanding how classical ciphers operate under the hood is fundamental to grasping modern cryptanalysis and information theory. This repository provides standalone implementations of classical substitution and transposition techniques, coupled with dynamic GUI visualizers that decompose encryption and decryption pipelines into deterministic, auditable steps.

### Highlights
- **Zero External Dependencies**: Pure Python implementation leveraging standard libraries (`tkinter`, `math`).
- **Granular Execution Trace**: Displays intermediate states, index mapping, modulo arithmetic calculations, and transposition matrix transformations.
- **Bi-directional Support**: Seamless encryption and decryption with full case-preservation and configurable padding.

---

## ??? Included Algorithms

### 1. Caesar Cipher (`caesar.py`)
A monoalphabetic substitution cipher based on cyclic shifts over modular arithmetic space $\mathbb{Z}_{26}$.

- **Shift Normalization**: Automatically handles shifts $k \in \mathbb{Z}$ by computing $k \pmod{26}$.
- **Mathematical Transparency**:
  $$\text{Encryption: } C_i = (P_i + k) \pmod{26}$$
  $$\text{Decryption: } P_i = (C_i - k) \pmod{26} \equiv (C_i + (26 - (k \pmod{26}))) \pmod{26}$$
- **Inspection View**: Generates a tabular trace showing character indices, ASCII offsets, algebraic substitutions, and post-shift mappings.

### 2. Double Columnar Transposition (`transposisi_ganda.py`)
A complex permutation cipher that arranges plaintext into two consecutive geometric grids governed by independent alphanumeric keys.

- **Dynamic Priority Permutation**: Computes key column ranks $(\pi_1, \pi_2)$ using alphabetical sorting with duplicate resolution.
- **Matrix Visualization**: Real-time rendering of grid dimensions ($r \times c$), padding schemes, and columnar readouts for both Stage 1 and Stage 2 passes.
- **Least Common Multiple (LCM) Bounds**: Analytical evaluation of permutation periodicity and theoretical keyspace.

---

## ?? Repository Structure

```text
cyber-security-scripts/
+-- caesar.py              # Caesar cipher engine & GUI visualizer
+-- transposisi_ganda.py   # Double columnar transposition engine & GUI visualizer
+-- requirements.txt       # Environment specifications
+-- .gitignore             # Standard Python exclusion rules
+-- LICENSE                # MIT License terms
+-- README.md              # Engineering documentation
```

---

## ?? Getting Started

### Prerequisites
- Python 3.8 or higher.
- Tkinter library (bundled by default with standard Python distributions on Windows/macOS).

> **Linux users (Debian/Ubuntu):** If Tkinter is missing, install it via:
> ```bash
> sudo apt-get update && sudo apt-get install -y python3-tk
> ```

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Luthfi1006/cyber-security-scripts.git
   cd cyber-security-scripts
   ```

2. **Launch the Caesar Cipher module:**
   ```bash
   python caesar.py
   ```

3. **Launch the Double Transposition module:**
   ```bash
   python transposisi_ganda.py
   ```

---

## ?? Sample Execution Trace

### Caesar Cipher Trace Output
```text
==========================================================================
                      CAESAR CIPHER PROCESS TRACE (ENCRYPT)
==========================================================================
[-] Input String       : CYBER
[-] Shift Factor (k)   : 3
[-] Shift Direction    : Forward (+3 positions in alphabet)
[-] Algebraic Model    : C = (P + 3) mod 26
--------------------------------------------------------------------------
No   | Char     | Type         | Pos    | Formula                | Output
--------------------------------------------------------------------------
1    | C        | Uppercase    | 2      | (2 + 3) mod 26 = 5     | F
2    | Y        | Uppercase    | 24     | (24 + 3) mod 26 = 1    | B
3    | B        | Uppercase    | 1      | (1 + 3) mod 26 = 4     | E
4    | E        | Uppercase    | 4      | (4 + 3) mod 26 = 7     | H
5    | R        | Uppercase    | 17     | (17 + 3) mod 26 = 20   | U
--------------------------------------------------------------------------
Final Ciphertext: FBEHU
```

---

## ?? Security Disclaimer

The algorithms implemented in this repository are **historical ciphers** intended strictly for **educational and research demonstrations**. They do not provide cryptographic confidentiality against modern cryptanalysis (such as frequency analysis or brute-force search) and **must not be used to protect sensitive or production data**.

For secure communications, industry-standard cryptographic algorithms such as AES-GCM, ChaCha20-Poly1305, and RSA/ECC (via vetted libraries such as `cryptography`) should be utilized.

---

## ?? License

This project is open-source software licensed under the terms of the [MIT License](LICENSE).

---

## ????? Author

**Muhamad Luthfi Abdullah**  
- GitHub: [@Luthfi1006](https://github.com/Luthfi1006)
- Repository: [cyber-security-scripts](https://github.com/Luthfi1006/cyber-security-scripts)
