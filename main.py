# === Mengambil Alat-Alat yang Dibutuhkan ===
# Bayangkan kamu mau bikin kue, kamu butuh resep, oven, dan bahan.
# Baris-baris di bawah ini seperti mengambil 'alat' yang kita perlukan untuk program kita.

import configparser  # Ini alat untuk membaca file konfigurasi (seperti membaca resep dari buku).
import os            # Ini alat untuk berinteraksi dengan sistem operasi, misalnya membuat folder.
from datetime import datetime # Ini alat untuk mendapatkan tanggal dan waktu saat ini.

# === Fungsi untuk Menganalisis Log ===
# Ini adalah 'resep' atau set instruksi pertama kita.
# Namanya 'analyze_log', tugasnya membaca file log dan mencari kata kunci.
def analyze_log(log_path, keywords):
    
    # Cetak pesan ke layar untuk memberitahu kita bahwa analisis dimulai.
    print(f"[*] Memulai analisis pada file: {log_path}")
    
    # Siapkan sebuah 'keranjang' kosong untuk menampung baris-baris yang kita temukan.
    found_lines = []
    
    # 'try...except' itu seperti berkata, "Coba lakukan ini, tapi kalau ada masalah, jangan panik."
    try:
        # Buka file log yang alamatnya ada di 'log_path'. 'r' artinya kita hanya akan 'read' (membaca).
        # 'with open' memastikan filenya akan ditutup otomatis setelah selesai.
        with open(log_path, 'r') as file:
            
            # Baca file tersebut baris demi baris, seperti membaca buku halaman per halaman.
            for line in file:
                
                # Untuk setiap baris, cek apakah ada 'keyword' (kata kunci) yang kita cari di dalamnya.
                # 'any(...)' akan bernilai True jika salah satu saja kata kunci ditemukan.
                if any(keyword in line for keyword in keywords):
                    
                    # Jika ditemukan, masukkan baris itu ke dalam 'keranjang' kita.
                    # .strip() fungsinya untuk membersihkan spasi kosong di awal dan akhir baris.
                    found_lines.append(line.strip())
                    
    # Kalau ada masalah 'FileNotFoundError' (file tidak ditemukan)...
    except FileNotFoundError:
        # ...cetak pesan error ini ke layar.
        print(f"[!] Error: File log di '{log_path}' tidak ditemukan.")
        # ...dan hentikan fungsi dengan mengembalikan 'None' (tidak ada hasil).
        return None
        
    # Kalau ada masalah 'PermissionError' (kita tidak punya izin untuk baca filenya)...
    except PermissionError:
        # ...cetak pesan error ini dan sarankan untuk pakai 'sudo'.
        print(f"[!] Error: Izin ditolak. Coba jalankan skrip dengan 'sudo'.")
        # ...dan hentikan juga fungsinya.
        return None
        
    # Jika semua berjalan lancar, kembalikan 'keranjang' yang sudah berisi hasil temuan.
    return found_lines

# === Fungsi untuk Membuat Laporan ===
# Ini adalah 'resep' kedua kita, namanya 'create_report'.
# Tugasnya adalah mengambil hasil temuan dan menuliskannya ke dalam sebuah file laporan.
def create_report(folder, findings):
    
    # Jika hasil temuannya 'None' (artinya ada error di fungsi sebelumnya)...
    if findings is None:
        # ...beri tahu pengguna dan jangan lakukan apa-apa lagi.
        print("[*] Tidak ada laporan yang dibuat karena terjadi error.")
        return

    # Jika hasil temuannya adalah keranjang kosong (tidak ada kata kunci yang ditemukan)...
    if not findings:
        # ...beri tahu pengguna dan jangan buat file laporan.
        print("[*] Tidak ada baris yang cocok dengan kata kunci. Laporan tidak dibuat.")
        return
        
    # Dapatkan waktu sekarang dan format menjadi teks yang rapi untuk nama file.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Buat nama file laporan yang unik, contohnya: "analysis_report_2025-10-05_16-45-00.txt"
    report_filename = f"analysis_report_{timestamp}.txt"
    
    # Gabungkan nama folder dan nama file menjadi satu alamat lengkap.
    report_path = os.path.join(folder, report_filename)
    
    # Coba lagi, kali ini untuk menulis file.
    try:
        # Cek apakah folder untuk laporan sudah ada atau belum.
        if not os.path.exists(folder):
            # Jika belum ada, buat foldernya.
            os.makedirs(folder)
            
        # Buka (atau buat) file laporan. 'w' artinya kita akan 'write' (menulis) ke dalamnya.
        with open(report_path, 'w') as report_file:
            
            # Tulis judul laporan beserta waktu pembuatannya.
            report_file.write(f"Laporan Analisis Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            # Tulis garis pemisah biar rapi.
            report_file.write("="*40 + "\n\n")
            # Tulis ringkasan berapa banyak baris yang ditemukan.
            report_file.write(f"Ditemukan {len(findings)} baris yang cocok:\n\n")
            
            # Ulangi untuk setiap baris yang ada di dalam 'keranjang' hasil temuan.
            for line in findings:
                # Tulis setiap baris tersebut ke dalam file laporan.
                report_file.write(f"- {line}\n")
        
        # Jika semua berhasil, cetak pesan sukses ke layar.
        print(f"[+] Laporan berhasil disimpan di: {report_path}")

    # Jika ada masalah lain saat mencoba menyimpan file...
    except Exception as e:
        # ...cetak pesan errornya.
        print(f"[!] Gagal menyimpan laporan: {e}")


# === Bagian Utama Program ===
# Di sinilah program kita benar-benar mulai berjalan.
# Kode di dalam 'if' ini hanya akan berjalan jika kita menjalankan file ini secara langsung.
if __name__ == "__main__":
    
    # Buat sebuah 'pembaca resep' dari alat configparser.
    config = configparser.ConfigParser()
    # Suruh 'pembaca' itu untuk membaca file 'config.ini'.
    config.read('config.ini')

    # Dari 'resep' itu, ambil informasi-informasi berikut:
    # Ambil alamat file log dari bagian [settings].
    log_file = config.get('settings', 'log_file_path')
    # Ambil daftar kata kunci dari bagian [settings].
    keywords_str = config.get('settings', 'keywords')
    # Ambil nama folder laporan dari bagian [output].
    report_folder = config.get('output', 'report_folder')
    
    # Kata kunci tadi masih jadi satu kalimat, kita perlu memisahnya menjadi sebuah daftar (list).
    # "error,warning" akan menjadi ['error', 'warning'].
    keywords_list = [k.strip() for k in keywords_str.split(',')]
    
    # Sekarang, panggil 'resep' pertama kita (analyze_log) untuk mulai bekerja.
    # Berikan alamat file dan daftar kata kunci yang sudah kita siapkan.
    # Hasilnya kita simpan di variabel 'found_data'.
    found_data = analyze_log(log_file, keywords_list)
    
    # Terakhir, panggil 'resep' kedua kita (create_report).
    # Berikan nama folder dan 'found_data' (hasil dari analisis) agar bisa dibuat laporannya.
    create_report(report_folder, found_data)