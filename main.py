# log_analyzer/main.py

import configparser
import os
from datetime import datetime

def analyze_log(log_path: str, keywords: list) -> list | None:
    """
    Membaca dan menganalisis sebuah file log untuk mencari kata kunci tertentu.

    Args:
        log_path (str): Path lengkap menuju file log.
        keywords (list): Sebuah list berisi string kata kunci yang akan dicari.

    Returns:
        list | None: Sebuah list berisi baris log yang cocok, atau None jika terjadi error.
    """
    print(f"[*] Menganalisis file: {log_path}")
    found_lines = []

    try:
        with open(log_path, 'r') as file:
            for line in file:
                # Menggunakan generator expression di dalam any() untuk pengecekan yang efisien.
                if any(keyword in line for keyword in keywords):
                    found_lines.append(line.strip())
    except FileNotFoundError:
        print(f"[!] Error: File log tidak ditemukan di '{log_path}'.")
        return None
    except PermissionError:
        print(f"[!] Error: Izin ditolak. Coba jalankan skrip dengan 'sudo'.")
        return None
        
    return found_lines

def create_report(folder: str, findings: list | None) -> None:
    """
    Membuat sebuah laporan teks dari hasil analisis.

    Args:
        folder (str): Direktori untuk menyimpan file laporan.
        findings (list | None): List berisi baris log dari fungsi analyze_log.
    """
    if findings is None:
        print("[*] Pembuatan laporan dilewati karena terjadi error sebelumnya.")
        return

    if not findings:
        print("[*] Tidak ada entri yang cocok. Laporan tidak dibuat.")
        return
        
    # Membuat nama file yang unik berdasarkan timestamp saat ini.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_filename = f"analysis_report_{timestamp}.txt"
    report_path = os.path.join(folder, report_filename)
    
    try:
        # Pastikan direktori output sudah ada sebelum menulis file.
        os.makedirs(folder, exist_ok=True)
            
        with open(report_path, 'w') as report_file:
            report_file.write(f"Laporan Analisis Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            report_file.write("="*40 + "\n\n")
            report_file.write(f"Ditemukan {len(findings)} entri yang cocok:\n\n")
            
            for line in findings:
                report_file.write(f"- {line}\n")
        
        print(f"[+] Laporan berhasil disimpan di: {report_path}")

    except OSError as e:
        print(f"[!] Gagal menyimpan laporan: {e}")


if __name__ == "__main__":
    # Inisialisasi parser untuk file konfigurasi.
    config = configparser.ConfigParser()
    config.read('config.ini')

    # --- Memuat Konfigurasi ---
    try:
        log_file = config.get('settings', 'log_file_path')
        keywords_str = config.get('settings', 'keywords')
        report_folder = config.get('output', 'report_folder')
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"[!] Error saat membaca config.ini: {e}")
        exit(1) # Hentikan skrip jika konfigurasi tidak lengkap.
    
    # Memisahkan string keywords dari config menjadi sebuah list.
    keywords_list = [k.strip() for k in keywords_str.split(',')]
    
    # --- Eksekusi ---
    found_data = analyze_log(log_file, keywords_list)
    create_report(report_folder, found_data)
