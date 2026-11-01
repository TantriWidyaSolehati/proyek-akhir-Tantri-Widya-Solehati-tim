from utilitas import validasi_nilai


def baca_data(path_file):
	"""
	Membaca data nilai dari file teks.
	Format:
	Nama,Nilai
	"""

	data = []

	try:
		with open(path_file, "r", encoding="utf-8") as file:
			for baris in file:
				bagian = baris.strip().split(",")

				if len(bagian) != 2:
					continue

				nama = bagian[0]
				nilai = int(bagian[1])

				if validasi_nilai(nilai):
					data.append(
						{
							"nama": nama,
							"nilai": nilai
						}
					)

	except FileNotFoundError:
		print("Error: File tidak ditemukan!")

	return data


def simpan_laporan(teks_laporan, path_file):
	"""
	Menyimpan laporan ke file.
	"""
	with open(path_file, "w", encoding="utf-8") as file:
		file.write(teks_laporan)
