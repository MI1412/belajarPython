
# pangkat
urutan = sum(i*i for i in range(10))
print(f"urutan kali: {urutan}")

# perkalian vector
x = [4,5,6]
y = [7,8,9]
print(sum(x*y for x,y in zip(x,y)))

# mengambil kata unik
page = [
    "Python is a great programming language",
    "Python is versatile and powerful",
    "Programming in Python is fun and productive"
]
kata_unik = set(kata for baris in page for kata in baris.split())
print(f"unik: {kata_unik}")

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


# mengambil nilai max
# Daftar lulusan
graduates = [
    Student("Alice", 3.9),
    Student("Bob", 3.7),
    Student("Charlie", 4.0),
    Student("David", 3.8)
]

valedictorian = max((student.gpa, student.name) for student in graduates)

# Output valedictorian
print(f"Valedictorian: {valedictorian[1]} with GPA: {valedictorian[0]}")

data = input("input: ")
reverse = list(data[i] for i in range(len(data) -1,-1,-1)) # index, posisi, pengurangan
print(reverse)