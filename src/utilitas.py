def validasi_nilai(nilai):
	"""
	Memeriksa apakah nilai berada pada rentang 0-100.
	"""
	return 0 <= nilai <= 100


def tentukan_status(nilai, kkm=75):
	"""
	Menentukan status ketuntasan siswa.
	"""
	if nilai >= kkm:
		return "Tuntas"
	return "Belum Tuntas"
