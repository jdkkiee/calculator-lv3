def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 == 0:
        return "Tidak bisa membagi dengan 0."
    return angka1 / angka2

while True:

    print("\n=== KALKULATOR ===")
    print("1. Hitung")
    print("2. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "2":
        print("Program selesai.")
        break

    elif pilihan == "1":

        try:
            angka1 = float(input("Masukkan angka pertama: "))
            operator = input("Masukkan operator (+, -, *, /): ")
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if operator == "+":
            hasil = angka1 + angka2

        elif operator == "-":
            hasil = angka1 - angka2

        elif operator == "*":
            hasil = angka1 * angka2

        elif operator == "/":
            hasil = angka1 / angka2

        else:
            hasil = "Operator tidak valid"

        print("Hasil:", hasil)

    else:
        print("Pilihan tidak valid.")

try:
    angka1 = float(input("Masukan Angka:"))
except ValueError:
    print("Input harus berubah angka!")
