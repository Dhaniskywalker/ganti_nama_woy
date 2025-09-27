<?php
// Ambil session dari server tujuan
$ch = curl_init("https://antrianpanganbersubsidi.pasarjaya.co.id/index.php");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, true);
$response = curl_exec($ch);

if ($response === false) {
    echo json_encode(["error" => curl_error($ch)]);
    curl_close($ch);
    exit;
}
curl_close($ch);

// Cari cookie PHPSESSID dari response
if (preg_match('/PHPSESSID=([^;]+)/', $response, $matches)) {
    echo json_encode(["phpsessid" => $matches[1]]);
} else {
    echo json_encode(["phpsessid" => null]);
}