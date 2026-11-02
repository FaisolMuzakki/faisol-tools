import os
import sys
import time
import socket
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

def bersihkan_layar():
    os.system('clear')

def menu_utama():
    while True:
        bersihkan_layar()
        # Banner ASCII Art Keren untuk FAISOL M TOOLS
        print(Fore.GREEN + Style.BRIGHT + r"  _____ _    ___ ____   ___  _     ")
        print(Fore.GREEN + Style.BRIGHT + r" |  ___/ \  |_ _/ ___| / _ \| |    ")
        print(Fore.CYAN + Style.BRIGHT +  r" | |_ / _ \  | |\___ \| | | | |    ")
        print(Fore.CYAN + Style.BRIGHT +  r" |  _/ ___ \ | | ___) | |_| | |___ ")
        print(Fore.BLUE + Style.BRIGHT +  r" |_|/_/   \_\___|____/ \___/|_____|")
        print(Fore.MAGENTA + Style.BRIGHT + "     [ M  T O O L S  -  v1.0 ]     ")
        print(Fore.YELLOW + "=====================================")

        print(Fore.YELLOW + "1. Tes Koneksi Internet")
        print(Fore.YELLOW + "2. Cek IP Lokal")
        print(Fore.YELLOW + "3. DNS Lookup (Domain ke IP)")
        print(Fore.YELLOW + "4. Kamus Password Admin Router")
        print(Fore.RED + "0. Keluar")

        print(Fore.CYAN + "=====================================")
        
        pilihan = input(Fore.WHITE + "Pilih menu [0-3]: ")
        
        if pilihan == '1':
            print(Fore.CYAN + "\n[*] Menguji koneksi internet...")
            try:
                socket.setdefaulttimeout(3)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
                print(Fore.GREEN + Style.BRIGHT + "[+] KONEKSI BERHASIL: Anda terhubung ke internet!")
            except socket.error:
                print(Fore.RED + Style.BRIGHT + "[-] KONEKSI GAGAL: Periksa paket data atau Wi-Fi Anda!")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == '2':
            print(Fore.CYAN + "\n[*] Memeriksa IP Lokal perangkat Anda...")
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ip_lokal = s.getsockname()[0]
                s.close()
                print(Fore.GREEN + Style.BRIGHT + f"[+] IP LOKAL ANDA: {ip_lokal}")
            except Exception as e:
                print(Fore.RED + f"[-] Gagal mendapatkan IP Lokal: {e}")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == '3':
            print(Fore.CYAN + "\n=== DNS LOOKUP ===")
            domain = input(Fore.WHITE + "[*] Masukkan nama domain (contoh: google.com): ")
            if domain.strip() == "":
                print(Fore.RED + "[-] Domain tidak boleh kosong!")
            else:
                print(Fore.CYAN + f"[*] Mencari IP untuk {domain}...")
                try:
                    # Mengambil alamat IP dari domain yang diinput
                    ip_domain = socket.gethostbyname(domain)
                    print(Fore.GREEN + Style.BRIGHT + f"[+] IP DOMAIN: {ip_domain}")
                except socket.gaierror:
                    print(Fore.RED + Style.BRIGHT + "[-] GAGAL: Domain tidak ditemukan atau salah ketik!")
                except Exception as e:
                    print(Fore.RED + f"[-] Error: {e}")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == '4':
            print(Fore.CYAN + "\n=== KAMUS PASSWORD ADMIN ROUTER ===")
            print(Fore.WHITE + "Merek populer: ZTE, Huawei, TP-Link, Tenda, ASUS")
            cari = input(Fore.WHITE + "[*] Masukkan merek router yang dicari: ").strip().lower()
            
            # Database kamus password default router di Indonesia
            database_router = {
                "zte": [
                    {"Username": "admin", "Password": "admin (Umum)"},
                    {"Username": "user", "Password": "user (Akses terbatas)"},
                    {"Username": "admin", "Password": "Telkomsel@123 (Orbit)"},
                    {"Username": "Telkomadmin", "Password": "admintelecom (IndiHome)"}
                ],
                "huawei": [
                    {"Username": "admin", "Password": "admin"},
                    {"Username": "Telekomadmin", "Password": "admintelecom (IndiHome)"},
                    {"Username": "root", "Password": "admin"}
                ],
                "tp-link": [
                    {"Username": "admin", "Password": "admin"},
                    {"Username": "admin", "Password": "password"}
                ],
                "tenda": [
                    {"Username": "admin", "Password": "admin"},
                    {"Username": "admin", "Password": "(Kosongkan/Tanpa password)"}
                ],
                "asus": [
                    {"Username": "admin", "Password": "admin"}
                ]
            }
            
            found = False
            print(Fore.CYAN + f"\n[*] Hasil pencarian untuk merek: {cari.upper()}")
            print(Fore.YELLOW + "---------------------------------------------")
            
            for merk, akun_list in database_router.items():
                if cari in merk:
                    found = True
                    for akun in akun_list:
                        print(Fore.GREEN + f"[+] Username: {akun['Username']} | Password: {akun['Password']}")
            
            if not found:
                print(Fore.RED + "[-] Merek tidak ditemukan atau belum ada di kamus.")
                print(Fore.WHITE + "[*] Tips: Coba kombinasi umum -> U: admin | P: admin")
                
            print(Fore.YELLOW + "---------------------------------------------")
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == '0':
            print(Fore.RED + "\nTerima kasih telah menggunakan FAISOL M TOOLS!")
            sys.exit()
            
        else:
            print(Fore.RED + "\nPilihan tidak valid!")
            time.sleep(1.5)

if __name__ == "__main__":
    menu_utama()

