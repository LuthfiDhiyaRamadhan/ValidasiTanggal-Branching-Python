tanggal=int(input("Masukan tanggal:"))
bulan=int(input("Masukan bulan:"))
tahun=int(input("Masukan tahun:"))
if bulan>=1 and bulan <=12 :
    if bulan==1 or bulan ==3 or bulan ==5 or bulan ==7\
        or bulan ==8 or bulan==10 or bulan==12:
        maks_tanggal=31
    elif bulan ==2:
        maks_tanggal =28
        if (tahun % 100 != 0) and (tahun % 4 == 0) or \
            (tahun % 100 == 0) and (tahun % 400 == 0):
            maks_tanggal=29
    else:
        maks_tanggal=30
    if tanggal >1 and tanggal <=maks_tanggal:
        print(f"Tanggal {tanggal}{bulan}{tahun}Valid")
    else:
        print("Tanggal invalid")
else:
    print("Tanggal Salah. Bulan Salah")