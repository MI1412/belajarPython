# prinsip tanggung jawab tunggal / Single Responsibility Principle (SRP), artinya Sebuah kelas hanya harus memiliki satu tugas utama. Jika sebuah kelas melakukan terlalu banyak hal, akan sulit memeliharanya.
# contoh:
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# Kelas lain yang bertanggung jawab mengirim email
class EmailService:
    def send_email(self, user):
        print(f"Sending email to {user.email}")