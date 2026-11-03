print("=== PROGRAM NILAI MAHASISWA ===")

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

if jumlah_mahasiswa <= 0:
    print("Jumlah mahasiswa harus lebih dari 0!")

else:
    total_nilai = 0
    daftar_nilai = []

    for i in range(1, jumlah_mahasiswa + 1):
        nilai = float(input(f"Masukkan Nilai Mahasiswa {i}: "))

        daftar_nilai.append(nilai)
        total_nilai += nilai

    rata_rata = total_nilai / jumlah_mahasiswa

    print("\n=== HASIL PERHITUNGAN ===")

    for i in range(jumlah_mahasiswa):
        if daftar_nilai[i] >= 60:
            status = "Lulus"
        else:
            status = "Tidak Lulus"

        print(f"Mahasiswa {i + 1}: {daftar_nilai[i]} - {status}")

    print(f"\nTotal Nilai: {total_nilai}")
    print(f"Rata-rata: {rata_rata:.2f}")

    if rata_rata >= 60:
        print("Keterangan: Rata-rata mahasiswa Lulus")
    else:
        print("Keterangan: Rata-rata mahasiswa Tidak Lulus")
