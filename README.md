# 🐧 Automated Linux Log Analyzer

Sebuah tool command-line sederhana yang ditulis dengan Python untuk menganalisis file log sistem Linux secara otomatis dan menghasilkan laporan ringkas.



---

## ✨ Fitur Utama (Key Features)

* **Analisis Cepat**: Secara otomatis membaca file log (`auth.log`, `syslog`, dll.) untuk mencari event penting.
* **Deteksi Gagal Login**: Menghitung dan melaporkan semua upaya login yang gagal dari `auth.log`.
* **Pencarian Error**: Memfilter dan menampilkan pesan error atau warning dari `syslog`.
* **Laporan Simpel**: Menghasilkan output laporan yang bersih dan mudah dibaca di terminal.

---

## ⚙️ Prasyarat & Instalasi (Prerequisites & Installation)

**Prasyarat:**
* Python 3.8+
* Akses `sudo` untuk membaca file log sistem.

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

3.  **Install semua library yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 Cara Penggunaan (Usage)

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

## 📄 Contoh Output (Example Output)

Setelah dijalankan, skrip akan menampilkan laporan seperti ini di terminal:
