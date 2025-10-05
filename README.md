## 🚀 Cara Penggunaan (Usage)

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
