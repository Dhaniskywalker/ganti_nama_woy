import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib3

# Matikan warning SSL (biar nggak spam di console)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL utama
url_form = "https://antrianpanganbersubsidi.pasarjaya.co.id/index.php"

# Tambahkan User-Agent biar nggak ditolak server
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

try:
    # Ambil halaman utama (abaikan SSL verify)
    res = requests.get(url_form, headers=headers, verify=False)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text, "html.parser")
        form = soup.find("form", {"method": "post"})

        if form and form.get("action"):
            action_url = urljoin(url_form, form["action"])

            # Tampilkan di console
            print("✅ URL action terbaru:", action_url)

            # Simpan ke file
            with open("latest_url.txt", "w", encoding="utf-8") as f:
                f.write(action_url)

            print("💾 URL action disimpan ke latest_url.txt")

        else:
            print("❌ Form dengan action tidak ditemukan.")
    else:
        print("❌ Gagal akses halaman, status:", res.status_code)

except Exception as e:
    print("⚠ Terjadi error:", e)
