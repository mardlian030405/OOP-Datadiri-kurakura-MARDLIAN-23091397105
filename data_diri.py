# Definisikan Class DataDiri
class DataDiri:
    # Constructor untuk inisialisasi atribut
    def __init__(self, nama, kelas, nim, jurusan, fakultas, kampus):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.kampus = kampus

    # Method untuk menampilkan data diri
    def tampilkan_data_diri(self):
        print("-" * 45)  # Garis pembatas antar data
        print(f"Nama      : {self.nama}")
        print(f"Kelas     : {self.kelas}")
        print(f"NIM       : {self.nim}")
        print(f"Jurusan   : {self.jurusan}")
        print(f"Fakultas  : {self.fakultas}")
        print(f"Kampus    : {self.kampus}")
        print("-" * 45)  # Garis pembatas antar data

# Membuat Object dari class DataDiri
data_diri_mahasiswa = DataDiri(
    nama="M. MARDLIAN NUROFIQ",
    kelas="MANAJEMEN INFORMATIKA 2023C",
    nim="23091397105",
    jurusan="D4 MANAJEMEN INFORMATIKA",
    fakultas="Fakultas Vokasi",
    kampus="Universitas Negeri Surabaya"
)

# Memanggil method untuk menampilkan data diri
data_diri_mahasiswa.tampilkan_data_diri()