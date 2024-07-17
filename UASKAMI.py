import os
os.system("cls")
def main():
    print("================================================")
    print("          PROGRAM PEMBAGIAN GAJI                ")
    print("================================================")
    print("")
    jumlah_karyawan = int(input(" => MASUKAN JUMLAH KARYAWAN : "))
    karyawan_gajian = []

    for i in range(jumlah_karyawan):
        print("------------------------------------------------")
        print("1.Manager")
        print("2.Staff")
        print("3.Assistant")
        print("4.Supervisor")
        jabatan = int(input(f"> MASUKAN JABATAN KARYAWAN {i + 1} : "))

        switcher = {
            1: {"gaji": 5000000, "jabatan": "Manager"},
            2: {"gaji": 2000000, "jabatan": "Staff"},
            3: {"gaji": 1500000, "jabatan": "Assistant"},
            4: {"gaji": 2500000, "jabatan": "Supervisor"}
        }

        if jabatan in switcher:
            gaji = switcher[jabatan]["gaji"]
            jabatank = switcher[jabatan]["jabatan"]
        else:
            print("Jabatan tidak valid. Silakan coba lagi.")
            continue

        print("-----------------------------------------------")
        print(f"Jabatan yang anda pilih adalah {jabatank}")
        nilai_keterampilan = float(input("> MASUKAN NILAI KETERAMPILAN KARYAWAN  [1-10] : "))
        nilai_kehadiran = float(input("> MASUKAN NILAI KEHADIRAN KARYAWAN  [1-10] : "))
        nilai_kedisiplinan = float(input("> MASUKAN NILAI KEDISIPLINAN KARYAWAN  [1-10] : "))
        nilai_pencapaian = float(input("> MASUKAN NILAI PENCAPAIAN KARYAWAN  [1-10] : "))

        nilai = nilai_keterampilan + nilai_kehadiran + nilai_kedisiplinan + nilai_pencapaian
        persentase = (nilai / 4) * 10

        if persentase >= 90:
            bonus = gaji * 0.20
            gaji += bonus
            print(f"> Karyawan mendapatkan bonus sebesar Rp.{bonus}")
        elif 60 <= persentase < 90:
            print(f"> Gaji yang anda dapatkan adalah : Rp.{gaji}")
        elif 40 <= persentase < 60:
            pemotongan = gaji * 0.50
            gaji -= pemotongan
            print(f"> Gaji anda di kurangi sebanyak : Rp.{pemotongan}")
        elif 0 <= persentase < 40:
            print("> maaf anda tidak mendapatkan gaji karena anda malas-malasan")
            gaji = 0

        
        print("================================================================")
        print(f"Nilai keterapilan: {nilai_keterampilan}")
        print(f"Nilai kehadiran: {nilai_kehadiran}")
        print(f"Nilai kedisiplinan: {nilai_kedisiplinan}")
        print(f"Nilai pencapaian: {nilai_pencapaian}")
        print(f"Rating Karyawan: {persentase}%")
        print(f"Karyawan ke-{i + 1} (jabatan: {jabatank}) setelah pembagian : Rp.{gaji}")
        karyawan_gajian.append(f"{i + 1}. {jabatank} ")
        
if __name__ == "__main__":
    main()