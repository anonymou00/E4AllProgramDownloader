#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
██████╗░██╗░░██╗░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██║░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██████╔╝█████═╝░███████║░░░██║░░░███████║██████╦╝
██╔═══╝░██╔═██╗░██╔══██║░░░██║░░░██╔══██║██╔══██╗
██║░░░░░██║░╚██╗██║░░██║░░░██║░░░██║░░██║██████╦╝
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░

💀 ChatGPT & 😈 & E4lord  tarafından yazılmıştır
🔥 3000+ Red Team aracıyla Linux Mint'i dönüştürür
"""

import subprocess
import os

def run_cmd(command, check=True):
    print(f"💻 Komut: {' '.join(command)}")
    subprocess.run(command, check=check)

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"📄 Yazıldı: {path}")

def main():
    print("🚀 Kurulum başlıyor | Hazırlayan: ChatGPT & 😈 & E4lord")

    if os.geteuid() != 0:
        print("❌ Root olmalısın! sudo ile çalıştır.")
        return

    run_cmd(["apt", "update"])
    run_cmd(["apt", "upgrade", "-y"])

    if not os.path.exists("/swapfile"):
        print("📀 Swap oluşturuluyor...")
        run_cmd(["fallocate", "-l", "2G", "/swapfile"])
        run_cmd(["chmod", "600", "/swapfile"])
        run_cmd(["mkswap", "/swapfile"])
        run_cmd(["swapon", "/swapfile"])
        with open("/etc/fstab", "a") as f:
            f.write("/swapfile none swap sw 0 0\n")

    kali_list = "/etc/apt/sources.list.d/kali.list"
    if not os.path.exists(kali_list):
        write_file(kali_list, "deb http://http.kali.org/kali kali-rolling main non-free contrib")

    if not os.path.exists("/etc/apt/trusted.gpg.d/kali.gpg"):
        run_cmd(["curl", "-fsSL", "https://archive.kali.org/archive-key.asc", "-o", "/tmp/kali.asc"])
        run_cmd(["gpg", "--dearmor", "-o", "/etc/apt/trusted.gpg.d/kali.gpg", "/tmp/kali.asc"])

    pref_path = "/etc/apt/preferences.d/kali.pref"
    if not os.path.exists(pref_path):
        write_file(pref_path, """Package: *
Pin: release o=Kali
Pin-Priority: 10""")

    run_cmd(["apt", "update"])

    print("🛠️  kali-linux-everything (3000+ tool) kuruluyor...")
    run_cmd(["apt", "install", "kali-linux-everything", "-y"])

    run_cmd(["xfce4-panel", "--restart"])

    print("\n✅ KURULDU! ChatGPT & 😈 & E4lord efsanesi aktif!")
    print("🖤 Her zamanki gibi, aşk ile yazıldı.")

if __name__ == "__main__":
    main()
