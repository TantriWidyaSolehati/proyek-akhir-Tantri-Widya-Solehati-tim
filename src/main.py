from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik, hitung_ketuntasan


def main():

	path_data = "../data/nilai_contoh.txt"

	data = baca_data(path_data)

	if not data:
		print("Tidak ada data yang dapat diproses.")
		return

	statistik = hitung_statistik(data)
	ketuntasan = hitung_ketuntasan(data)

	laporan = f"""
=== LAPORAN ANALISIS NILAI ===

Jumlah Data      : {len(data)}
Rata-rata Nilai  : {statistik['rata_rata']:.2f}
Nilai Maksimum   : {statistik['maksimum']}
Nilai Minimum    : {statistik['minimum']}

Jumlah Tuntas        : {ketuntasan['tuntas']}
Jumlah Belum Tuntas  : {ketuntasan['belum_tuntas']}
"""

	print(laporan)

	simpan_laporan(
		laporan,
		"../output/laporan_nilai.txt"
	)

	print("Laporan berhasil disimpan.")


if __name__ == "__main__":
	main()
