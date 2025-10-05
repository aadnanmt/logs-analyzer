# 🐧 Automated Linux Log Analyzer

Sebuah tool command-line sederhana yang ditulis dengan Python untuk menganalisis file log di sistem Linux secara otomatis dan menghasilkan laporan ringkas.



---

## ✨ Fitur Utama (Key Features)

* **Analisis Fleksibel**: Menganalisis file log apa pun (`auth.log`, `syslog`, dll.) langsung dari terminal.
* **Pencarian Cerdas**: Mencari beberapa kata kunci atau frasa dalam satu kali proses.
* **Deteksi Gagal Login**: Menghitung dan melaporkan semua upaya login yang gagal dari `auth.log`.
* **Pencarian Error**: Memfilter dan menampilkan pesan error atau warning dari `syslog`.
* **Laporan Otomatis**: Menghasilkan file laporan `.txt` yang bersih dan mudah dibaca, lengkap dengan *timestamp*.

---

## ⚙️ Prasyarat & Instalasi (Prerequisites & Installation)

**Prasyarat:**
* Python 3.8+
* Akses `sudo` (diperlukan untuk membaca file log sistem yang dilindungi).

**Langkah Instalasi:**

1.  **Clone repository ini:**
    ```bash
    git clone https://github.com/aadnanmt/logs-analyzer.git
    cd logs-analyzer
    ```

2.  **Buat dan aktifkan virtual environment (sangat disarankan):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *Catatan: Proyek ini tidak memerlukan library eksternal, jadi tidak ada file `requirements.txt`.*

---

## 🚀 Cara Penggunaan Sederhana (Usage)

1.  **Konfigurasi (jika ada):**
    Buka file `config.ini` dan sesuaikan path file log yang ingin dianalisis.
    ```ini
    [settings]
    log_file_path = /var/log/auth.log
    keywords = Failed password, error
    ```

2.  **Jalankan skrip utama:**
    Pastikan kamu menjalankannya dengan `sudo` agar skrip memiliki izin untuk membaca file log sistem.
    ```bash
    sudo python main.py
    ```
---
## 🚀 Cara Penggunaan Kompleks (Usage)

#### 1. Jalankan Analisis
Jalankan skrip `main.py` dengan `sudo` dan berikan argumen `--file` dan `--keywords`. Skrip akan memberitahukan di mana laporan disimpan.

* **Mencari upaya login yang gagal:**
    ```bash
    sudo python3 main.py --file /var/log/auth.log --keywords "Failed password,invalid user"
    ```
    *Output Terminal:*
    ```
    [*] Analyzing file: /var/log/auth.log
    [+] Report successfully saved to: reports/analysis_report_2025-10-05_17-30-00.txt
    ```

#### 2. Lihat Hasil Laporan
Setelah skrip berjalan, kamu bisa melihat isi laporan langsung dari terminal.

* **Lihat daftar semua laporan yang ada:**
    ```bash
    ls reports/
    ```
    *Contoh Output Terminal:*
    ```
    analysis_report_2025-10-05_17-30-00.txt
    ```

* **Tampilkan isi salah satu laporan menggunakan `cat`:**
    ```bash
    cat reports/analysis_report_2025-10-05_17-30-00.txt
    ```
    *Contih Output Terminal:*
    ```
    Log Analysis Report - 2025-10-05 17:30:00
    ========================================

    Found 5 matching entries:

    - Oct  5 17:29:01 my-server sshd[1234]: Failed password for invalid user admin from 10.0.2.2
    ... (dan seterusnya)
    ```
