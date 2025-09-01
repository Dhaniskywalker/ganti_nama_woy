import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://antrianpanganbersubsidi.pasarjaya.co.id"
URL_FORM = f"{BASE_URL}/index.php"
URL_KOUTA = f"{BASE_URL}/kouta.php"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

session = requests.Session()

# 1. Ambil daftar wilayah dari form utama
resp = session.get(URL_FORM, headers=headers, verify=False)
soup = BeautifulSoup(resp.text, "html.parser")

wilayah_opts = soup.select("select#wilayah option")
wilayah_dict = {
    opt["value"]: opt.text.strip()
    for opt in wilayah_opts if opt["value"]
}

print("Wilayah ditemukan:", wilayah_dict)

data = {}

# 2. Untuk tiap wilayah → ambil lokasi via kouta.php
for kode_wilayah, nama_wilayah in wilayah_dict.items():
    payload = {"wilayah": kode_wilayah}
    r = session.post(URL_KOUTA, data=payload, headers=headers, verify=False)
    try:
        lokasi_data = r.json()  # coba parse JSON
    except Exception:
        lokasi_data = {}

    lokasi_dict = {}
    for loc in lokasi_data:
        lokasi_dict[loc["id"]] = loc["nama"]

    data[nama_wilayah] = lokasi_dict

# 3. Simpan ke list.json
with open("list.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ list.json berhasil dibuat")
