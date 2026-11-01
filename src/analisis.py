from utilitas import tentukan_status


def hitung_statistik(data):
	"""
	Menghitung statistik data nilai.
	"""

	daftar_nilai = [item["nilai"] for item in data]

	statistik = {
		"rata_rata": sum(daftar_nilai) / len(daftar_nilai),
		"maksimum": max(daftar_nilai),
		"minimum": min(daftar_nilai)
	}

	return statistik


def hitung_ketuntasan(data, kkm=75):
	"""
	Menghitung jumlah siswa tuntas dan belum tuntas.
	"""

	tuntas = 0
	belum_tuntas = 0

	for siswa in data:
		status = tentukan_status(siswa["nilai"], kkm)

		if status == "Tuntas":
			tuntas += 1
		else:
			belum_tuntas += 1

	return {
		"tuntas": tuntas,
		"belum_tuntas": belum_tuntas
	}
