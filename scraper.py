import requests
from bs4 import BeautifulSoup
import urllib3
import json
import sys

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

URL = "https://antrianpanganbersubsidi.pasarjaya.co.id/index.php"

try:
    res = requests.get(URL, verify=False, timeout=30)
    res.raise_for_status()
except requests.RequestException as e:
    print(f"❌ Gagal mengambil data dari {URL}: {e}")
    sys.exit(1)

soup = BeautifulSoup(res.text, "html.parser")

# Cari dropdown wilayah & lokasi
wilayah_select = soup.find("select", {"id": "wilayah"})
lokasi_select = soup.find("select", {"id": "lokasi"})

wilayah_data = []
lokasi_data = []

if wilayah_select:
    for option in wilayah_select.find_all("option"):
        val = option.get("value", "").strip()
        text = option.text.strip()
        if val and text and val != "0":
            wilayah_data.append({"value": val, "text": text})

if lokasi_select:
    for option in lokasi_select.find_all("option"):
        val = option.get("value", "").strip()
        text = option.text.strip()
        if val and text and val != "0":
            lokasi_data.append({"value": val, "text": text})

output = {
    "wilayah": wilayah_data,
    "lokasi": lokasi_data
}

# Simpan ke list.json
with open("list.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("✅ Data berhasil disimpan ke list.json")
