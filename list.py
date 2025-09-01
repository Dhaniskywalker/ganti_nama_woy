import requests
from bs4 import BeautifulSoup
import urllib3

# Matikan warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://antrianpanganbersubsidi.pasarjaya.co.id/index.php"
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text, "html.parser")

# Ambil dropdown wilayah
wilayah_select = soup.find("select", {"id": "wilayah"})
lokasi_select = soup.find("select", {"id": "lokasi"})

wilayah_data = []
lokasi_data = []

if wilayah_select:
    for option in wilayah_select.find_all("option"):
        if option.get("value") and option.text.strip():
            wilayah_data.append({
                "value": option.get("value"),
                "text": option.text.strip()
            })

if lokasi_select:
    for option in lokasi_select.find_all("option"):
        if option.get("value") and option.text.strip():
            lokasi_data.append({
                "value": option.get("value"),
                "text": option.text.strip()
            })

print("Wilayah:", wilayah_data)
print("Lokasi:", lokasi_data)
