import turtle

# Definisikan class TurtleSegitiga
class TurtleSegitiga:
    # Constructor untuk inisialisasi turtle dan ukuran sisi segitiga
    def __init__(self, sisi):
        self.sisi = sisi
        self.t = turtle.Turtle()  # Membuat object turtle
        self.t.shape("turtle")
        self.t.pencolor("blue")  # Set warna garis menjadi biru

    # Method untuk menggambar satu segitiga
    def gambar_segitiga(self):
        for _ in range(3):
            self.t.forward(self.sisi)  # Maju sesuai ukuran sisi
            self.t.left(120)  # Belok kiri 120 derajat untuk membuat segitiga

       # Method untuk menggambar delapan segitiga
    def gambar_delapan_segitiga(self):
        # Hitung jarak yang diperlukan agar segitiga berada di tengah
        total_width = (8 * self.sisi) + (7 * 20)  # Total panjang 8 segitiga dan jarak antar segitiga
        start_x = -total_width / 2  # Posisi x untuk memulai agar berada di tengah
        
        # Pindah ke posisi awal (kiri layar)
        self.t.penup()
        self.t.goto(start_x, 0)  # Posisi y=0 agar segitiga berada di garis tengah
        self.t.pendown()

        # Gambar delapan segitiga
        for _ in range(8):
            self.gambar_segitiga()  # Gambar segitiga
            self.t.penup()  # Angkat pena agar tidak menggambar saat berpindah
            self.t.forward(self.sisi + 20)  # Pindah ke posisi baru
            self.t.pendown()  # Turunkan pena untuk menggambar lagi

    # Method untuk menutup jendela turtle
    def selesai(self):
        turtle.done()

# Membuat object dari class TurtleSegitiga dengan ukuran sisi segitiga 100
segitiga = TurtleSegitiga(100)

# Memanggil method untuk menggambar tiga segitiga
segitiga.gambar_delapan_segitiga()

# Menutup jendela turtle setelah selesai
segitiga.selesai()
